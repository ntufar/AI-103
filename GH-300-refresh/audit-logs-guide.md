---
title: Audit Logs, Compliance & Monitoring for Copilot
tags: [gh-300, audit-logs, compliance, monitoring, enterprise, business, security, retention]
created: 2026-04-17
updated: 2026-04-17
type: guide
---

> 📌 **Navigation:** [[INDEX|← Back to Index]]

# Audit Logs, Compliance & Monitoring for Copilot

**EXAM CRITICAL:** GH-300 tests audit logs heavily for enterprise features - what they contain, retention periods, and how to access them.

---

## What Are Audit Logs?

Audit logs are **immutable, timestamped records** of administrative actions and events in GitHub, specifically related to Copilot in Business and Enterprise plans.

### Key Point
- **Audit logs are only available in:** Copilot Business and Copilot Enterprise
- **Free/Pro:** No audit logs
- **Who can access:** Enterprise owners or users with "Read enterprise audit logs" custom role

---

## What Audit Logs Contain

### Administrative/Licensing Events (Always Tracked)

```
License Management Events:
├── copilot.cfb_seat_assignment_created
│   └── User was assigned a Copilot license
│   └── Who: [user], When: [timestamp], Org: [org]
│
├── copilot.cfb_seat_assignment_removed
│   └── User's Copilot license was revoked
│   └── Who: [user], When: [timestamp], Action by: [admin]
│
├── copilot.cfb_seat_blocked
│   └── User was blocked from using their license
│
├── copilot.cfb_seat_unblocked
│   └── User's block was removed

Policy & Settings Events:
├── copilot.cfb_policies_updated
│   └── Feature policy was changed
│   └── What: [feature name], New setting: [enabled/disabled]
│
├── copilot.cfb_organization_settings_updated
│   └── Organization settings changed
│   └── Example: IDE support, CLI support, chat enabled/disabled
│
├── copilot.cfb_enterprise_settings_updated
│   └── Enterprise-wide settings changed
│
├── copilot.custom_model_provider_created
│   └── Custom LLM integration added
│
├── copilot.custom_model_provider_deleted
│   └── Custom LLM integration removed

Agent & Automation Events:
├── copilot.agent_created
│   └── New custom agent was registered
│
├── copilot.agent_updated
│   └── Custom agent was modified
│
├── copilot.agent_deleted
│   └── Custom agent was removed
│
└── copilot.agent_execution
    └── Agent task was executed (when tracking enabled)
```

### What's NOT in Audit Logs (Privacy Protection)

❌ **Individual prompts users entered**
❌ **Individual code suggestions generated**
❌ **Which code files were analyzed**
❌ **Chat messages or conversations**
❌ **Local IDE session data**

**Why?** GitHub respects user privacy - your code and prompts stay private, not tracked in audit logs.

**Important:** If you need to track individual prompts/sessions, you need **custom logging solutions** with webhooks or hooks.

---

## Where to Access Audit Logs

### For Enterprise Owners

```
github.com/settings/enterprises
  └── [Your Enterprise]
      └── Settings
          └── Audit log
              └── View all enterprise events
```

**Filter by:**
- `action:copilot` → Show only Copilot events
- `action:copilot.cfb_seat_assignment_created` → Specific event
- `actor:Copilot` → Agent/automation actions

### For Organization Owners (Limited)

```
github.com/[org]/settings
  └── Audit log (if Copilot Business/Enterprise is enabled)
      └── Organization-level events only
          (not full enterprise view)
```

### Programmatically Via API

**Enterprise Audit Log API:**
```bash
GET /enterprises/{enterprise}/audit-log
  ?action=copilot
  &per_page=100
```

Returns JSON with all matching events, timestamps, actors, details.

---

## Retention Periods

### Default Retention

**Audit logs retained for:** **180 days** (6 months)

**After 180 days:**
- Logs are automatically deleted
- No recovery possible
- Enterprise must archive elsewhere if long-term retention needed

### Important Exam Question Format
"An audit log event happened 200 days ago. Can we access it?"
**Answer:** No (unless it was exported before the 180-day window)

### Long-Term Retention Strategy

**If you need logs beyond 180 days:**

```
GitHub Audit Log
  ↓
1. Stream to external SIEM (Security Information & Event Management)
   ├── Splunk
   ├── Datadog
   ├── Azure Sentinel
   └── Other systems
  ↓
2. Archive in external storage
   ├── S3, GCS, Azure Blob
   └── Long-term archive
  ↓
3. Use external system for reporting/compliance
```

**GitHub provides Streaming API for this:**
```
Enterprise Settings → Audit log → Streaming
  └── Enable streaming to external URL/system
```

### Compliance & Auditing

Common use cases for audit logs:
- **SOC 2 Compliance** → Prove security controls exist
- **HIPAA Compliance** → Track access to patient data (if applicable)
- **Internal Audits** → Track who accessed what, when
- **Incident Response** → Timeline of events during security issue

---

## Usage Metrics vs. Audit Logs

### Key Difference

| Aspect | Audit Logs | Usage Metrics |
|--------|-----------|---------------|
| **What it tracks** | Admin actions, license changes, policy updates | Feature usage, adoption, lines generated |
| **User privacy** | ✅ Private | ✅ Private (aggregated) |
| **Time range** | Last 180 days | Configurable |
| **Granularity** | Individual events | Aggregated statistics |
| **Who can access** | Enterprise/org admins | Org admins (basic dashboard) |
| **Requires export?** | No (180 day view) | Often exported to analytics tools |

### Usage Metrics Content

**In Copilot Dashboard:**
```
Organization Copilot Usage:
├── Total Active Users (this month)
├── Total Lines Accepted (this month)
├── Adoption Rate (%)
├── Cost Analysis
├── Feature Usage Breakdown
│   ├── Chat usage %
│   ├── Inline suggestions %
│   └── Agent usage %
├── Refusal Rate (% suggestions declined)
└── Performance Trends (over time)
```

**NOT shown:** Individual user data, specific acceptances per person, or which code was analyzed.

---

## API Insights from Audit Logs

### What Information You Can Extract

**Using Audit Log API:**

```json
{
  "action": "copilot.cfb_seat_assignment_created",
  "actor": "admin@company.com",
  "created_at": "2026-04-17T10:30:00Z",
  "data": {
    "user_id": "123456",
    "username": "developer",
    "organization": "myorg",
    "plan": "business"
  }
}
```

**You can discover:**
- Which users got licenses and when
- Which licenses were revoked and when
- Who made the changes (actor/admin)
- When policies were updated and to what
- Custom agents that were created/modified
- Any agents that executed tasks

### Using API for Compliance Reporting

```bash
# Get all Copilot seat assignments in last 180 days
curl -H "Authorization: token YOUR_TOKEN" \
  "https://api.github.com/enterprises/myent/audit-log?action=copilot.cfb_seat_assignment_created"

# Results can be:
# - Imported to Excel for reporting
# - Streamed to BI tools
# - Analyzed for access patterns
# - Used for reconciliation audits
```

---

## Streaming Audit Logs

### Why Stream Logs?

1. **Compliance** - Ensure you have 90+ year record for regulations
2. **Real-time Alerts** - Alert on suspicious activity immediately
3. **Integration** - Send logs to your SOC or security platform
4. **Backup** - Protect against accidental deletion
5. **Analysis** - Run queries beyond 180 days

### How to Enable Streaming

```
Enterprise Settings
  └── Audit log
      └── Streaming
          ├── Webhook endpoint (your system)
          ├── App registration (for auth)
          └── Enable streaming
```

**Your system receives:**
- Real-time JSON events
- Every Copilot action
- Allows you to store permanently

### Webhook Format

```json
{
  "data": {
    "action": "copilot.cfb_policies_updated",
    "actor": {
      "login": "admin",
      "id": 12345
    },
    "created_at": "2026-04-17T14:22:00Z",
    "org": "myorg",
    "details": {
      "feature": "Copilot in IDE",
      "setting": "disabled"
    }
  }
}
```

---

## Common Exam Scenarios

### Scenario 1: "We need to prove Copilot was enabled on March 15"
**Solution:**
1. Go to Enterprise Settings → Audit log
2. Search: `action:copilot.cfb_policies_updated created:2026-03-15`
3. Find the event showing `Copilot in IDE` → `enabled`
4. Timestamp proves when it happened

### Scenario 2: "Did developer X access Copilot between X dates?"
**Solution:**
1. Search audit logs: `action:copilot.cfb_seat_assignment_created username:developer_x`
2. If found: Yes, access was granted on that date
3. Search: `action:copilot.cfb_seat_assignment_removed username:developer_x`
4. If found: Access was revoked on that date

### Scenario 3: "We need compliance proof of user removals"
**Solution:**
1. Export all: `action:copilot.cfb_seat_assignment_removed`
2. Filter by date range needed
3. Provides timestamp, admin who did it, user affected
4. Perfect for SOC 2 Type II audit

### Scenario 4: "We need logs from 200 days ago but only save last 180"
**Solution:**
1. Too late if not previously exported
2. But have them stream now to external system
3. Or: Check if export was done in prior audit trail
4. Going forward: Maintain streaming to ensure capture

### Scenario 5: "A custom agent was compromised, when was it created?"
**Solution:**
1. Search: `action:copilot.agent_created`
2. Find the agent in question
3. Timestamp shows when it was added
4. Can identify who created it (actor field)

---

## Configuring Policies for Security

### Audit-Related Policies (Copilot Enterprise Only)

```
Enterprise Settings → Copilot → Policies
└── Audit Settings (if enabled)
    ├── Log retention period
    ├── Streaming configuration
    ├── Event filtering (what to capture)
    └── Access control (who can view)
```

### Best Practices

1. **Enable streaming immediately** (don't wait for breach)
2. **Retain logs for 90+ days** in primary system
3. **Archive annually** to cold storage
4. **Review events monthly** for compliance
5. **Set up alerts** for suspicious patterns:
   - Bulk user removals
   - Rapid policy changes
   - Unusual agent activity

---

## Related Topics

- [[enterprise-management]] - Managing Copilot in organizations
- [[file-exclusions-guide]] - Protecting sensitive files from Copilot
- [[api-insights-guide]] - API usage and metrics insights

---

**Last Updated:** April 17, 2026  
**Status:** Complete - Exam Ready

**Key Takeaway for Exam:** 
- Audit logs = Admin actions, licensing, policies (180 days)
- NOT prompts/code (privacy)
- Stream for long-term retention
- API accessible for reporting/compliance
