---
title: Data Privacy & Security Guide
tags: [gh-300, data-privacy, security, content-exclusions, duplication-detection, data-flow]
created: 2026-04-16
updated: 2026-04-16
type: deep-dive
---

> 📌 **Navigation:** [[INDEX|← Back to Index]] | [[exam-objectives|Exam Objectives]]

# Data Privacy & Security Guide

## Data Flow Overview

### How Your Code Moves Through Copilot

```
1. You type code in your IDE
   ↓
2. Context collected (surrounding code, file info)
   ↓
3. Prompt constructed with context
   ↓
4. Sent to GitHub/OpenAI APIs
   ↓
5. Model generates suggestions
   ↓
6. Post-processing (filter secrets, check duplication)
   ↓
7. Suggestions returned to you
   ↓
8. You accept/reject/modify
```

### Key Points About Data

**What gets sent:**
- Current file content
- Surrounding code context (above and below)
- File name and language
- Project structure metadata
- Your prompt/question

**What doesn't get sent:**
- Other open files (unless you reference them)
- Local environment variables
- Credentials (if duplication detection catches them)
- Files in `.copilotignore`

**What happens to it:**
- Depends on your subscription plan (see below)

---

## Data Handling by Subscription Plan

### Personal (Free/Pro Individual)

**Data Usage:**
- Code sent to GitHub/OpenAI for processing
- May be used to improve product
- May be used to train future models
- **User takes responsibility** for training data concerns

**Retention:**
- Kept for 90 days maximum
- Can request deletion
- Minimal logging

**Control:**
- Limited
- You can exclude files via `.copilotignore`
- Telemetry settings available

**Best for:** Individual developers, non-sensitive projects

### GitHub Copilot Business

**Data Usage:**
- Code explicitly **NOT** used for training
- NOT used to improve other organizations' models
- **GitHub contractual commitment** (legally binding)
- Used only for processing and suggestion

**Retention:**
- Shorter retention than free plan
- Security-focused handling
- Audit trails available

**Control:**
- Organization-wide policies can be set
- REST API for management
- Instruction files enforce standards
- Audit logs track usage

**Best for:** Companies concerned about IP protection, regulated industries

### GitHub Copilot Enterprise

**Data Usage:**
- Code **NOT** used for training
- **Strongest privacy guarantees**
- Enterprise SLA for compliance
- May support custom processing

**Retention:**
- Organization controls retention
- Can be customized per org policy
- Full audit trail

**Control:**
- Maximum control and customization
- Custom fine-tuning available
- Advanced security features
- Codebase indexing for better context

**Best for:** Large enterprises, regulated industries, stringent privacy needs

---

## Privacy & Security Features

### Content Exclusions - `.copilotignore`

**Purpose:** Prevent Copilot from seeing sensitive files

**File Locations:**
- Project root: `.copilotignore`
- Subdirectory: `.copilot/.copilotignore`

**Syntax:** Like `.gitignore`

**Typical Exclusions:**
```
# Environment & Credentials
.env
.env.local
.env.production
config/secrets.json
credentials.json

# Private Keys & Tokens
*.pem
*.key
private/

# Proprietary Code
src/proprietary/
algorithms/secret-algorithm.ts

# Customer Data
data/customers/
*.csv
user_data.json

# API Keys (if committed by accident)
**/api-keys.txt
**/tokens.json
```

**Important:**
- This is **preventive** (stops Copilot seeing files)
- Not a guarantee (never store secrets in code!)
- Still follow `.gitignore` for sensitive files

### Duplication Detection

**What it does:**
- Scans suggestions against public code
- Alerts when code matches training data
- Shows similarity percentage
- Gives you the choice to use it

**Why it matters:**
- License compliance (GPL, AGPL, etc.)
- Transparency about code origins
- Reduces legal risk

**How it works:**
1. Suggestion generated
2. Post-processing checks against public repos
3. Match found → Warning displayed
4. You decide: Accept, modify, or reject

**Important Caveat:**
- Duplication detection is NOT foolproof
- Responsibility is ultimately yours
- Always review generated code
- Understand license implications

### Security Warnings

**What Copilot watches for:**

| Issue | Example | Severity |
|-------|---------|----------|
| Hardcoded secrets | `password = "secret123"` | Critical |
| SQL injection | `"SELECT * FROM users WHERE id=" + id` | Critical |
| Weak crypto | `MD5.hash()` or `Math.random()` | High |
| XSS vulnerability | `innerHTML = userInput` | High |
| Insecure deserialization | Pickle, Java serialization | High |
| Missing auth check | No permission verification | Medium |
| Weak TLS | SSL v2, weak ciphers | Medium |

**Your responsibility:**
- Review warnings carefully
- Don't override warnings carelessly
- Test for security issues
- Never commit code with unresolved warnings

### Duplication Detection Filter

**How it filters:**
1. AI suggests code
2. Checks against known public sources
3. Matches found → Marked in suggestion
4. Low matches: Usually safe
5. High matches: Review carefully

**What counts as duplication:**
- Code from public GitHub repos
- Code from training data sources
- Common patterns (may have false positives)

**What's NOT flagged:**
- Common language idioms (everyone writes similar loops)
- Standard library usage
- Well-known algorithms

---

## Data & Architecture Understanding

### Code Suggestion Lifecycle (Detailed)

**Phase 1: Context Gathering**
1. IDE sends current file to Copilot extension
2. Extension gathers surrounding code (up to token limit)
3. File type and language identified
4. Project structure analyzed

**Phase 2: Prompt Construction**
1. System prompt + user context combined
2. Any custom instructions added (from `.github/copilot-instructions.md`)
3. Organization policies applied
4. Token limit checked (usually 8K-16K tokens)

**Phase 3: API Request**
1. Prompt sent to GitHub API
2. GitHub routes to language model (GPT-4 for Pro, custom for Enterprise)
3. Network-level filtering applied (if Enterprise)
4. Request logged per compliance rules

**Phase 4: Generation**
1. Language model generates suggestions
2. Usually produces 3-5 options
3. Ranked by quality/relevance
4. Beam search ensures best candidates

**Phase 5: Post-Processing**
1. Security scanning (secrets, vulnerabilities)
2. Duplication detection check
3. Filter based on organization policies
4. Exclusion rules applied (`.copilotignore`)
5. Remove potentially problematic suggestions

**Phase 6: Delivery**
1. Suggestions sent to IDE
2. Formatted for display
3. Rankings shown to user
4. User acceptance/rejection tracked

**Phase 7: Feedback**
1. User action recorded (accept/reject/modify)
2. Feedback stored (with consent)
3. Used to improve ranking, not training
4. Helps GitHub understand what works

### Input Processing Details

**How context is built:**
- Current line + ~10 lines before and after
- Function/class definition if inside function
- Imports and dependencies
- File name and extension
- Comment context
- Recent edits in file

**Prompt building steps:**
1. System instructions (e.g., "You are a helpful code assistant")
2. Relevant files/patterns mentioned via `@` in chat
3. User's actual request/question
4. Context from surrounding code
5. Organization instructions (Business+ plans)

**Context optimization:**
- Limited by token count
- Priority: Most recent code, imports, function signature
- Deprioritized: Comments way above, unrelated code
- User can influence by opening relevant files

### Limitations of LLMs (Language Models)

**Knowledge Cutoff**
- Model trained until specific date
- Doesn't know about new frameworks/libraries after that
- Version-specific knowledge may be outdated
- Real-time data (stock prices, current time) not available

**Context Window Limits**
- Can't process infinitely large files
- Very large projects may lose context
- Need to refocus chat for long conversations
- Token counting affects what gets included

**Reasoning Limitations**
- Can't do complex mathematical proofs
- May struggle with very abstract problems
- Logic chains sometimes break down
- Better with concrete examples than abstractions

**Hallucinations**
- May confidently generate wrong code
- Can invent function names that don't exist
- May forget parts of provided context
- Can confuse similar concepts

**Language/Style Issues**
- May not match your code style perfectly
- Idioms sometimes wrong or outdated
- Language-specific nuances missed
- Indentation/formatting sometimes off

---

## Privacy Configuration

### IDE Settings for Privacy

**VS Code:**
- Settings → Copilot → disable "Copilot: Inline Suggest"
- Settings → Copilot → disable telemetry
- Settings → Copilot → limit request to specific files

**JetBrains:**
- Settings → Tools → GitHub Copilot → disable inline suggestions
- Preferences → Tools → Copilot → telemetry options

**Visual Studio:**
- Tools → Options → GitHub Copilot → disable inline suggestions

### Organization-Level Privacy Controls (Business+)

**Policies you can set:**
- Which features are enabled organization-wide
- IDE support (vs. GitHub.com only)
- Preview features (on by default or off)
- Code review requirements
- Instruction file enforcement
- Audit frequency and depth

**Data retention policies:**
- How long to keep logs
- When to purge suggestion data
- Audit trail requirements
- Backup retention

---

## When to Exclude Content

### Definitely Exclude

✅ **API Keys and Credentials**
- Database passwords
- OAuth tokens
- AWS keys
- Third-party API credentials

✅ **Personally Identifiable Information (PII)**
- Customer names, emails, phone numbers
- Social security numbers
- Credit card numbers
- Addresses

✅ **Proprietary Algorithms**
- Core business logic you want protected
- Unique competitive advantages
- Trade secrets

✅ **Sensitive Customer Data**
- Full customer records
- Financial data
- Health information
- Security test results

### Consider Excluding

⚠️ **Specific Business Logic**
- If it's highly proprietary
- If it's a core differentiator
- If competitors shouldn't see patterns

⚠️ **Architecture Decisions**
- Infrastructure details
- Security topology
- System design (if truly secret)

### Usually OK to Include

✅ **Standard Libraries & Frameworks**
- React, Django, Spring code
- Standard design patterns
- Common algorithms

✅ **Public Code Standards**
- Linting rules
- Code style preferences
- Open source dependencies

✅ **General Business Logic**
- Most application code
- Data processing logic
- User-facing features

---

## Exam Tips for Data & Privacy

**Questions about data flow:**
- Understand the journey from IDE to API to model to response
- Know what gets filtered at each stage
- Understand post-processing

**Questions about duplication:**
- Duplication detection is for transparency/compliance
- It's checked POST-generation, not preventing the suggestion
- Responsibility is still yours

**Questions about exclusions:**
- `.copilotignore` is the tool to exclude files
- Format similar to `.gitignore`
- Prevents Copilot from reading files

**Questions about plan types:**
- Free plan: Data may be used for training
- Business: Code NOT used for training (contractual)
- Enterprise: Maximum privacy + custom features

**Questions about security:**
- Copilot can detect common vulnerabilities
- Warnings are alerts, not blockers
- You're responsible for final code security

**Questions about responsibility:**
- Copilot is a tool, not a replacement for code review
- You own the code and its implications
- Validation is your responsibility
- Copyright/license checking is your responsibility
