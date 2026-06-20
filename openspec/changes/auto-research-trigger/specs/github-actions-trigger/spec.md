## ADDED Requirements

### Requirement: GitHub Actions workflow listens for new issues
The system SHALL automatically trigger when a user creates a new GitHub Issue in the repository.

#### Scenario: Issue creation triggers workflow
- **WHEN** a user creates a new issue with title starting with `[调研]`
- **THEN** the GitHub Actions workflow `auto-research.yml` SHALL execute within 60 seconds

#### Scenario: Non-research issues are ignored
- **WHEN** a user creates an issue without the `[调研]` prefix in the title
- **THEN** the workflow SHALL skip execution and exit with status 0

### Requirement: Workflow extracts research topic from issue
The system SHALL parse the issue title and body to determine the research query.

#### Scenario: Extract query from issue title
- **WHEN** the workflow receives an issue with title `[调研] 2026年大模型在招投标领域的最新应用`
- **THEN** the system SHALL extract the query string `2026年大模型在招投标领域的最新应用`

#### Scenario: Extract query from issue body when title is generic
- **WHEN** the issue title is `[调研]` and the body contains a research topic
- **THEN** the system SHALL use the first non-empty line of the body as the query

### Requirement: Workflow configures execution environment
The system SHALL set up Python 3.11+ and install required dependencies before executing research.

#### Scenario: Environment setup succeeds
- **WHEN** the workflow starts executing
- **THEN** it SHALL install Python 3.11, pip, and dependencies from `requirements.txt`

### Requirement: Workflow passes secrets to research script
The system SHALL inject all API keys and webhook URLs as environment variables.

#### Scenario: Secrets are available in script
- **WHEN** the workflow runs the research script
- **THEN** environment variables `TAVILY_API_KEY`, `EXA_API_KEY`, `FIRECRAWL_API_KEY`, `JINA_API_KEY`, `ALIYUN_API_KEY`, `WECHAT_WEBHOOK_URL` SHALL be set
