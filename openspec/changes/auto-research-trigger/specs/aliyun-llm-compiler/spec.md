## ADDED Requirements

### Requirement: LLM compiler compiles evidence into Chinese report
The system SHALL invoke阿里云 Qwen API to compile the raw evidence package into a structured Chinese research report.

#### Scenario: Compile evidence with Qwen
- **WHEN** the evidence file path is available and `ALIYUN_API_KEY` is configured
- **THEN** the system SHALL read the evidence file, construct a prompt following the wiki-research SKILL.md compilation rules, and call the Qwen API

#### Scenario: Compiled report follows required structure
- **WHEN** the LLM compilation completes
- **THEN** the output SHALL contain sections: `## 核心结论`, `## 内容整理`, `## 推荐工作流`, `## 适用场景`, `## 不适用场景`, `## 风险与约束`, `## 信源质量门控记录`, `## 来源与可信度`, `## 对于可信度较高的来源逐来源总结`, `## 跨源矛盾检测结论`, `## 矛盾与待验证问题`, `## 原始证据摘录`

#### Scenario: LLM compilation failure fallback
- **WHEN** the Qwen API call fails or times out after 3 retries
- **THEN** the system SHALL fall back to saving the raw evidence package directly without compilation, and include a warning in the notification

### Requirement: LLM prompt follows wiki-research compilation rules
The system SHALL construct a prompt that instructs the LLM to follow the same compilation standards as the wiki-research SKILL.md.

#### Scenario: Prompt includes all compilation instructions
- **WHEN** constructing the LLM prompt
- **THEN** it SHALL include: evidence content, required output structure, citation rules (`[来源: URL]`), credibility levels (高/中/低), cross-source contradiction detection requirements, and source quality gate mapping rules

### Requirement: API integration uses阿里云百炼 endpoint
The system SHALL call the阿里云百炼 API for Qwen model inference.

#### Scenario: Successful API call
- **WHEN** the system POSTs to阿里云百炼 chat completion endpoint with model `qwen3.5-plus`
- **THEN** it SHALL receive a valid response containing the compiled report text

#### Scenario: API rate limit handling
- **WHEN** the API returns HTTP 429 (rate limit)
- **THEN** the system SHALL wait 5 seconds and retry up to 3 times before failing
