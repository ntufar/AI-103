---
title: GitHub Copilot Enterprise & Organization Management
tags: [gh-300, enterprise, organization, management, business, policies, features]
created: 2026-04-17
updated: 2026-04-17
type: guide
---

> 📌 **Navigation:** [[INDEX|← Back to Index]]

# GitHub Copilot Enterprise & Organization Management

**EXAM CRITICAL:** GH-300 heavily tests organizational management features, especially for enterprise and business deployments.

---

## Organizational Structure & Licensing

### Enterprise vs. Organization vs. Business Plan

```
GitHub Enterprise
    └── Enterprise Owner (manages Copilot plan)
        ├── Organization 1 (multiple orgs within enterprise)
        │   ├── Org Owner (manages within org boundaries)
        │   └── Team Members (users with Copilot licenses)
        ├── Organization 2
        │   └── Team Members
        └── Organization N
```

**Key Distinctions:**

| Aspect | Organization | Enterprise | Enterprise Cloud (Copilot Business) |
|--------|---------|-----------|---------|
| **Plan Assigned At** | Organization level | Enterprise level | Enterprise level |
| **Who Controls It** | Org owner | Enterprise owner | Enterprise owner |
| **Can Have Multiple Orgs** | N/A | ✅ Yes | ✅ Yes |
| **Audit Logs** | Org-level only | Enterprise-wide | Enterprise-wide |
| **Policy Control** | Org owner (within limits) | Enterprise owner | Enterprise owner |
| **Member Types** | Managed users | Managed users | Managed or external users |

**Important:** The exam calls these "workgroups" or organizational units - these refer to the **organization structure within the enterprise**.

---

## Copilot Plans for Organizations

### Copilot Business
- **For:** Teams/organizations wanting centralized management
- **Requires:** GitHub Enterprise Cloud or Team plan
- **Key Features:**
  - Manage licenses at organization level
  - Access to audit logs
  - Code privacy (your code won't be used for Copilot training)
  - Basic policy controls
  - Partial feature governance

### Copilot Enterprise
- **For:** Large organizations needing complete control
- **Requires:** GitHub Enterprise Cloud
- **Key Features:**
  - All Business features
  - **Full policy control** at enterprise level
  - Enterprise-wide audit logs with detailed tracking
  - Custom agent management
  - Knowledge base integration (Copilot Enterprise)
  - Comprehensive usage analytics and metrics
  - Content exclusions and guardrails
  - LLM model customization

**Test Tip:** If exam asks about "enterprise feature" - think Copilot Enterprise (not just Business).

---

## Access Management & License Assignment

### How Licenses Are Granted

**Flow:**
```
Enterprise Owner subscribes to Copilot Business/Enterprise
    ↓
Enterprise Owner enables Copilot for specific organizations
    ↓
Org Owner assigns licenses to team members
    ↓
Team members request/receive access
    ↓
Users can activate Copilot in IDE, CLI, Web
```

### Access Control Models

**1. Organization-Level Access Control**
```
Organization Settings → Copilot
  ├── Grant access to selected teams
  └── Or grant access to all members
```

**2. Repository-Level Access Control (for specific features)**
```
Organization Settings → Copilot → Cloud Agent
  └── Enable/disable in specific repositories
      (e.g., only allow Copilot Agent in "main" repo)
```

**3. Enterprise-Level Policy (highest precedence)**
```
Enterprise Settings → Copilot → Policies
  └── Can override all org/repo settings
      (e.g., disable feature everywhere)
```

### How to See If User Has Access

1. User goes to: `https://github.com/settings/copilot`
2. Under "Get Copilot from an organization" - see available orgs
3. Or in IDE settings → Extensions → GitHub Copilot → Sign in

**Important:** Users must be explicitly assigned a license, even if they're org members.

---

## Managing Policies & Features

### What Can Be Controlled

**At Organization Level:**
- ✅ Enable/disable Copilot Chat
- ✅ Enable/disable inline suggestions
- ✅ Enable/disable specific IDE editors
- ✅ Enable/disable Copilot in command line
- ✅ Enable/disable third-party agents (Claude, Codex)
- ✅ Allow preview/beta features
- ✅ Opt in to feedback collection
- ✅ Model selection (with Copilot Enterprise)

**At Enterprise Level (overrides org):**
- ✅ All of the above
- ✅ Set enterprise-wide defaults
- ✅ Grant to selected orgs only ("Enabled for selected organizations")
- ✅ Content exclusion patterns
- ✅ Guardrails and safety settings
- ✅ Custom model configuration

### Policy Enforcement Options

**For Each Policy:**
```
Unconfigured → No enforcement (each org decides)
    ↓
Enabled → Feature available to all assigned users
    ↓
Disabled → Feature blocked for all assigned users
```

**For Enterprise-Wide Policy:**
```
No Policy → Let orgs decide
    ↓
Enabled Everywhere → Feature available in all orgs
    ↓
Enabled for Selected Organizations → Only specific orgs
    ↓
Disabled Everywhere → Feature blocked everywhere
```

**Exam Example:** "An enterprise admin disabled chat feature across all organizations." This blocks Copilot Chat completely; org owners cannot override.

---

## Managing Cloud Agents

### What Are Cloud Agents?

Autonomous agents that can:
- Read and analyze code
- Make changes across multiple files
- Run terminal commands
- Create pull requests
- Self-correct errors

### Agent Types

**Built-in Agents:**
1. **Plan Agent** - Creates implementation plans
2. **Agent Mode** - Autonomous task completion
3. **Ask Mode** - Question answering

**Third-Party Coding Agents:**
1. **Anthropic Claude Agent** - Via Claude integration
2. **OpenAI Codex-based agents** - Alternative agent

### How to Enable/Disable Agents

**For Organization:**
```
Org Settings → Copilot → Policies
  ├── Copilot in IDE → Enable/Disable agents
  └── Cloud Agent → Enable/Disable + select repos
```

**For Enterprise:**
```
Enterprise Settings → Copilot → Policies
  ├── Agents (IDE)
  ├── Cloud Agent Availability
  └── Third-Party Agents (Claude, etc.)
```

### Limiting Agent Access to Specific Repos

```
Org Settings → Copilot → Cloud Agent
  └── "Enable in specific repositories"
      └── Select which repos agents can access
```

**Important:** Agents access all files in enabled repos. Use [[file-exclusions-guide]] to protect sensitive files.

---

## Usage Monitoring & Analytics

### What Data Can Be Viewed

**Available in Dashboards:**
- Number of active users
- Number of acceptances (lines of code generated)
- Adoption rate per org/team
- Cost per user
- Feature utilization (chat vs. inline)
- Refusal rate (percentage suggestions declined)

**Important:** This is aggregated data. No individual prompt visibility at organization level.

### Where to Find Metrics

**For Org Admin:**
```
Org Settings → Copilot → Activity
  └── View usage by team member
```

**For Enterprise Admin:**
```
Enterprise Settings → Copilot → Usage & Adoption Metrics
  └── Organization-wide aggregate data
```

### What's NOT Tracked (Privacy)

- Individual prompts users entered
- Individual code suggestions generated
- Accepted vs. rejected suggestions per user
- Which files were analyzed

These require **custom logging solutions** if needed (see [[audit-logs-guide]]).

---

## Removing Access & License Management

### Revoking User Access

**Option 1: Remove from organization**
```
Org Settings → Members → Remove member
  └── User loses all Copilot access
```

**Option 2: Remove from Copilot team**
```
Org Settings → Copilot → Team access
  └── Deselect user
  └── User keeps org membership, loses Copilot
```

**Option 3: Change assignment at enterprise level**
```
Enterprise Settings → Copilot → Seat Management
  └── Unassign license from user
```

### What Happens When License Is Removed

- User cannot activate new Copilot features
- Existing Copilot features may continue briefly (grace period)
- Audit log records the removal event
- User still sees Copilot icon but cannot use

---

## Policies & Conflicts

### What Happens When Policies Conflict?

**Scenario:** Org1 enables Chat, but Enterprise disables it.
```
Result → Chat is DISABLED (enterprise wins)
```

**Scenario:** Org1 has no policy, Org2 enables Chat, Enterprise has no policy.
```
Result → Chat is ENABLED (more permissive)
```

**Precedence Order:**
```
1. Enterprise policy (highest) - if defined, overrides all
2. Organization policy - if no enterprise policy
3. Default behavior (least restrictive)
```

**Exam Tip:** Questions like "Why can't user in Org A access feature?" → Check enterprise policy first.

---

## Copilot for Managing GitHub

### Using Copilot to Manage Copilot

Some newer features (Copilot Enterprise only):
- View Copilot metrics via Copilot Chat (ask questions about usage)
- Get recommendations on policy changes
- Identify top contributors to Copilot
- Generate reports on adoption

### Audit Events Related to Copilot Management

**Examples of Events Logged:**
- `copilot.cfb_seat_assignment_created` → License assigned
- `copilot.cfb_seat_assignment_removed` → License removed
- `copilot.cfb_policies_updated` → Policy changed
- `copilot.cfb_organization_settings_updated` → Org settings changed
- `copilot.agent_created` → Custom agent added
- `copilot.agent_updated` → Custom agent modified

See [[audit-logs-guide]] for full list and details.

---

## Common Exam Scenarios

### Scenario 1: "We need to protect customer data files"
**Solution:**
1. Use `.copilotignore` file to exclude `/data/customers/`
2. Or use enterprise content exclusion policies
3. Both ensure Copilot won't see these files

See [[file-exclusions-guide]].

### Scenario 2: "We want analytics but can't store sensitive data"
**Solution:**
1. Enable audit logs → organization/enterprise captures usage
2. Stream logs to external SIEM system
3. Use custom hooks/solutions for detailed prompts (if needed)
4. Review metrics dashboard for adoption data

### Scenario 3: "Some teams use Copilot, others shouldn't"
**Solution:**
1. At org level: "Enabled for selected organizations"
2. At enterprise: Enable Copilot for Org A only
3. Org B gets no access, regardless of requests

### Scenario 4: "We enabled agents but want to limit repo access"
**Solution:**
1. Org Settings → Copilot → Cloud Agent
2. Enable agents
3. Select "specific repositories"
4. Choose which repos agents can access

### Scenario 5: "An admin needs to understand feature availability"
**Solution:**
1. Check org Settings → Copilot → Policies page
2. Look for each feature's enforcement setting
3. If set to "Disabled" - feature unavailable
4. If "Enabled" - feature available to licensed users

---

## Related Topics

- [[audit-logs-guide]] - Track all Copilot management changes
- [[file-exclusions-guide]] - Exclude files from Copilot
- [[api-insights-guide]] - Get insights from API and metrics

---

**Last Updated:** April 17, 2026  
**Status:** Complete - Exam Ready
