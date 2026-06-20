## ADDED Requirements

### Requirement: Research executor orchestrates the full pipeline
The system SHALL provide a single entry point script that coordinates all steps of the automated research workflow.

#### Scenario: Execute complete research pipeline
- **WHEN** the script `run-research.py` is invoked with a query string
- **THEN** it SHALL execute in sequence: config loading → issue parsing → research → LLM compilation → git push → notification

#### Scenario: Pipeline handles partial failures gracefully
- **WHEN** any step in the pipeline fails
- **THEN** subsequent steps SHALL be skipped, an error summary SHALL be logged, and the notification step SHALL still attempt to send a failure message

### Requirement: Config loader supports dual-mode configuration
The system SHALL load sensitive configuration from GitHub Secrets (priority) or a local JSON file (fallback).

#### Scenario: Load from GitHub Secrets
- **WHEN** the script runs in GitHub Actions environment
- **THEN** it SHALL read all API keys from environment variables injected by GitHub Secrets

#### Scenario: Load from local config file
- **WHEN** the script runs locally and no environment variables are set
- **THEN** it SHALL attempt to read from `.github/scripts/config.local.json`

#### Scenario: Missing required config fails fast
- **WHEN** a required API key is missing from both sources
- **THEN** the script SHALL exit with code 1 and print the missing key name

### Requirement: Issue parser extracts research intent
The system SHALL parse GitHub Issue event payload to extract the research query.

#### Scenario: Parse from GitHub event JSON
- **WHEN** the `GITHUB_EVENT_PATH` environment variable points to a valid issue event JSON
- **THEN** the parser SHALL extract `issue.title` and `issue.body` and determine the query

#### Scenario: Parse from command line argument
- **WHEN** the script is invoked with `--query` argument
- **THEN** it SHALL use the provided query directly, bypassing issue parsing

### Requirement: Research runner invokes four-tool research
The system SHALL execute the existing `four_tool_research.py` script with the extracted query.

#### Scenario: Run standard research mode
- **WHEN** the query is extracted and config is loaded
- **THEN** the system SHALL invoke `python .github/scripts/four_tool_research.py --query "<query>" --mode standard --raw-dir raw/articles`

#### Scenario: Research output is captured
- **WHEN** the research script completes
- **THEN** the system SHALL capture the generated evidence file path from stdout (`RAW_RESEARCH_FILE=`)

### Requirement: Git pusher commits and pushes results
The system SHALL commit the generated research report to the repository and push to origin.

#### Scenario: Successful git push
- **WHEN** the research report is generated at `raw/articles/<filename>.md`
- **THEN** the system SHALL execute `git add`, `git commit` with message `[auto-research] <query>`, and `git push origin main`

#### Scenario: Git push conflict handling
- **WHEN** `git push` fails due to remote changes
- **THEN** the system SHALL attempt `git pull --rebase` and retry push once; if still failing, report error
