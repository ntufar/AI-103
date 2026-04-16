#!/usr/bin/env python3
"""
Azure AI-103 Prompt Evaluation Trainer with Azure OpenAI
Generates scenario-based prompts and provides LLM-guided feedback.
Requires: AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_KEY, AZURE_OPENAI_DEPLOYMENT_NAME in .env
"""

import os
import sys
import textwrap
from typing import Optional

from dotenv import load_dotenv

try:
    from openai import AzureOpenAI
except ImportError:
    print("Error: OpenAI SDK not installed. Run: pip install openai")
    sys.exit(1)


def load_env() -> tuple[str, str, str, str]:
    """Load Azure OpenAI credentials from .env file."""
    load_dotenv()
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    key = os.getenv("AZURE_OPENAI_KEY")
    deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")

    if not endpoint or not key:
        raise ValueError(
            "AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_KEY must be set in .env file. "
            "See AZURE-SETUP.md for instructions."
        )

    return endpoint, key, deployment, api_version


SCENARIOS = [
    {
        "title": "Customer Feedback Summarizer",
        "goal": "Summarize feedback into 3 themes and list 3 recommended actions.",
        "sample_context": "Users complain about pricing and confusing onboarding, but praise support speed.",
        "rubric": [
            "Clear role and objective",
            "Structured output format",
            "Grounded in provided context",
            "Safety constraints present",
            "Concise and actionable",
        ],
    },
    {
        "title": "Support Ticket Triage",
        "goal": "Classify urgency and extract action items from a support message.",
        "sample_context": "Production API is returning 500 errors for 35 percent of requests.",
        "rubric": [
            "Explicit urgency categories",
            "Deterministic output schema",
            "No invented facts",
            "Error handling for missing details",
            "Operational clarity",
        ],
    },
]


def evaluate_prompt_with_ai(client: AzureOpenAI, user_prompt: str, rubric: list[str]) -> str:
    """Use Azure OpenAI to evaluate the user's prompt."""
    evaluation_request = f"""
You are an AI-103 exam expert. A student wrote this prompt:

---
{user_prompt}
---

Evaluate it against these criteria (score each 1-5):
{chr(10).join(f"  - {r}" for r in rubric)}

Provide:
1. A score for each criterion
2. Overall score (1-5)
3. Top 2 improvements

Be concise (under 150 words).
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": evaluation_request}],
            max_tokens=500,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error calling Azure OpenAI: {e}"


def generate_improved_prompt(client: AzureOpenAI, original_prompt: str) -> str:
    """Generate an improved version of the user's prompt."""
    improvement_request = f"""
You are an AI-103 exam expert. A student wrote this prompt:

---
{original_prompt}
---

Generate an IMPROVED version that:
1. Adds explicit role ("You are a...")
2. Specifies output format (JSON/bullets/table)
3. Includes constraints and safety guardrails
4. Is concise (under 150 words)

Return ONLY the improved prompt, no explanation.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": improvement_request}],
            max_tokens=500,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error calling Azure OpenAI: {e}"


def run_scenario(
    client: AzureOpenAI, scenario: dict, index: int
) -> tuple[int, str]:
    """Run a single scenario with AI feedback."""
    print("\n" + "=" * 70)
    print(f"Scenario {index}: {scenario['title']}")
    print("-" * 70)
    print(textwrap.fill(f"Goal: {scenario['goal']}", width=70))
    print(textwrap.fill(f"Context: {scenario['sample_context']}", width=70))

    print("\nRubric:")
    for criterion in scenario["rubric"]:
        print(f"  - {criterion}")

    print("\nWrite your prompt below (type 'END' on a new line when done):")
    print("-" * 70)

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    user_prompt = "\n".join(lines).strip()

    if not user_prompt:
        print("No prompt provided. Skipping.")
        return 0, ""

    print("\n" + "-" * 70)
    print("AI Evaluation:")
    print("-" * 70)

    evaluation = evaluate_prompt_with_ai(client, user_prompt, scenario["rubric"])
    print(evaluation)

    print("\n" + "-" * 70)
    print("AI-Generated Improvement:")
    print("-" * 70)

    improved = generate_improved_prompt(client, user_prompt)
    print(improved)

    # Score manually
    print("\n" + "-" * 70)
    while True:
        score_input = input("Your self-score (1-5): ").strip()
        if score_input.isdigit() and 1 <= int(score_input) <= 5:
            score = int(score_input)
            break
        print("Please enter a number between 1 and 5.")

    reflection = input("One improvement you'll make next: ").strip()

    return score, reflection


def main() -> None:
    print("AI-103 Prompt Evaluation Trainer with Azure OpenAI")
    print("=" * 70)
    print("This trainer uses Azure OpenAI to evaluate your prompts in real-time.")
    print()

    # Load credentials
    try:
        endpoint, key, deployment, api_version = load_env()
    except ValueError as e:
        print(f"Configuration error: {e}")
        sys.exit(1)

    # Initialize Azure OpenAI client
    try:
        client = AzureOpenAI(
            api_key=key,
            api_version=api_version,
            azure_endpoint=endpoint,
        )
        print("✓ Connected to Azure OpenAI\n")
    except Exception as e:
        print(f"Error connecting to Azure: {e}")
        sys.exit(1)

    input("Press Enter to start...")

    total_score = 0
    for idx, scenario in enumerate(SCENARIOS, start=1):
        score, reflection = run_scenario(client, scenario, idx)
        total_score += score

    print("\n" + "=" * 70)
    avg_score = total_score / len(SCENARIOS) if SCENARIOS else 0
    print(f"Final Average Score: {avg_score:.2f}/5")

    if avg_score >= 4.0:
        print("Readiness: STRONG - Focus on speed and consistency.")
    elif avg_score >= 3.0:
        print("Readiness: MEDIUM - Improve structure and grounding.")
    else:
        print("Readiness: NEEDS WORK - Revisit prompt fundamentals.")

    print("=" * 70)


if __name__ == "__main__":
    main()
