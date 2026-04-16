---
title: GitHub Copilot Features - Quick Reference Checklist
tags: [gh-300, copilot-features, ide-features, cli, organization-features, plan-comparison]
created: 2026-04-16
updated: 2026-04-16
type: reference
---

> 📌 **Navigation:** [[INDEX|← Back to Index]] | [[exam-objectives|Exam Objectives]]

# GitHub Copilot Features - Quick Reference Checklist

Use this as a quick reminder of features, where they're available, and what they do.

---

## IDE Features (VS Code, Visual Studio, JetBrains IDEs)

### Inline Suggestions
- **What:** Real-time code suggestions as you type
- **How to Trigger:** Start typing code, suggestions appear automatically
- **Accept:** Tab or Enter
- **Reject:** Escape or keep typing
- **Navigate:** Alt/Cmd + [ or ] for previous/next suggestions
- **Availability:** All Copilot plans
- **Best For:** Quick completions, boilerplate code, methods

### Copilot Chat Panel
- **What:** Interactive conversation with Copilot in sidebar/pane
- **How to Trigger:** Ctrl+L (Windows) or Cmd+L (Mac)
- **Features:**
  - Reference files with `@filename`
  - Use slash commands: `/explain`, `/fix`, `/tests`, `/refactor`, `/doc`
  - Multiple turns in conversation thread
  - Custom instructions via `.github/copilot-instructions.md`
- **Availability:** All Copilot plans
- **Best For:** Complex requests, multi-step tasks, explanations

### Plan Mode
- **What:** Plan code structure before implementation
- **How to Trigger:** Ask in Chat panel or start with planning prompt
- **What it does:** Breaks down implementation into steps
- **Availability:** Copilot Pro and higher
- **Best For:** Large features, architecture planning, learning

### Edit Mode
- **What:** Targeted edits to code instead of full rewrites
- **How to Trigger:** Ask for refactoring, changing specific sections
- **What it does:** Suggests changes to selected code block
- **Availability:** Copilot Pro and higher
- **Best For:** Refactoring, adding features to existing code, large files

### Agent Mode (Preview)
- **What:** Copilot can make autonomous changes to files
- **How to Trigger:** Enable in settings or ask Chat
- **What it does:** Creates multiple files, makes complex changes automatically
- **Safety:** You review before accepting
- **Availability:** Copilot Pro and higher (preview)
- **Best For:** Project scaffolding, architectural refactoring

### MCP (Model Context Protocol)
- **What:** Connect Copilot to external tools and data sources
- **Extends:** Chat capabilities with custom tools
- **How it works:** 3rd party integrations send context to Copilot
- **Availability:** Beta/Preview
- **Best For:** Accessing real-time data, custom knowledge bases

### Code Review in IDE
- **What:** Copilot reviews your code for issues
- **How to Trigger:** Right-click on file → Review Code
- **What it checks:** Security, performance, style, logic errors
- **Availability:** Organization-wide feature (requires subscription)
- **Best For:** Quality assurance before merging

---

## GitHub.com Features

### Copilot Chat on GitHub.com
- **Where:** In pull requests, issues, code discussions
- **What it does:** Answer questions about code, explain changes
- **Trigger:** Type @ to mention Copilot in discussions
- **Availability:** Copilot Pro and higher

### Spaces (Preview)
- **What:** Organize repositories and shared knowledge
- **Purpose:** Give Copilot project-wide context
- **Contains:** Repos, documentation, patterns, decisions
- **Benefit:** Copilot suggestions more aligned to team standards
- **Availability:** Preview feature

### Spark
- **What:** Generate code from natural language description
- **Where:** Use in Chat to create new functionality
- **Process:** Describe feature → Spark generates structure
- **Availability:** Preview/Copilot Pro
- **Best For:** Prototyping, scaffolding new features

### Pull Request Summaries
- **What:** Auto-generate PR description from code changes
- **How:** Click "Generate summary" button
- **Contains:** What changed, why it matters
- **Saves:** Time on documentation
- **Availability:** Copilot Pro and higher

### Pull Request Code Review
- **What:** Copilot reviews PRs automatically
- **Checks:** Security, performance, style, logic
- **Format:** Comments on specific lines
- **Customizable:** Via instruction files and policies
- **Availability:** Organization feature

---

## CLI Features (Command Line)

### GitHub Copilot CLI (`gh copilot`)
- **Installation:** `gh extension install github/gh-copilot`
- **Auth:** `gh copilot auth login`

#### Key Commands:

| Command | What it does | Example |
|---------|-------------|---------|
| `gh copilot explain` | Explains what a command does | `gh copilot explain "git rebase -i"` |
| `gh copilot suggest` | Get command suggestions | `gh copilot suggest` then describe what you want |
| `-t shell` flag | Specify shell suggestions | `gh copilot suggest -t shell` |
| Interactive mode | Multi-turn conversation | Start with `gh copilot suggest` and keep chatting |

**Benefits:**
- Don't need to search docs for command syntax
- Safer - understand command before running
- Reduces context switching
- Multi-turn conversation for complex tasks

**Best For:**
- Learning new commands
- Complex shell scripting
- Git operations
- DevOps/deployment tasks

---

## Organization-Level Features

### Organization Policy Management
- **Where:** Organization Settings → Copilot
- **Controls:**
  - Enable/disable for organization
  - Per-user licenses
  - IDE availability (which IDEs to support)
  - GitHub.com features (Spaces, Spark, PR reviews)
  - Preview features (on/off by default)

### Code Review Policies
- **Define:** Review standards organization-wide
- **Configure:** Via `instructions.md` files
- **Enforce:** Review requirements per repository
- **Track:** Via audit logs

### Instruction Files
- **Location 1:** `.github/copilot-instructions.md` (org-wide)
- **Location 2:** `.copilot/instructions.md` (repo-specific)
- **Contains:**
  - Naming conventions
  - Code style preferences
  - Security requirements
  - Performance guidelines
  - Architecture patterns
  - Linting/testing requirements

### Audit Logging
- **What:** Track Copilot feature usage
- **Tracks:** Who used what features, when
- **Purpose:** Compliance, usage analytics, governance
- **Access:** Organization owners/admins only
- **Availability:** GitHub Enterprise

### REST API for Management
- **Purpose:** Programmatic license management
- **Use cases:** Bulk user provisioning, usage reporting
- **Integrations:** Identity management systems, HR tools
- **Available endpoints:** License assignment, user management

---

## Content Exclusion & Privacy

### `.copilotignore` File
- **Location:** Project root or `.copilot/` directory
- **Format:** Similar to `.gitignore`
- **Purpose:** Prevent Copilot from seeing sensitive files
- **Excludes:**
  - Credentials and API keys
  - PII (personally identifiable info)
  - Proprietary algorithms
  - Sensitive customer data
  
**Example:**
```
# Credentials
*.env
.env.local
config/secrets.yml

# Proprietary code
src/proprietary/*
algorithms/secret-algo.js

# Data
*.csv
customer_data.json
```

### App Knowledge Exclusions
- **What:** Exclude organization-specific patterns Copilot shouldn't see
- **Purpose:** Privacy, preventing leakage of internal patterns
- **Level:** Organization-wide setting

### Privacy Settings
- **IDE Settings:** Configure what telemetry Copilot collects
- **Options:** Inline suggestions, chat history, usage data
- **Control:** Per-IDE settings

---

## Data & Security Features

### Duplication Detection
- **What:** Copilot checks if suggestion matches public training data
- **Alert:** Shows warning if potential duplication detected
- **Your Choice:** You can accept or reject
- **Purpose:** Avoid license compliance issues
- **Transparency:** You see what's flagged

### Security Warnings
- **Detects:**
  - Hardcoded secrets/credentials
  - SQL injection patterns
  - Weak cryptography
  - File permission issues
  - Common vulnerabilities
  
- **Format:** Warnings shown in suggestions
- **Action:** Up to you to fix or override

### Proxy Filtering (Enterprise)
- **For:** Organizations with network restrictions
- **Function:** Intercept/filter network requests
- **Use case:** Compliance, data residency, content filtering

### Data Handling
- **Personal Plan:** Code sent to GitHub, not used for training, 90-day retention
- **Business/Enterprise:** Code not used for training, shorter retention, more control
- **Key point:** Data handling depends on subscription level

---

## Features by Plan Type

### GitHub Copilot Individual
- ✅ Inline suggestions
- ✅ Chat in IDE and github.com
- ✅ CLI (suggest, explain)
- ✅ Code review (read-only)
- ✅ Basic customization
- ❌ Plan Mode
- ❌ Agent Mode
- ❌ Organization policies

### GitHub Copilot Pro
- ✅ Everything in Individual
- ✅ Plan Mode
- ✅ Edit Mode
- ✅ Agent Mode (preview)
- ✅ Spark
- ✅ Spaces
- ✅ PR summaries
- ✅ Better model access (GPT-4 equivalent)

### GitHub Copilot Business
- ✅ Everything in Pro
- ✅ Organization management
- ✅ Audit logs
- ✅ Code review policies
- ✅ Custom instructions enforcement
- ✅ REST API
- ✅ Enhanced support
- ✅ No code training clause

### GitHub Copilot Enterprise
- ✅ Everything in Business
- ✅ Codebase indexing
- ✅ Knowledge base integration
- ✅ Advanced security features
- ✅ Custom fine-tuning (roadmap)
- ✅ Priority support
- ✅ Enterprise SLA

---

## Quick Feature Decision Tree

**Question: What do I need Copilot to do?**

- **Code completion while typing?** → Inline Suggestions
- **Answer my questions about code?** → Chat Panel
- **Plan a complex feature?** → Plan Mode (Pro+)
- **Edit existing code targeted?** → Edit Mode (Pro+)
- **Build from scratch?** → Spark (Pro+) or Agent Mode (Pro+)
- **Review my code for issues?** → Code Review
- **Explain a shell command?** → CLI `gh copilot explain`
- **Get a command suggestion?** → CLI `gh copilot suggest`
- **Document my pull request?** → PR Summary (Pro+)
- **Enforce standards org-wide?** → Instructions + Policies (Business+)

---

## Common Mistakes on Exam

❌ **Confusing Agent Mode with Edit Mode**
- Agent Mode: Can create/modify multiple files autonomously
- Edit Mode: Targeted edits to code you select

❌ **Thinking Copilot Chat and IDE Chat are the same**
- They're different interfaces with similar capabilities
- GitHub.com Chat has fewer commands than IDE Chat

❌ **Forgetting about `.copilotignore`**
- Easy way to exclude sensitive files
- Exam will likely test this knowledge

❌ **Not knowing which features require Pro**
- Plan Mode, Edit Mode, Agent Mode need Pro+
- Be clear on feature availability

❌ **Mixing up data handling by plan**
- Free: Data may be used for training
- Business+: Code explicitly NOT used for training
- Check your subscription level in exam questions

---

## Exam Tips

- **For feature questions:** Remember the Plan vs Free distinction
- **For organization questions:** Policies, audits, instructions = Business+
- **For privacy questions:** `.copilotignore` and duplication detection
- **For productivity questions:** Think about which feature saves most time
- **For data questions:** Plan type determines data handling
