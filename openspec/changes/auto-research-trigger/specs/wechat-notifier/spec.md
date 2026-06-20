## ADDED Requirements

### Requirement: WeChat notifier sends completion notification
The system SHALL send a notification to the configured企业微信 webhook when research completes or fails.

#### Scenario: Success notification
- **WHEN** the research pipeline completes successfully and the report is pushed
- **THEN** the system SHALL POST a markdown-formatted message to the企业微信 webhook containing: research topic, report file path (relative to repo), 3-5 core conclusions, and execution status

#### Scenario: Failure notification
- **WHEN** any step in the pipeline fails
- **THEN** the system SHALL POST a failure notification containing: research topic, error step, error summary, and a link to the GitHub Actions run log

#### Scenario: Notification respects webhook URL configuration
- **WHEN** `WECHAT_WEBHOOK_URL` is not configured
- **THEN** the notification step SHALL be skipped with a warning log, not fail the pipeline

### Requirement: Notification content follows template
The system SHALL format notifications using a consistent markdown template.

#### Scenario: Success message format
- **WHEN** formatting a success notification
- **THEN** the message SHALL follow this structure:
  ```markdown
  ## 自动调研完成
  **调研主题**: <query>
  **报告路径**: <file_path>
  **执行时间**: <timestamp>
  **核心结论**:
  1. <conclusion 1>
  2. <conclusion 2>
  ...
  ```

#### Scenario: Failure message format
- **WHEN** formatting a failure notification
- **THEN** the message SHALL follow this structure:
  ```markdown
  ## 自动调研失败
  **调研主题**: <query>
  **失败环节**: <failed_step>
  **错误摘要**: <error_summary>
  **查看日志**: <actions_run_url>
  ```
