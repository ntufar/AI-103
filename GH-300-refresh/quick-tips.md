---
title: GH-300 Exam - Quick Tips & Cheat Sheet
tags: [gh-300, quick-reference, exam-tips, high-yield, last-minute, cheat-sheet, enterprise, management]
created: 2026-04-16
updated: 2026-04-17
type: quick-reference
---

> 📌 **Navigation:** [[INDEX|← Back to Index]]

# GH-300 Exam - Quick Tips & Cheat Sheet

**READ THIS FIRST** - These are the most testable, high-value concepts.

---

## Top 5 Things to Know

### 1. Plan vs. Free - Feature Differences
**Critical for exam:** Many questions test what's available in each plan

| Feature | Free | Pro | Business | Enterprise |
|---------|------|-----|----------|-----------|
| Inline Suggestions | ✅ | ✅ | ✅ | ✅ |
| Chat (IDE & Web) | ✅ | ✅ | ✅ | ✅ |
| CLI | ✅ | ✅ | ✅ | ✅ |
| Plan Mode | ❌ | ✅ | ✅ | ✅ |
| Edit Mode | ❌ | ✅ | ✅ | ✅ |
| Agent Mode | ❌ | ✅ | ✅ | ✅ |
| Code Review Policies | ❌ | ❌ | ✅ | ✅ |
| Org Management | ❌ | ❌ | ✅ | ✅ |
| Audit Logs | ❌ | ❌ | ✅ | ✅ |
| No Training on Your Code | ❌ | ❌ | ✅ | ✅ |

### 2. `.copilotignore` - How to Exclude Files
**Critical for exam:** This is simple but heavily tested

```
# Location: Root of project or .copilot/ directory
# Format: Like .gitignore

# Always exclude:
.env
*.pem
*.key
config/secrets.json

# Also exclude sensitive:
data/customers/
**/api-keys.txt
```

**What it does:** Prevents Copilot from READING those files
**What it doesn't do:** Doesn't prevent accidental commits

### 3. Data Handling by Plan
**Critical for exam:** Privacy/compliance questions always test this

- **Free/Pro:** Code may be used for training ⚠️
- **Business:** Code contractually NOT used for training ✅
- **Enterprise:** Maximum privacy + customization ✅✅

### 4. Duplication Detection
**Critical for exam:** Questions test when/how it's used

**What:** Post-processing checks suggestions against public code
**Purpose:** License compliance & transparency
**Action:** Shows warning, you choose to accept or not
**Reality:** Detection is NOT foolproof - your responsibility

### 5. Prompt Engineering Core Principle
**Critical for exam:** Questions ask what makes prompts effective

**Good prompts have:**
- ✅ Specific goal (not vague)
- ✅ Relevant context (framework, language)
- ✅ Clear constraints (what to do/not do)
- ✅ Example of desired output
- ✅ Progressive if complex (break into steps)

---

## Exam Question Patterns (Likely to See)

### Pattern 1: "Which feature for this scenario?"
**Approach:**
1. Read the scenario carefully
2. Identify the goal (refactor? generate? plan?)
3. Match to feature
4. Check if plan supports it

**Common Scenarios:**
- "Developer wants to plan complex feature" → Plan Mode
- "Team wants code review standards" → Code Review Policies
- "Need to exclude API keys" → .copilotignore
- "Speed up shell commands" → GitHub Copilot CLI

### Pattern 2: "What's the responsible approach?"
**Answer format:**
- Includes validation
- Mentions code review
- Considers security
- Documents AI use
- Tests thoroughly

### Pattern 3: "What data gets sent?"
**Safe answer:** Current file + surrounding context
**What's NOT sent:** Other open files, credentials, excluded files

### Pattern 4: "Which prompt is better?"
**Better prompts:** More specific, include examples, clearer constraints

### Pattern 5: "Organization policy question"
**Key facts:**
- Business+ plan required
- Set via organization settings
- Enforced via instruction files
- Tracked in audit logs

---

## Common Wrong Answers to Avoid

❌ "Copilot will train on Business plan code"
- ✅ Correct: Business plan contractually prevents training

❌ "Use duplication detection to prevent duplication"
- ✅ Correct: Detection is post-generation, it warns you

❌ "Agent Mode does small targeted edits"
- ✅ Correct: Edit Mode does targeted edits, Agent creates files

❌ "Copilot knows about events happening now"
- ✅ Correct: Copilot has knowledge cutoff, can't access real-time

❌ ".gitignore excludes files from Copilot"
- ✅ Correct: .copilotignore does that, .gitignore doesn't affect Copilot

❌ "Copilot is responsible for code quality"
- ✅ Correct: You are responsible, Copilot is a tool

❌ "CLI and IDE Chat are identical"
- ✅ Correct: Different interfaces with slightly different commands

---

## 10-Minute Cram Session

**Read these in order (5 min each):**

1. **What Copilot does:**
   - Provides code suggestions using AI
   - Available in IDE (inline, chat), CLI, web
   - Requires validation before use
   - You are responsible for output

2. **Features by plan:**
   - Free: Basic suggestions + chat
   - Pro: + Plan Mode, Edit Mode, Agent Mode
   - Business: + Org policies, audit logs, no training
   - Enterprise: + Custom features

3. **Responsible use means:**
   - Validate all suggestions (test them)
   - Review for security
   - Understand copyright implications
   - Use duplication detection
   - Document AI assistance

4. **Privacy basics:**
   - .copilotignore excludes files
   - Duplication detection flags matches
   - Business plan doesn't train on your code
   - You own the generated code

5. **Prompt engineering:**
   - Be specific, not vague
   - Include context
   - Show examples
   - Define constraints
   - Use Chat for complex requests

---

## NEW: Enterprise & Organization Management (April 17 Update)

**EXAM UPDATE:** GH-300 heavily tests enterprise features - know these!

### Quick Facts: Organization Licensing

| Concept | What to Know |
|---------|-------------|
| **Who controls license** | Enterprise Owner or Org Owner |
| **Audit logs retention** | 180 days (then deleted unless exported) |
| **Can disable Chat** | Yes - via org policies (affects all users) |
| **Can exclude files** | Yes - `.copilotignore` (repo) + policy (org) |
| **Agent mode usage** | Can limit to specific repos |

### Slash Commands You Must Know

| Command | What It Does | Exam Q Pattern |
|---------|------------|----------------|
| `/test` | Generate unit tests | "What generates tests?" → `/test` |
| `/help` | Get Copilot help | "Learn about Copilot features" |
| `/new` | Start conversation | "Clear context for new topic" |
| `/fix` | Fix code | "Improve buggy code" |
| `/review` | Review code | "Security/quality audit" |

**Remember:** Type `/` in chat to see all available commands (varies by IDE)

### Content Exclusions (2 Types)

```
Type 1: Local .copilotignore
  └── Repo root (not .copilot-ignore or copilot.ignore)
  └── Like .gitignore format
  └── Prevents Copilot seeing those files

Type 2: Enterprise Policy
  └── Admin sets at org/enterprise level
  └── Enforced for all teams
  └── Overrides repo settings
```

**Exam question type:** "How to prevent Copilot from seeing secrets?"
**Answer:** Add to .copilotignore OR enable enterprise content exclusion policy

### Audit Logs Quick Reference

```
What's tracked:
  ✅ License assignments/removals
  ✅ Policy changes
  ✅ Custom agent lifecycle
  ✅ Who did it + when

What's NOT tracked:
  ❌ Individual prompts (privacy)
  ❌ Code suggestions
  ❌ Chat messages

Retention: 180 days (then deleted)
  → Need long-term? Stream to external system
```

### Copilot Business vs. Enterprise

| Feature | Business | Enterprise |
|---------|----------|-----------|
| License management | ✅ | ✅ |
| Audit logs | ✅ | ✅ |
| Org-level policies | ✅ | ✅ |
| Custom agents | ❌ | ✅ |
| Content exclusion policy | Limited | Full |
| Model customization | ❌ | ✅ |
| Full feature control | Limited | ✅ |

**Exam tip:** "Enterprise features" questions = Copilot Enterprise only

---

## Links to Full Guides (New Apr 17)

**For detailed coverage, read these guides:**

- [[enterprise-management]] - Organizations, licensing, policies, agents
- [[audit-logs-guide]] - What logs contain, retention, compliance
- [[file-exclusions-guide]] - .copilotignore, patterns, guardrails  
- [[api-insights-guide]] - Metrics, usage data, compliance reporting
- [[chat-commands-guide]] - All slash commands, modes, usage

---

**Scan these keywords:**

- **Plan Mode** = Planning complex features (Pro+)
- **Edit Mode** = Targeted edits to code (Pro+)
- **Agent Mode** = Auto-modify multiple files (Pro+)
- **Duplication Detection** = Post-processing check for license issues
- **.copilotignore** = Exclude files from Copilot
- **Instruction Files** = .github/copilot-instructions.md + .github/instructions/*.instructions.md
- **Business Plan** = Contractual no-training + audit logs
- **CLI** = Terminal: `copilot`, `/login`, and `copilot -p`
- **Code Review** = Copilot reviews PRs (Business+)
- **Responsible AI** = Validate, test, review, document

---

## Exam Day Strategies

### Before You Start
- [ ] Deep breath - you've got this
- [ ] Review the question format (this practice test helps: https://ghcertdemo.starttest.com/)
- [ ] Understand scoring (~1 min per question paces you well)
- [ ] Plan to review at end if time permits

### During the Exam
- **Read questions carefully** - Watch for "NOT" and "EXCEPT"
- **Watch for absolutes** - "Always", "Never" are rarely right answers
- **Focus on practical** - Exam tests real-world use, not trivia
- **When unsure:**
  1. Eliminate obviously wrong answers
  2. Choose the most responsible/safe answer
  3. Flag for review if you have time
- **Don't second-guess** - First instinct is usually right

### Answer Strategies by Question Type

**"Choose the best approach"**
- Best answer includes: validation, testing, documentation
- Safe answer: human-in-the-loop, not fully automated

**"What does this feature do?"**
- Match feature to capability
- Remember plan limitations
- Test understanding of "why" not just "what"

**"Which prompt is better?"**
- Better = more specific, includes examples, clear constraints
- Better = includes relevant context

**"What's a risk of..."**
- Risks include: security issues, license problems, hallucinations
- Mitigation = validation, review, testing

**"How to solve this problem?"**
- Solution should include: steps, validation, responsible approach
- Responsible = human review, testing, documentation

---

## Key Terms (Quick Definitions)

- **Inline Suggestions** - Auto-complete while typing
- **Chat Panel** - Interactive Q&A in IDE
- **Plan Mode** - Break down complex features into steps
- **Edit Mode** - Targeted edits instead of full rewrite
- **Agent Mode** - Copilot can modify files autonomously
- **Spark** - Generate code from descriptions
- **Spaces** - Organize repos for project context
- **MCP** - Connect external tools to Copilot
- **Duplication Detection** - Flag code matching training data
- **Hallucination** - AI confidently generating wrong code
- **Zero-shot** - No examples provided
- **Few-shot** - Examples provided to guide suggestions
- **Token** - Unit of text (usually ~4 characters)
- **Context Window** - Amount of code Copilot can consider
- **Knowledge Cutoff** - Training data stops at this date

---

## If You Get Stuck

**Strategy when unsure:**
1. **Read carefully again** - You might have missed something
2. **Eliminate obviously wrong** - Remove 1-2 options
3. **Choose most responsible** - Safe answer usually right
4. **If timed pressure** - Move on, flag to review later
5. **Trust your study** - You know this material

**Don't:**
- ❌ Overthink obvious questions
- ❌ Change correct answers
- ❌ Get stuck on one question
- ❌ Panic if unsure

---

## Confidence Check

**Before exam, make sure you can:**
- ✅ Explain what Copilot does and doesn't do
- ✅ List features by plan type
- ✅ Describe data handling by plan
- ✅ Explain responsible AI use
- ✅ Write an effective prompt
- ✅ Identify security risks
- ✅ Use `.copilotignore`
- ✅ Understand duplication detection
- ✅ Know CLI basic commands
- ✅ Explain org-wide policies

**If you're weak on any, quickly review that section.**

---

## Final Reminders

1. **Read questions slowly** - No rush, you have time
2. **You've studied this** - Trust your preparation
3. **Responsible answers are correct** - Safe > risky
4. **Practical > theoretical** - Real-world application matters
5. **Validate suggestions = main theme** - Keep asking "is this correct?"

---

**Good luck! You've got this! 🎯**

Remember: The exam tests practical knowledge of Copilot, not memorization. 
If you understand the concepts, you'll do well.
