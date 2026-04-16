---
title: Prompt Engineering & Context Crafting Guide
tags: [gh-300, prompt-engineering, prompt-structure, best-practices, context-crafting]
created: 2026-04-16
updated: 2026-04-16
type: deep-dive
---

> 📌 **Navigation:** [[INDEX|← Back to Index]] | [[exam-objectives|Exam Objectives]]

# Prompt Engineering & Context Crafting Guide

## What Makes a Good Prompt?

A good prompt to Copilot is like a clear specification to a developer. It should be:
- **Specific** - Not vague or ambiguous
- **Contextual** - Include relevant information
- **Constrained** - Define limits and requirements
- **Example-driven** - Show what you want, not just describe it

---

## Prompt Structure Framework

### Basic Structure
```
[GOAL] + [CONTEXT] + [CONSTRAINTS] + [EXAMPLE/FORMAT]
```

### Detailed Template

```
I need to write a [THING] that [GOAL]

Context:
- Used in [WHERE]
- Works with [DEPENDENCIES/FRAMEWORKS]
- Follows [PROJECT PATTERN]

Requirements:
- [CONSTRAINT 1]
- [CONSTRAINT 2]
- [CONSTRAINT 3]

Example of desired output:
[SAMPLE CODE/FORMAT]
```

### Example in Practice

❌ **Bad Prompt:**
```
Write a function to validate a password
```
- Vague requirements
- No context about standards
- No example of what "valid" means

✅ **Good Prompt:**
```
Write a password validation function for a web app authentication system.

Context:
- This is in a Node.js/Express backend
- Using TypeScript
- Part of user registration flow

Requirements:
- Minimum 8 characters
- Must include uppercase, lowercase, number, and special character
- Return boolean (true if valid)
- Throw error with descriptive message if invalid
- Include JSDoc comments

Example of desired behavior:
validatePassword("Pass123!") // true
validatePassword("weak") // throws Error("Password must be at least 8 characters")
```

---

## Zero-Shot vs. Few-Shot Prompting

### Zero-Shot (No Examples)
**When to use:** Straightforward requests, common patterns, simple tasks
```
Generate a function to calculate the factorial of a number in JavaScript
```
**Pros:** Faster, less context needed
**Cons:** May need refinement, might not match your style

### Few-Shot (With Examples)
**When to use:** Custom patterns, specific style, complex logic
```
Generate a function to calculate factorial, following this pattern:

// Pattern example - double asterisk for multiplication:
function double(n) {
  return n ** 2;
}

// Now generate factorial:
```
**Pros:** Better alignment with your code style, more accurate
**Cons:** More tokens used, takes slightly longer

### Multi-Shot (Multiple Examples)
**When to use:** Very specific patterns, custom domain logic
```
Generate a validator function following this pattern:

// Example 1: Email validator
const validateEmail = (email) => {
  if (!email.includes('@')) throw new Error('Invalid email format');
  return true;
};

// Example 2: Phone validator  
const validatePhone = (phone) => {
  if (!/^\d{10}$/.test(phone)) throw new Error('Phone must be 10 digits');
  return true;
};

// Example 3 (generate this): Password validator
```
**Pros:** Highest accuracy for custom patterns
**Cons:** Requires pre-work identifying patterns

---

## Context is King

### Types of Context Copilot Uses

1. **File Context** (Automatic)
   - Current file content
   - Surrounding code (above/below cursor)
   - File name and language
   
2. **Project Context** (Automatic)
   - Project structure
   - File names and structure
   - Open files in workspace

3. **Explicit Context** (You Provide)
   - `@file` mentions in chat
   - Code snippets in messages
   - Configuration files
   - Architecture documentation

### How to Maximize Context

**Do This:**
- ✅ Open relevant files before asking Copilot
- ✅ Reference existing patterns in your codebase
- ✅ Mention your tech stack early
- ✅ Include error messages if debugging
- ✅ Share configuration files relevant to the task

**Don't Do This:**
- ❌ Ask for code without showing current codebase style
- ❌ Forget to mention framework versions
- ❌ Leave out business logic context
- ❌ Ask in chat without opening related files

---

## Common Prompt Patterns

### Pattern 1: Refactoring Request
```
Refactor this function [PASTE CODE] to:
- Use async/await instead of promises
- Add error handling with try/catch
- Extract the [SPECIFIC PART] into a helper function
- Keep the same functionality

Current style in this project uses: [PASTE STYLE EXAMPLE]
```

### Pattern 2: Feature Implementation
```
Add a feature to [WHERE] that [WHAT].

This should:
- [REQUIREMENT 1]
- [REQUIREMENT 2]
- [REQUIREMENT 3]

Use this existing pattern:
[PASTE SIMILAR CODE]

Return type should match [EXISTING FUNCTION/TYPE]
```

### Pattern 3: Bug Fix
```
This code has a bug [DESCRIBE ISSUE]:
[PASTE CODE]

Error message: [PASTE ERROR]

Fix it by [SPECIFIC APPROACH] and add comments explaining the issue.
```

### Pattern 4: Code Review / Analysis
```
Review this code for [ISSUES]:
[PASTE CODE]

Check for:
- Security vulnerabilities
- Performance issues
- Error handling gaps
- Code style inconsistencies with [PROJECT STYLE]

Suggest specific improvements.
```

### Pattern 5: Learning / Understanding
```
Explain how this [FEATURE/PATTERN] works:
[PASTE CODE]

Focus on:
- Why it works this way
- Common pitfalls
- How to use it correctly
- When NOT to use it
```

---

## Iterative Refinement Strategy

When your first suggestion isn't quite right, use this process:

### Step 1: Analyze the Gap
```
That's close, but I need [WHAT'S DIFFERENT].

The issue is: [SPECIFIC PROBLEM]
```

### Step 2: Add Constraints
```
Can you add:
- [MISSING REQUIREMENT]
- [SPECIFIC FORMAT]
- [PERFORMANCE CONSTRAINT]

Also, make sure to [SPECIFIC INSTRUCTION]
```

### Step 3: Provide Example
```
I need it in this style:
[PASTE EXAMPLE]

Can you regenerate using that pattern?
```

### Step 4: Simplify or Expand
```
That's too [COMPLEX/SIMPLE]. 

Instead of [CURRENT APPROACH], use [ALTERNATIVE]
```

---

## Best Practices for Exam Questions

When you see a prompt engineering question on the exam, remember:

### Effective Prompt Characteristics
- ✅ **Specific** - Uses concrete terms, not vague language
- ✅ **Contextual** - Includes relevant framework, language, patterns
- ✅ **Constrained** - Defines what should/shouldn't do
- ✅ **Example-based** - Shows desired output format
- ✅ **Progressive** - Complex requests broken into steps

### Ineffective Prompt Characteristics
- ❌ **Vague** - "Write some code" with no specifics
- ❌ **Context-poor** - No mention of language/framework
- ❌ **Unconstrained** - No requirements or limits
- ❌ **Overwhelming** - Asks for 10 things at once
- ❌ **Contradictory** - Conflicting requirements

---

## Practice: Prompt Evaluation

For exam prep, you may see prompts that you need to evaluate. Ask:

1. **Is it specific?**
   - Does it clearly state what's needed?
   - Would a developer understand without asking clarifications?

2. **Is the context clear?**
   - Is the tech stack mentioned?
   - Are dependencies clear?
   - Are existing patterns referenced?

3. **Are constraints reasonable?**
   - Can all requirements be met?
   - Are they contradictory?
   - Are they testable?

4. **Will Copilot understand?**
   - Is the language precise (not colloquial)?
   - Are terms defined?
   - Could it be misinterpreted?

5. **Can the output be evaluated?**
   - Is success clear?
   - Are acceptance criteria defined?
   - Can we test the result?

---

## Exam Tips for Prompt Engineering Questions

### Question Type 1: "What's wrong with this prompt?"
- Look for vagueness, missing context, contradictions
- Check if it would produce multiple valid interpretations
- Verify if Copilot would have enough info to comply

### Question Type 2: "Which prompt is better?"
- Better prompts are more specific
- Better prompts include context
- Better prompts provide examples
- Better prompts have clearer constraints

### Question Type 3: "How would you improve this prompt?"
- Add specific constraints
- Include relevant context
- Provide examples of desired output
- Break complex requests into steps
- Clarify ambiguous terms

### Question Type 4: "What would Copilot suggest for this prompt?"
- Predict based on specificity level
- Consider what context is available
- Think about common interpretations
- Remember Copilot works with file context too

---

## Key Takeaways

1. **Structure matters** - Use consistent prompt format
2. **Specificity wins** - "Validate email with regex" beats "check emails"
3. **Context helps** - Show existing code patterns before asking
4. **Examples clarify** - Even one example improves results dramatically
5. **Constraints focus** - Define limits and requirements upfront
6. **Iterate when needed** - Follow-up prompts refine initial results
7. **Test always** - Validate generated code, don't just accept it
