---
title: Copilot Chat Commands & Features - Slash Commands & Tools
tags: [gh-300, chat, slash-commands, /help, /test, copilot-chat, commands, agents, features]
created: 2026-04-17
updated: 2026-04-17
type: guide
---

> 📌 **Navigation:** [[INDEX|← Back to Index]]

# Copilot Chat Commands & Features

**EXAM CRITICAL:** The exam tests knowledge of Copilot Chat slash commands, especially `/help` and `/test` commands.

---

## Copilot Chat Overview

### Where Chat is Available

```
Copilot Chat available in:
├── IDE (VS Code, JetBrains, Visual Studio, etc.)
├── GitHub.com (Web)
├── GitHub Mobile
├── Windows Terminal (Canary/preview)
└── CLI (via GitHub CLI plugin)
```

### Plan Availability

| Feature | Free | Pro | Business | Enterprise |
|---------|------|-----|----------|-----------|
| Chat in IDE | ✅ | ✅ | ✅ | ✅ |
| Chat on GitHub.com | ✅ | ✅ | ✅ | ✅ |
| Chat in CLI | ✅ | ✅ | ✅ | ✅ |
| Plan Mode (planning) | ❌ | ✅ | ✅ | ✅ |
| Agent Mode (autonomous) | ❌ | ✅ | ✅ | ✅ |
| Custom Agents | ❌ | ❌ | ✅ | ✅ |
| Org-level control | ❌ | ❌ | ✅ | ✅ |

---

## Slash Commands in Copilot Chat

### What Are Slash Commands?

**Slash commands** are shortcuts to avoid typing complex prompts.

**Format:** Type `/` → see list of available commands → select one

**Examples:**
```
/new          Start a new conversation
/clear        Clear conversation history
/help         Get help about Copilot
/test         Generate test code
/explain      Explain selected code
/fix          Fix a bug in code
/review       Review code for issues
```

### Important Note on Availability

**Slash commands vary by:**
- IDE used (VS Code has different set than JetBrains)
- Chat interface (IDE vs. GitHub.com vs. CLI)
- Copilot version
- Custom agent configuration

**Exam Q:** "What slash command generates tests?"
**Answer:** `/test` (generates unit tests for selected code)

### Common Slash Commands

#### `/new`
- **Purpose:** Start a new chat conversation
- **Use case:** Clear context, start fresh topic
- **Available:** All environments
- **Example:**
  ```
  /new
  → New conversation thread starts
  ```

#### `/clear`
- **Purpose:** Clear chat history in current conversation
- **Use case:** Remove context to prevent hallucination
- **Available:** All environments
- **Example:**
  ```
  /clear
  → Conversation history cleared
  → Previous context lost
  ```

#### `/help`
- **Purpose:** Get help about Copilot features
- **Use case:** Learn what Copilot can do
- **Available:** Chat in IDE, GitHub.com
- **Example:**
  ```
  /help
  → Lists all available commands
  → Shows how to use Copilot
  → Links to documentation
  
  /help slash commands
  → Shows all slash commands
  
  /help agents
  → Shows how to use agent mode
  ```

#### `/test`
- **Purpose:** Generate unit tests for selected code
- **Use case:** Create test cases automatically
- **Available:** IDE chat environments
- **Uses code context:** Analyzes selected file/code
- **Example:**
  ```
  Select code in editor → /test
  → Copilot generates:
     - Unit test file
     - Test cases for functions
     - Mock data setup
  ```

**Exam Question Pattern:**
"What command generates tests?"
**Answer:** `/test` (or "Generate test code")

#### `/explain`
- **Purpose:** Explain selected code
- **Use case:** Understand complex functions
- **Available:** IDE chat
- **Example:**
  ```
  Select code → /explain
  → Copilot explains:
     - What the code does
     - How it works
     - Key concepts
  ```

#### `/fix`
- **Purpose:** Fix bugs or issues in code
- **Use case:** Debug or improve code
- **Available:** IDE chat
- **Example:**
  ```
  Select buggy code → /fix
  → Copilot:
     - Identifies issues
     - Suggests fixes
     - Explains changes
  ```

#### `/review`
- **Purpose:** Review code for quality, security, performance
- **Use case:** Code review automation
- **Available:** IDE chat, Business/Enterprise
- **Example:**
  ```
  Select code → /review
  → Copilot checks:
     - Security issues
     - Performance problems
     - Code style
     - Best practices
  ```

#### `/rename`
- **Purpose:** Rename a conversation
- **Use case:** Organize chat history
- **Available:** All chat environments
- **Example:**
  ```
  /rename "Auth refactoring"
  → Conversation title changes
  ```

#### `/delete`
- **Purpose:** Delete a conversation
- **Use case:** Remove old/obsolete chats
- **Available:** GitHub.com chat
- **Example:**
  ```
  /delete
  → Conversation removed
  → (Ask for confirmation first)
  ```

### How to See Available Commands

**In IDE:**
```
Copilot Chat panel
  ↓
Type "/" in chat box
  ↓
List appears with all available commands
  ↓
Select one, see description
```

**Available commands depend on:**
- Your plan (Free/Pro/Business/Enterprise)
- Your IDE
- Selected code (some commands need context)
- Admin policies (orgs may disable some)

---

## Context Keywords in Chat

### Using Mentions (@)

**Purpose:** Attach specific context to chat

```
@file:path/to/file.ts
  → Include specific file in context
  → Copilot analyzes this file

@workspace
  → Include entire workspace context
  → Copilot considers all files
  → Use carefully (can be slow)

@github
  → Use GitHub-specific skills
  → Search GitHub docs
  → Get GitHub API information
```

### Using Variables (#)

**Purpose:** Reference specific items

```
#selection
  → Current selected code in editor
  
#file
  → Current open file
  
#web
  → Web search capability
  
#codebase
  → All files in repo
```

### Combining Keywords

```
Example 1:
@workspace /test
  → Examine entire workspace
  → Generate comprehensive tests

Example 2:
@file:config.js #selection /fix
  → Focus on config.js
  → Get selected part
  → Fix issues

Example 3:
/review @codebase
  → Review all code
  → Comprehensive security check
```

---

## Chat Modes in IDE

### Ask Mode (Default)
```
Best for: Questions, explanations, understanding
What it does: Analyzes your question and code context
Prompt example: "Why is this function slow?"
```

### Plan Mode
```
Available: Pro, Business, Enterprise
Best for: Complex features, refactoring, planning
What it does: Creates detailed implementation plan
Prompt example: "Add authentication to our API"
  ↓
Copilot returns:
  - Step-by-step plan
  - Time estimates
  - Questions for clarification
  
Then: "Start Implementation" to begin
```

### Agent Mode
```
Available: Pro, Business, Enterprise
Best for: Autonomous task completion
What it does: Makes code changes, runs commands, self-corrects
Prompt example: "Refactor this to use async/await"
  ↓
Copilot:
  - Edits files
  - Runs tests
  - Fixes errors automatically
```

---

## Commands in CLI

### Copilot CLI Commands

```bash
# Ask question
gh copilot explain "select code in editor"

# Generate explanation
gh copilot explain

# Get help
gh copilot --help
```

### Available CLI Commands

```bash
gh copilot <COMMAND>

Commands:
  explain   - Explain code/commands
  suggest   - Suggest improvements
  help      - Get help on Copilot
```

---

## MCP Skills in Chat

### What Are MCP Skills?

**MCP = Model Context Protocol**

Copilot can use specialized tools/skills for common operations:

```
Available Skills:
├── create_branch
│   Usage: "Create a new branch for authentication feature"
│
├── create_or_update_file
│   Usage: "Add a new file with hello world content"
│
├── update_pull_request_branch
│   Usage: "Sync my PR with main branch"
│
├── merge_pull_request
│   Usage: "Merge PR #123"
│
├── get_me
│   Usage: "Tell me about myself"
│
├── search_users
│   Usage: "Find all users named John"
│
└── Other GitHub operations
```

### How to Use Skills

```
In Chat:
"Using GitHub skills, create a new branch called feature/auth"
  ↓
Copilot recognizes the intent
  ↓
Uses skill to create branch
  ↓
Returns result
```

---

## Limitations & Restrictions

### What Chat CAN'T Do

```
❌ Access your IDE file system
   (except files you explicitly mention)

❌ Execute arbitrary commands
   (only specific GitHub operations)

❌ Access external APIs
   (unless explicitly configured)

❌ Modify private GitHub data
   (can't change secrets, etc.)

❌ See audit logs
   (only org admins see these)
```

### Org-Level Restrictions

**If your org disables Chat:**
```
Org Settings → Copilot → Policies
  └── Copilot in IDE → Disabled

Result:
  ❌ Chat is unavailable in IDE
  ❌ Users can't access chat
  ❌ Can still use code suggestions
```

---

## Common Exam Scenarios

### Scenario 1: "What command generates test code?"
**Answer:** `/test`

### Scenario 2: "User can't find slash commands. Why?"
**Possible causes:**
```
1. Chat is disabled by org admin
   → Check org policies
   
2. Using unsupported IDE
   → Some IDEs have limited commands
   
3. Copilot extension not installed
   → Install/enable extension
   
4. Free plan user
   → Some commands only in Pro+
   
5. Chat not open
   → Open Copilot Chat panel first
```

### Scenario 3: "How do we generate tests for our codebase?"
**Solution:**
```
1. Select function in editor
2. Open Copilot Chat
3. Type: /test
4. Copilot generates test file
5. Review and customize tests
6. Commit to repo
```

### Scenario 4: "/help shows no output. What's wrong?"
**Possible issues:**
```
1. Copilot connection lost
   → Sign in again
   
2. Chat disabled by org
   → Contact org admin
   
3. Using unsupported interface
   → Use IDE or GitHub.com
   
4. Command not recognized
   → Check spelling: /help (not /Help or /HELP)
```

### Scenario 5: "We want to learn more about Copilot capabilities"
**Solution:**
```
1. In Copilot Chat
2. Type: /help
3. Shows all available commands
4. Type: /help agents
5. Learn about agent capabilities
6. Type: /help [specific command]
7. Get detailed help on that command
```

---

## Best Practices

### 1. Clear Context Before Starting
```
Bad:   Start new chat, ask questions
Good:  /new → Set up context → Ask questions
```

### 2. Use Right Mode for Task
```
Simple questions        → Ask mode (/help, /test)
Complex projects       → Plan mode (/plan)
Hands-on implementation → Agent mode
```

### 3. Use Commands Instead of Prompts
```
Instead of:
  "Can you write tests for this function?"
  
Use:
  /test
```

### 4. Keep Context Focused
```
Don't:  /test @workspace
        (tests entire codebase)

Do:     Select function → /test
        (test one function)
```

### 5. Review Generated Code
```
Always:
  - Review suggestions
  - Verify correctness
  - Check for security issues
  - Understand the logic
```

---

## Related Topics

- [[enterprise-management]] - Controlling chat availability via policies
- [[prompt-engineering-guide]] - Writing better prompts for chat
- [[responsible-ai-notes]] - Ethical use of generated code

---

**Last Updated:** April 17, 2026  
**Status:** Complete - Exam Ready

**Key Takeaway for Exam:**
- Slash commands streamline common tasks
- `/help` gets information about Copilot
- `/test` generates unit tests
- `/new` starts fresh conversation
- Availability depends on plan and org policies
- Commands vary by IDE/interface
