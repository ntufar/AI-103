---
title: File Exclusions & Content Guardrails for Copilot
tags: [gh-300, exclusions, .copilotignore, content-filtering, security, sensitive-files, guardrails]
created: 2026-04-17
updated: 2026-04-17
type: guide
---

> 📌 **Navigation:** [[INDEX|← Back to Index]]

# File Exclusions & Content Guardrails for Copilot

**EXAM CRITICAL:** The exam had many questions about `.copilotignore`, `.gitignore`, exclusion patterns, and how to configure what Copilot can see.

---

## Overview: Two Types of Exclusions

```
1. Individual User Level
   └── .copilotignore file in your repo
       (patterns like .gitignore)
       Prevents Copilot from seeing certain files locally

2. Organization/Enterprise Level (Business/Enterprise only)
   └── Content Exclusion Policies
       Enforced across organization
       Prevents Copilot from seeing files workspace-wide
```

---

## `.copilotignore` File (User/Repository Level)

### File Name & Location

**Correct:** `.copilotignore` ✅
**Incorrect:** `.copilot-ignore` ❌
**Incorrect:** `copilot.ignore` ❌ (The exam has questions testing this!)

**Where to place:**
```
your-repo/
├── .copilotignore          (root directory)
├── .copilot/
│   └── .copilotignore      (alternative location)
└── src/
```

**Precedence:** Root `.copilotignore` takes priority if both exist.

### Format & Syntax

**Syntax:** Same as `.gitignore` - uses glob patterns

```
# Exclude environment files
.env
.env.local
.env.*.local

# Exclude private keys
*.pem
*.key
*.p12
*.p8

# Exclude credential files
aws_secrets.txt
config/credentials.json
secrets/

# Exclude data directories
data/customers/
data/pii/
data/health_records/

# Exclude compiled/generated files (often safe)
dist/
build/
node_modules/

# Exclude test data
tests/fixtures/
tests/data/

# Exclude vendor/third-party (usually safe)
vendor/

# Exclude documentation that might leak info
docs/architecture-internal.md
docs/security-vulnerabilities.txt
```

### Pattern Examples

```
Pattern                     | Matches
============================|========================================
*.key                       | api.key, private.key, all.key files
config/secrets.json         | Exactly this file path
data/*/                     | All subdirs in data/ (data/customers/, etc.)
**/*.env                    | .env files at any nesting level
src/**/config.js            | config.js anywhere under src/
!important.pem              | Negate: DON'T exclude this file
```

### Important Exam Points

**Q:** "Can `.gitignore` be used instead of `.copilotignore`?"
**A:** No. `.gitignore` controls git, `.copilotignore` controls Copilot. They're independent.

**Q:** "Will Copilot ignore files in `.gitignore`?"
**A:** No. Copilot reads all committed files unless explicitly blocked by `.copilotignore`.

**Q:** "Where is the file configured?"
**A:** In the root of your repository (or `.copilot/` subdirectory).

**Q:** "Who can create/edit it?"
**A:** Any repository contributor with push access can create it in a PR. It's a regular repo file.

### How Copilot Respects `.copilotignore`

**In IDE:**
```
When you type in IDE:
1. Copilot scans open files and context
2. Checks if file matches .copilotignore pattern
3. If matched → excludes from analysis
   → Won't use for context
   → Won't show suggestions
4. If not matched → includes in context
```

**How to verify file is excluded:**

In VS Code:
```
Copilot Chat → Settings
  └── Should show .copilotignore is being respected
      (some versions show "X files excluded")
```

Or look for: "Copilot has excluded files matching .copilotignore"

---

## Enterprise-Level Content Exclusions (Business/Enterprise)

### Where to Configure

```
Organization Settings → Copilot → Policies
  └── Content Exclusion Settings (if available)
      └── Configure patterns organization-wide
```

Or:

```
Enterprise Settings → Copilot → Policies
  └── Org-specific content exclusions
      └── Apply to all organizations
```

**Note:** Feature availability depends on Copilot plan and settings.

### What Can Be Excluded at Enterprise Level

```
Exclusion Options:
├── File patterns (similar to .copilotignore)
├── Directory patterns
├── Repository names
├── Team-specific exclusions
└── Sensitive data types (PII, keys, secrets)
```

### Important: Local vs. Enterprise Exclusions

| Aspect | `.copilotignore` (Local) | Enterprise Policy (Org) |
|--------|--------|---------|
| **Who sets it** | Repository contributor | Org/Enterprise admin |
| **Scope** | This repo only | Entire org/enterprise |
| **Can be bypassed** | Yes (if repo owner changes it) | Harder (enforced centrally) |
| **Format** | Glob patterns | Admin UI or policy file |
| **Applies to** | All Copilot users in repo | All users in org |

---

## Guardrails & Content Filtering

### Copilot Enterprise Guardrails

**Available in:** Copilot Enterprise only

**What they do:**
1. **Pattern Matching** - Detect and block sensitive data types
   - Credit card numbers
   - Social Security numbers
   - API keys/tokens
   - Database passwords
   - PII (names, addresses, emails)

2. **Behavioral Control** - Control what Copilot can do
   - Limit access to specific repositories
   - Prevent agent execution in sensitive repos
   - Control model behavior

3. **Custom Guardrails** - Define your own rules
   - Block specific patterns
   - Enforce company policies
   - Prevent certain code patterns

### How to Know Files Are Excluded

### In IDE:

When a file is matched against `.copilotignore`:

**User sees:**
```
❌ File excluded by .copilotignore
   This file won't be used for Copilot suggestions
```

Or in chat:
```
"I can't analyze that file as it's excluded by your .copilotignore configuration"
```

### In Web (GitHub.com):

```
If you mention @-reference an excluded file:
  → Copilot shows warning
  → Asks to confirm
  → May still reference if you override
```

### Via API:

Using GitHub API to check file exclusions:
```bash
GET /repos/{owner}/{repo}/copilot/excluded-files
```

Returns list of files/patterns currently excluded.

---

## Common Scenarios from Exam

### Scenario 1: "We want to prevent Copilot from seeing customer data"

**Solution:**
```
1. Create .copilotignore in repo root
2. Add patterns:
   data/customers/
   data/pii/
   *.customer-data
3. Commit and push
4. Copilot now excludes these automatically
```

**Verification:**
- Check `.copilotignore` is in repo
- Copilot shows warning when trying to reference excluded files

### Scenario 2: "How do we enforce exclusions across all teams?"

**Solution (Enterprise):**
```
1. Enterprise Settings → Copilot → Policies
2. Content Exclusion Settings
3. Set organization-wide patterns:
   - **/*secrets*
   - **/*key*
   - database/backups/
4. Policy applies to all orgs/users
```

### Scenario 3: "A file was committed with API keys. How do we protect it?"

**Solution:**
```
Short term:
1. Add filename to .copilotignore immediately
   api-keys.json
2. Copilot won't use it going forward
3. But file is still in history!

Long term:
1. Rotate API keys (they're compromised)
2. Use git-filter-branch to remove from history
3. Or disable Copilot access to old branches
```

### Scenario 4: "How does user know if a file is excluded?"

**Solution:**
```
User tries to reference excluded file in chat:
  @file:excluded-file.ts
  ↓
Copilot shows: "File is excluded by .copilotignore"
  ↓
User can override: "include anyway?"
  ↓
File gets included (risky - it's excluded for a reason)
```

### Scenario 5: "Repository has many sensitive files. How to approach this?"

**Solution:**
```
Strategy:
1. Start restrictive: exclude more than necessary
   - /src/secrets/
   - /config/prod/
   - /data/
   
2. Monitor impact on developer productivity
3. Gradually add exceptions for safe content
   - /tests/ (usually safe)
   - /docs/ (usually safe)
   
4. Review quarterly
5. Audit logs show which files Copilot accessed
```

---

## Best Practices for File Exclusions

### 1. Start Broad, Refine Later
```
First: Exclude /data/ /config/ /secrets/
Then: Add exceptions for /data/public/
Eventually: Fine-tune to specific patterns
```

### 2. Document Your Exclusions
```
In repo README or SECURITY.md:
"Our .copilotignore excludes customer data to protect privacy.
See .copilotignore for current patterns."
```

### 3. Use Both Local & Enterprise Exclusions
```
Local (.copilotignore):
  - Project-specific secrets
  - Internal architecture docs
  - Customer data

Enterprise (Policy):
  - Company-wide secrets (AWS keys, databases)
  - Compliance-related files
  - Sensitive IP
```

### 4. Review Exclusions During Code Review
```
When PR includes changes to .copilotignore:
1. Verify patterns are correct
2. Check they don't exclude too much
3. Comment on intent
4. Ensure compliance with security policy
```

### 5. Maintain Audit Trail
```
Enterprise:
1. Log all policy changes in audit logs
2. Archive exclusion policy versions
3. Review annually for necessity
```

---

## Troubleshooting Exclusions

### Issue: "Copilot still sees my excluded files"

**Checks:**
1. Verify `.copilotignore` filename is correct (not `.copilot-ignore`)
2. Verify it's in repo root (not in subdirectory)
3. Did you commit the file? (uncommitted files don't take effect)
4. Did you refresh IDE? (restart IDE or reload folder)
5. Check syntax with glob pattern validator

### Issue: "Exclusion pattern not matching files"

**Debug:**
```
Test pattern in online glob matcher:
gitignore-glob.vercel.app

Pattern: data/*/
  Does it match: data/customers/   ✅ Yes
  Does it match: data/customers/user.json   ❌ No
  
Pattern: data/**/*
  Does it match: data/customers/user.json   ✅ Yes
  Does it match: data/a/b/c/d/file.txt      ✅ Yes
```

### Issue: "Excluded files appearing in chat history"

**Cause:** User manually added them with @file reference
**Solution:** Educate team that even if file is excluded, it's risky to override

### Issue: "Can't create .copilotignore in certain folder"

**Check:**
- Do you have write permissions to repo?
- Is the repo accepting commits?
- Is the path correct (root of repo)?

---

## Related Topics

- [[enterprise-management]] - Configuring policies at organization level
- [[audit-logs-guide]] - Tracking who accessed what (compliance)
- [[prompt-engineering-guide]] - Safe prompt patterns for sensitive data

---

**Last Updated:** April 17, 2026  
**Status:** Complete - Exam Ready

**Key Takeaway for Exam:**
- `.copilotignore` (not `.copilot-ignore`) blocks files locally
- Format matches `.gitignore` syntax
- Enterprise policies enforce org-wide
- Verify excluded files show warnings in IDE
- Use both for defense in depth
