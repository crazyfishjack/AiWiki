## ADDED Requirements

### Requirement: Config management isolates sensitive data
The system SHALL keep all API keys and webhook URLs in a dedicated configuration file, separate from code.

#### Scenario: Config file structure
- **WHEN** creating the configuration
- **THEN** the file SHALL follow the same structure as `config.example.json` in wiki-research skill, with additional fields for阿里云 and 企业微信:
  ```json
  {
    "wiki_root": "<path>",
    "raw_default_dir": "raw/articles",
    "proxy": "http://127.0.0.1:7897",
    "api_keys": {
      "tavily": "",
      "exa": "",
      "firecrawl": "",
      "jina": "",
      "aliyun": ""
    },
    "webhooks": {
      "wechat": ""
    },
    "research_defaults": {
      "max_subqueries": 6,
      "max_deep_read_urls": 10,
      "exa_highlight_char_limit": 4000,
      "evidence_full_content": true,
      "tavily_min_score": 0.4
    },
    "llm_config": {
      "model": "qwen3.5-plus",
      "max_tokens": 8192,
      "temperature": 0.7
    }
  }
  ```

#### Scenario: GitHub Secrets mapping
- **WHEN** running in GitHub Actions
- **THEN** the system SHALL map Secrets to config fields as follows:
  - `TAVILY_API_KEY` → `api_keys.tavily`
  - `EXA_API_KEY` → `api_keys.exa`
  - `FIRECRAWL_API_KEY` → `api_keys.firecrawl`
  - `JINA_API_KEY` → `api_keys.jina`
  - `ALIYUN_API_KEY` → `api_keys.aliyun`
  - `WECHAT_WEBHOOK_URL` → `webhooks.wechat`

### Requirement: Config file is excluded from version control
The system SHALL ensure sensitive configuration files are never committed.

#### Scenario: Git ignore protection
- **WHEN** the config file `.github/scripts/config.local.json` exists
- **THEN** `.gitignore` SHALL contain `.github/scripts/config.local.json` and `.github/scripts/config.*.local.json`

### Requirement: Config validation fails fast
The system SHALL validate configuration before executing any API calls.

#### Scenario: Validate all required keys
- **WHEN** loading configuration
- **THEN** the system SHALL check that all required keys are present and non-empty, and exit with code 1 if any are missing

#### Scenario: Validate proxy URL format
- **WHEN** a proxy is configured
- **THEN** the system SHALL validate it is a valid HTTP/HTTPS URL
