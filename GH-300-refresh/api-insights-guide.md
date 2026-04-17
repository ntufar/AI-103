---
title: GitHub Copilot API & Metrics Insights
tags: [gh-300, api, metrics, insights, usage-analytics, compliance-reporting, rest-api]
created: 2026-04-17
updated: 2026-04-17
type: guide
---

> 📌 **Navigation:** [[INDEX|← Back to Index]]

# GitHub Copilot API & Metrics Insights

**EXAM CRITICAL:** Questions about what insights you can get from the API, what metrics are available, and how to use them for organizational understanding.

---

## Available APIs for Copilot Insights

### 1. Audit Log API (Enterprise/Business)

**Purpose:** Get administrative events (licenses, policies, agents)

**Endpoint:**
```bash
GET /enterprises/{enterprise}/audit-log
  ?action=copilot
  &per_page=100
  &after=2026-04-01
```

**Returns:**
```json
[
  {
    "action": "copilot.cfb_seat_assignment_created",
    "actor": "admin@company.com",
    "created_at": "2026-04-17T10:30:00Z",
    "data": {
      "user_id": "12345",
      "username": "developer",
      "organization": "myorg"
    }
  }
]
```

**What you learn:**
- License assignment/removal timeline
- Policy changes (when/who changed them)
- Custom agent lifecycle (created/updated/deleted)
- User access patterns

See [[audit-logs-guide]] for detailed examples.

### 2. Copilot Usage Metrics API

**Purpose:** Get adoption and usage statistics (if available)

**Endpoint:**
```bash
GET /orgs/{org}/copilot/usage
  ?per_page=100
```

**Available via:**
- GitHub REST API (Copilot Enterprise)
- GitHub GraphQL API
- Organization dashboards

**Returns (typical):**
```json
{
  "total_active_users": 45,
  "total_engaged_users": 38,
  "total_lines_accepted": 12500,
  "total_lines_suggested": 15600,
  "date": "2026-04-17"
}
```

**What you learn:**
- How many users are actively using Copilot
- Adoption rate (engaged vs. total)
- Code generation volume
- Acceptance rate (accepted / suggested)
- Trends over time

### 3. Organization Activity API

**Purpose:** View general organization activity (includes Copilot events)

**Endpoint:**
```bash
GET /orgs/{org}/audit-log
  ?include=web
```

**Returns:** Organization-level events (limited Copilot events)

---

## What Insights You CAN Get from APIs

### ✅ Obtainable Insights

| Insight | API | Available |
|---------|-----|-----------|
| How many users have Copilot licenses? | Audit Log | Copilot Business+ |
| When was Copilot enabled? | Audit Log | Copilot Business+ |
| Which users are active? | Usage Metrics | Copilot Enterprise |
| What's our adoption rate? | Usage Metrics | Copilot Enterprise |
| How many lines of code generated? | Usage Metrics | Copilot Enterprise |
| What's our refusal rate? | Usage Metrics | Copilot Enterprise |
| Who created a custom agent? | Audit Log | Copilot Business+ |
| When was a policy changed? | Audit Log | Copilot Business+ |
| Which orgs have Copilot enabled? | Audit Log | Copilot Enterprise |

### ❌ What You CANNOT Get from APIs

| Item | Why Not | Alternative |
|------|--------|-------------|
| Individual user prompts | Privacy protection | Custom logging hooks |
| Specific code analyzed | Privacy protection | Custom logging hooks |
| Per-user acceptance rates | Privacy protection | Dashboard aggregates only |
| Chat conversations | Privacy protection | User must share voluntarily |
| Which repos used Copilot | Privacy protection | Custom tracking required |
| Declined suggestions | Privacy protection | Not tracked by design |

**Key Exam Point:** Privacy is a feature - individual usage data is intentionally not exposed.

---

## Copilot Usage Metrics Dashboard

### Where to Access

```
Organization Settings → Copilot → Activity
  └── Usage & Adoption Dashboard
      ├── Overview (this month, last 3 months, etc.)
      ├── Adoption metrics
      ├── Feature breakdown
      └── Refusal rate tracking
```

### Key Metrics Explained

#### 1. Active Users
```
Definition: Users who generated at least 1 suggestion in period

Example: 
  Total users with license: 100
  Active users (this month): 35
  Adoption rate: 35%
```

#### 2. Engaged Users
```
Definition: Users who accepted at least 1 suggestion

Example:
  Active users: 35
  Engaged users: 28
  Engagement rate: 28/35 = 80%
```

#### 3. Lines Suggested vs. Accepted
```
Lines Suggested: Total lines Copilot offered
Lines Accepted: Lines the user actually used

Example:
  Suggested: 15,600 lines (month)
  Accepted: 12,500 lines (month)
  Acceptance rate: 80%
  
Refusal rate: 20% (user rejected)
```

#### 4. Acceptance Rate Over Time
```
Chart shows trend:
  Week 1: 75% (ramping up)
  Week 2: 78% (learning curve)
  Week 3: 82% (confidence growing)
  Week 4: 85% (proficiency)
  
Low acceptance rate might indicate:
  - Users don't trust Copilot yet
  - Suggestions not relevant
  - Team not trained
```

#### 5. Feature Usage Breakdown
```
Where are suggestions coming from?

Chart:
  └── Copilot in IDE
      ├── Inline suggestions: 60%
      ├── Chat: 30%
      └── Other: 10%
      
Or (alternative breakdown):
      ├── VS Code: 45%
      ├── JetBrains: 35%
      └── Other IDEs: 20%
```

---

## Using Metrics for Organizational Decisions

### Scenario 1: "Is Copilot worth the cost for us?"

**Use Metrics:**
```
1. Check active users: 100 licensed, 35 active (35%)
2. Low adoption might mean:
   - Insufficient training
   - Tool not relevant for team
   - Quality of suggestions poor

Decision:
  - Increase training
  - Assess feature fit
  - Get feedback from non-users
```

### Scenario 2: "Which team is adopting Copilot fastest?"

**Approach:**
```
Limited by Privacy:
  ❌ Can't query per-team metrics directly
  ✅ Can use custom tracking
  ✅ Survey team leads
  ✅ Ask in retro meetings
```

### Scenario 3: "Is Copilot actually improving productivity?"

**Use Metrics + External Data:**
```
Copilot metrics:
  - Lines generated: 12,500/month
  - Acceptance rate: 82%
  
External measurement:
  - Code review time: reduced 15%
  - Feature delivery: +12% faster
  - Bug rate: stable (good!)
  
Conclusion: Positive impact, continue using
```

### Scenario 4: "Our acceptance rate dropped from 85% to 60%. Why?"

**Investigation:**
```
Metrics show: Acceptance dropped
  ├── Check audit logs: No policy changes
  ├── Check active users: Still high
  ├── Check features: All still enabled
  
Likely causes:
  - Model change (Copilot updated)
  - Team added harder tasks (lower acceptance ok)
  - New team members unfamiliar with tool
  - Code style changed
  
Action:
  - Review feedback from users
  - Check PR comments about suggestions
  - Provide refresher training
```

---

## API Usage Examples

### Example 1: Export Audit Events to CSV

```bash
#!/bin/bash
curl -H "Authorization: token YOUR_TOKEN" \
  "https://api.github.com/enterprises/myenterprise/audit-log?action=copilot.cfb_seat_assignment_created" \
  | jq '.[] | [.actor.login, .created_at, .data.username] | @csv' \
  > copilot_licenses.csv
```

**Output:**
```
admin@company.com,2026-04-01T10:00:00Z,john_dev
admin@company.com,2026-04-02T11:30:00Z,jane_dev
admin@company.com,2026-04-03T09:15:00Z,bob_architect
```

### Example 2: Get Usage Metrics for Reporting

```bash
curl -H "Authorization: token YOUR_TOKEN" \
  "https://api.github.com/orgs/myorg/copilot/usage" \
  | jq '.'
```

**Output:**
```json
{
  "total_active_users": 45,
  "total_engaged_users": 38,
  "total_lines_accepted": 12500,
  "total_lines_suggested": 15600,
  "total_chats": 450,
  "total_pr_summaries": 120,
  "date": "2026-04-17"
}
```

### Example 3: Search for Policy Changes

```bash
curl -H "Authorization: token YOUR_TOKEN" \
  'https://api.github.com/enterprises/myenterprise/audit-log?action=copilot.cfb_policies_updated&after=2026-04-01' \
  | jq '.[] | {actor: .actor.login, when: .created_at, detail: .data}'
```

**Output:**
```json
{
  "actor": "enterprise_admin",
  "when": "2026-04-10T14:22:00Z",
  "detail": {
    "feature": "Copilot in IDE",
    "new_setting": "disabled"
  }
}
```

---

## Limitations & Privacy Considerations

### What's Intentionally NOT Tracked

**GitHub Design Choice:**
```
We don't track individual prompts/responses because:
  1. Privacy protection (your code stays yours)
  2. IP protection (your code isn't analyzed by GitHub)
  3. Regulatory compliance (HIPAA, GDPR compatible)
  4. Trust (users know their input is private)
```

### What This Means for Compliance

**If your organization needs:**

| Need | Solution |
|------|----------|
| Individual prompt tracking | Deploy custom logging hooks |
| Detailed usage per repository | Query custom metrics system |
| User behavior analysis | Use surveys + interviews |
| Cost allocation by team | Manual tracking or custom system |
| Sensitive data protection | `.copilotignore` + audit for access |

### Custom Logging Example

```javascript
// Custom hook to capture Copilot usage
// (would need Copilot hooks support)

module.exports = {
  "on_suggestion_accepted": async (suggestion) => {
    await log({
      user: suggestion.user,
      timestamp: suggestion.timestamp,
      lines_accepted: suggestion.lines.length,
      repository: suggestion.repo,
      // NOT: actual code (privacy)
      // NOT: prompt text (privacy)
    });
  }
};
```

---

## Common Exam Questions

### Q: "What can we learn from Copilot API?"
**A:** License usage, adoption rates, lines of code generated, policy changes, agent lifecycle. NOT individual prompts or user behavior.

### Q: "How long are usage metrics retained?"
**A:** Depends on plan/implementation. Typically 1-2 years in dashboard. Archive older data if needed for compliance.

### Q: "Can we see which team members use Copilot?"
**A:** No - by design, for privacy. Can see org adoption rate and active user count, but not per-user data.

### Q: "Our acceptance rate is 45%. What does this mean?"
**A:** Copilot makes suggestions, but team only uses 45% of them. Could indicate: low-quality suggestions, team doesn't trust tool, or incompatible with code style.

### Q: "How do we track ROI on Copilot?"
**A:** Use metrics for volume (lines/day) + external measurement (code review time, bug rate, deployment frequency).

### Q: "What if we need to prove individual users accessed Copilot?"
**A:** Audit logs show license assignments (who was given access) and removal. For actual usage, need custom logging.

---

## Related Topics

- [[audit-logs-guide]] - Detailed audit log examples
- [[enterprise-management]] - How metrics fit in organization structure
- [[file-exclusions-guide]] - Protecting sensitive files from being analyzed

---

**Last Updated:** April 17, 2026  
**Status:** Complete - Exam Ready

**Key Takeaway for Exam:**
- APIs provide aggregated, privacy-safe data
- Audit logs track admin actions (licenses, policies)
- Usage metrics show adoption and engagement
- Individual prompts/code NOT tracked (by design)
- Custom solutions needed for detailed tracking
