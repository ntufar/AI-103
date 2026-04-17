---
title: GH-300 Practice Scenarios
tags: [gh-300, practice, scenarios, real-world, solutions, exam-prep]
created: 2026-04-16
updated: 2026-04-16
type: practice
---

> 📌 **Navigation:** [[INDEX|← Back to Index]] | [[exam-objectives|Exam Objectives]]

# GH-300 Practice Scenarios

Test your knowledge with these real-world scenarios. Solutions follow each.

---

## Scenario 1: Choosing the Right Feature

**Situation:**
Your team is building a new authentication system. The feature is complex with multiple components (password validation, OAuth integration, session management, API token handling). A junior developer asks what approach to use with Copilot.

**Question:** Which Copilot feature would be MOST appropriate for this situation?

A) Use inline suggestions while coding each component
B) Use Plan Mode to structure the implementation
C) Use Agent Mode to auto-generate all files
D) Use Spark to describe requirements

**Your Answer:** ___

---

### Solution: Scenario 1

**Correct Answer: B) Use Plan Mode**

**Why:**
- Plan Mode breaks down complex features into steps
- Perfect for multi-component systems
- Helps structure implementation before coding
- Ensures coherent architecture across components
- Pro+ feature available

**Why not others:**
- A) Inline suggestions are reactive, not strategic
- C) Agent Mode is autonomous, not good for complex decision-making
- D) Spark generates code, doesn't plan structure

**Real approach:**
1. Use Plan Mode in Chat to structure 5-step implementation
2. Review/modify the plan with team
3. Then use inline suggestions for each step
4. Use Chat for specific problems
5. Code review each component

---

## Scenario 2: Privacy & Exclusions

**Situation:**
Your company is using GitHub Copilot Business for a healthcare application. You need to:
- Develop features using patient data
- Include API keys for third-party services
- Reference proprietary algorithms

**Question:** How should you configure privacy?

A) Use .gitignore to prevent Copilot from seeing sensitive files
B) Create .copilotignore and exclude patient data and API keys
C) Rely on duplication detection to catch sensitive data
D) Disable Copilot for healthcare code entirely

**Your Answer:** ___

---

### Solution: Scenario 2

**Correct Answer: B) Create .copilotignore and exclude patient data and API keys**

**Why:**
- `.copilotignore` is designed exactly for this purpose
- Prevents Copilot from reading sensitive files
- Proactive protection (not reactive like duplication detection)
- Business plan contractually doesn't use data for training anyway
- Removes risk of accidental leakage

**What to exclude:**
```
# In .copilotignore
*.env
**/api-keys.json
src/data/patients/
config/secrets.yml
algorithms/proprietary-*.ts
```

**Why not others:**
- A) .gitignore doesn't affect Copilot, only Git
- C) Duplication detection is post-generation, not preventive
- D) Overkill; proper exclusions solve the problem

**Real approach:**
1. Create .copilotignore at project root
2. Exclude all sensitive files
3. Still use Copilot for business logic
4. Review all suggestions carefully
5. Business plan provides additional safety

---

## Scenario 3: Prompt Engineering

**Situation:**
You ask Copilot: "Write a function to validate input"

Copilot returns a function but you get poor results. What's wrong?

**Which version would be a BETTER prompt?**

A) "Write a better function to validate input"
B) "Write a function to validate email addresses in a Node.js/Express backend. It should check for proper format using regex, return true/false, and throw a descriptive error if invalid. Example: validateEmail('user@example.com') returns true"
C) "Create a comprehensive validation function"
D) "Write validation code like in enterprise apps"

**Your Answer:** ___

---

### Solution: Scenario 3

**Correct Answer: B)**

**Why B is better:**
- ✅ Specific (email, not generic input)
- ✅ Context (Node.js/Express)
- ✅ Constraints (regex, true/false, error handling)
- ✅ Example of desired output
- ✅ Clear acceptance criteria

**Why others are worse:**
- A) "Better" is vague - no guidance
- C) "Comprehensive" is vague and open-ended
- D) "Enterprise" is not specific enough

**Original problem:**
"Write a function to validate input"
- Too vague (what input?)
- No context (language? framework?)
- No constraints (what does valid mean?)
- No examples

**Better prompt structure:**
```
[SPECIFIC]: Validate email addresses
[CONTEXT]: Node.js/Express backend
[CONSTRAINTS]: Regex, return boolean, throw on invalid
[EXAMPLE]: validateEmail('test@test.com') → true
```

---

## Scenario 4: Responsible AI Use

**Situation:**
A Copilot suggestion includes security-sensitive code that Copilot flagged with a duplication detection warning. Your manager says: "It's already in Copilot, so it must be safe to use."

**What should you do?**

A) Use it - Copilot already filtered it
B) Ignore the warning and use it anyway
C) Research the original code, understand the license, and make an informed decision
D) Never use code with duplication warnings

**Your Answer:** ___

---

### Solution: Scenario 4

**Correct Answer: C) Research the original code, understand the license, and make an informed decision**

**Why:**
- Duplication detection is for TRANSPARENCY, not automatic approval
- YOU are responsible for code and compliance
- Different licenses have different implications
- You can use it if you're compliant
- Manager's reasoning ("Copilot said it's OK") is backwards

**What to do:**
1. Note which code was flagged as duplicate
2. Find the original source
3. Check the license (GPL? MIT? Apache?)
4. Verify you're compliant with that license
5. Document the decision
6. If compliant, you can use it
7. If not compliant, rewrite without copying

**Why not others:**
- A) Filtered doesn't mean approved
- B) Never ignore warnings
- D) Sometimes you can use flagged code if compliant

**Key principle:**
Duplication detection = "Hey, this comes from X with license Y"
Your decision = Whether to use it

---

## Scenario 5: Data Privacy by Plan

**Situation:**
Your startup currently uses Copilot Pro. You're planning expansion into regulated industries (healthcare, finance). Your CEO asks whether you need to upgrade.

**Question:** What's the most important reason to upgrade to Business?

A) Faster response times
B) Better AI model
C) Contractual guarantee that code is not used for training
D) Better IDE integration

**Your Answer:** ___

---

### Solution: Scenario 5

**Correct Answer: C) Contractual guarantee that code is not used for training**

**Why:**
- Compliance/regulated industries require this guarantee
- Pro plan doesn't explicitly exclude training
- Business plan = legal contract (Microsoft commitment)
- This is the key difference for regulated data
- Required for HIPAA, PCI-DSS, financial regulations

**Key differences:**
- **Pro:** Helpful tool, code may be used for training
- **Business:** Contractual protection, code NOT used for training

**Why not others:**
- A) Pro and Business have similar response times
- B) Model quality is similar (Pro has good access to GPT-4)
- D) IDE integration is same across plans

**Real answer for CEO:**
"We need Business plan because it contractually prevents GitHub from using our code to train models. This is required for healthcare and finance regulations. The extra cost is justified by compliance safety."

---

## Scenario 6: Feature Availability

**Situation:**
Your team member says: "I want to use Agent Mode to refactor this large codebase automatically."

You need to:
1. Confirm this is possible
2. Determine if it's appropriate

**Which statements are TRUE?**

A) Agent Mode is available in free plan
B) Agent Mode can modify multiple files autonomously
C) Agent Mode should be used without human review
D) Agent Mode is ideal for refactoring legacy code

**Your Answer:** ___ (may be multiple)

---

### Solution: Scenario 6

**True Statements: B) and D)**

**B) True:** Agent Mode can modify multiple files autonomously
- ✅ This is what Agent Mode does
- ✅ Can create and modify multiple files
- ✅ Operates autonomously on your behalf

**D) True:** Agent Mode is ideal for refactoring legacy code
- ✅ Perfect for large-scale changes
- ✅ Can apply consistent patterns
- ✅ Handles multiple files together

**False statements:**

**A) False:** Agent Mode is available in free plan
- ❌ Requires Copilot Pro or higher
- ❌ Premium feature only

**C) False:** Agent Mode should be used without human review
- ❌ Always review autonomously generated changes
- ❌ Test thoroughly before accepting
- ❌ Code review is essential
- ❌ You're responsible for validation

**Correct approach:**
1. Enable Agent Mode
2. Describe refactoring goal in Chat
3. Agent generates plan and file changes
4. Review all changes carefully
5. Test the refactored code
6. Run through code review
7. Merge with confidence

---

## Scenario 7: CLI Usage

**Situation:**
A developer on your team struggles with complex bash commands. They ask if Copilot can help with this.

**Question:** What's the best Copilot solution?

A) Chat in IDE to ask about bash syntax
B) Use Copilot CLI and ask it to explain the command first
C) Search GitHub documentation
D) Ask on Stack Overflow

**Your Answer:** ___

---

### Solution: Scenario 7

**Correct Answer: B) Use Copilot CLI and ask it to explain the command first**

**Why:**
- Direct, IDE-independent solution
- Explains actual commands before running (safer)
- Faster than searching docs
- Works in terminal context
- Can also use `copilot -p` for a one-off explanation

**How it works:**
```
# Understand a command
copilot -p "Explain what git rebase -i HEAD~3 does"

# Start an interactive session
copilot
/login
> Explain what `git rebase -i HEAD~3` does
```

**Why not others:**
- A) Chat works too, but CLI is better in terminal
- C) Docs don't explain in your context
- D) SO takes time, less specific to their setup

**Setup (if needed):**
```
npm install -g @github/copilot
copilot
/login
```

**Benefits:**
- Stay in terminal (no context switching)
- Learn commands safely (understand before running)
- Multi-turn conversation for complex tasks
- No risk of copy-pasting without understanding

---

## Scenario 8: Code Review

**Situation:**
You're implementing code review policies for your organization. You need to:
- Enforce coding standards
- Catch security issues automatically
- Allow customization per repository

**Question:** What tools/features should you use?

A) Just rely on Copilot's inline suggestions
B) Enable Copilot Code Review + custom instruction files
C) Disable Copilot entirely for code review
D) Have team members review all suggestions manually

**Your Answer:** ___

---

### Solution: Scenario 8

**Correct Answer: B) Enable Copilot Code Review + custom instruction files**

**Why:**
- Code Review = automated review of PR changes
- Instruction files = define standards (org + repo level)
- This combination = enforcement without manual burden
- Requires Business plan

**How it works:**
1. Create `.github/copilot-instructions.md`
   ```markdown
   # Organization-wide Standards
   - Use TypeScript for all new code
   - Require JSDoc comments
   - No console.log in production
   - Security review required for auth code
   ```

2. Enable Code Review in org settings

3. Copilot reviews every PR against standards

4. Comments on violations automatically

5. Team reviews Copilot's suggestions

**Why not others:**
- A) Inline suggestions are during development, not review
- C) Defeats the purpose of having Copilot
- D) Defeats purpose of automation

**Key features:**
- ✅ Automatic review of all PRs
- ✅ Suggests improvements
- ✅ Customizable per repo
- ✅ Frees up team time
- ✅ Consistent enforcement

---

## Scenario 9: Duplication Detection Interpretation

**Situation:**
Copilot suggests a sorting algorithm. It flags: "Code matches 92% with public repository: quicksort-lib (MIT License)"

**What does this mean?**

A) You can't use this code
B) GitHub won't let you commit it
C) You can use it because it's MIT licensed
D) You should verify the license compatibility

**Your Answer:** ___

---

### Solution: Scenario 9

**Correct Answer: D) You should verify the license compatibility**

**What duplication detection means:**
- "This matches public code with X license"
- "Here's the information you need"
- "You make the decision"

**MIT License implications:**
- ✅ MIT = Very permissive
- ✅ You CAN use it in proprietary software
- ✅ Just include license attribution
- ✅ Most commonly used, safest

**Decision process:**
1. Note the similarity (92%)
2. Find the original code
3. Check the license (MIT in this case)
4. Verify compatibility with YOUR project
5. If compatible, you can use it
6. Document the decision if needed

**Different license scenarios:**
- **MIT/Apache/BSD:** Usually safe ✅
- **GPL:** Only if your project is open source
- **AGPL:** Very restrictive, usually problematic
- **Custom license:** Research terms carefully

**Why not others:**
- A) False - MIT is permissive
- B) False - GitHub allows it, you control what commits
- C) Partially true, but you should still verify

**Key principle:** Duplication detection is not a blocker, it's information. You make the decision based on license compatibility.

---

## Scenario 10: Prompt Iteration

**Situation:**
You ask Copilot: "Write a sort function" and get a basic bubble sort that's O(n²).

You need better performance for your large dataset.

**What's the best next step?**

A) Accept the suggestion and optimize manually later
B) Ask: "Write a more efficient sort function for large datasets using JavaScript"
C) Ask: "Implement quicksort or merge sort for O(n log n) performance. Use this pattern: [show existing implementation] Keep consistent variable naming"
D) Reject and ask a completely different question

**Your Answer:** ___

---

### Solution: Scenario 10

**Correct Answer: C) Ask with specific constraints and example pattern**

**Why C is best:**
- ✅ Specifies algorithm (quicksort or merge sort)
- ✅ States performance goal (O(n log n))
- ✅ Provides pattern example (ensures style consistency)
- ✅ Requests specific variable naming
- ✅ Clear constraints and context

**Evolution of prompts:**

**Original (too vague):**
"Write a sort function"
→ Result: Basic but inefficient

**Better (adds constraints):**
"Write a more efficient sort function for large datasets"
→ Result: Better, but may not match your style

**Best (adds example + specific requirements):**
"Implement quicksort or merge sort with O(n log n) performance...
Use this pattern: [example]"
→ Result: Optimized, matches your style, exactly what you need

**Key iterative prompting technique:**
1. Initial request (basic)
2. Review result (too simple)
3. Add constraints (more specific)
4. Provide example (style match)
5. Get desired result

**Why not others:**
- A) Procrastinating optimization isn't efficient
- B) Better than original, but lacks specific algorithm
- D) Unnecessary, iteration works great

---

## Summary: Key Takeaways

**From these scenarios:**

1. **Choose features wisely** - Plan Mode for complex, Agent Mode for autonomous changes
2. **Privacy proactive** - Use .copilotignore, not reactive filtering
3. **Prompts matter** - Specific > vague, examples clarify
4. **Responsibility is yours** - Copilot is tool, you validate
5. **Plans have limits** - Know what's available at each tier
6. **Duplication = information** - Not a blocker, you decide
7. **CLI for terminal** - Use `copilot` before running commands
8. **Policies enforce standards** - Instructions + code review
9. **Licenses matter** - Understand implications
10. **Iterate prompts** - First try often not perfect, refine

---

## Exam Strategy

When you see scenarios like these on the exam:

1. **Read carefully** - Identify what's being asked
2. **Eliminate obvious wrong answers** - Usually easy
3. **Choose responsible approach** - Safe > risky
4. **Think practically** - Real-world application
5. **Remember trade-offs** - No feature is perfect for everything

**You've got this!** 🎯
