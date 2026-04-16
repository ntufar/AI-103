# Prompt Engineering Quick Reference

## Prompt Template

Use this base format:

1. Role: "You are a..."
2. Goal: exact task to complete
3. Context: relevant source or facts
4. Constraints: style, length, output format, exclusions
5. Examples: optional but high-impact
6. Evaluation: what makes output successful

## Practical Pattern

- Start specific and structured
- Force output schema when possible (JSON/table/bullets)
- Add guardrails for unsupported requests
- Ask model to cite or indicate uncertainty when context is missing

## Quality Checks

- Correctness: facts are accurate
- Relevance: answers the user intent
- Groundedness: based on provided context
- Safety: avoids harmful or policy-violating output
- Consistency: stable format and tone

## Common Fixes

- Too vague output -> add explicit constraints and format
- Hallucinations -> provide context and require grounded answers
- Too verbose -> add token/length limits and required sections only
- Missed instruction -> move critical instruction to top and repeat once
