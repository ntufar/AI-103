import textwrap

SCENARIOS = [
    {
        "title": "Customer Feedback Summarizer",
        "goal": "Summarize feedback into 3 themes and list 3 recommended actions.",
        "rubric": [
            "Clear role and objective",
            "Structured output format",
            "Grounded in provided context",
            "Safety constraints present",
            "Concise and actionable",
        ],
        "sample_context": "Users complain about pricing and confusing onboarding, but praise support speed.",
    },
    {
        "title": "Support Ticket Triage",
        "goal": "Classify urgency and extract action items from a support message.",
        "rubric": [
            "Explicit urgency categories",
            "Deterministic output schema",
            "No invented facts",
            "Error handling for missing details",
            "Operational clarity",
        ],
        "sample_context": "Production API is returning 500 errors for 35 percent of requests.",
    },
]


def prompt_user(message: str) -> str:
    print(message)
    return input("> ").strip()


def score_prompt() -> int:
    while True:
        raw = prompt_user("Enter your score from 1 to 5:")
        if raw.isdigit() and 1 <= int(raw) <= 5:
            return int(raw)
        print("Please enter a whole number between 1 and 5.")


def run_scenario(item: dict, index: int) -> int:
    print("\n" + "=" * 70)
    print(f"Scenario {index}: {item['title']}")
    print("-" * 70)
    print(textwrap.fill(f"Goal: {item['goal']}", width=70))
    print(textwrap.fill(f"Context: {item['sample_context']}", width=70))

    print("\nRubric:")
    for criterion in item["rubric"]:
        print(f"- {criterion}")

    print("\nWrite your improved prompt in your notes/editor, then self-score.")
    score = score_prompt()

    reflection = prompt_user("What is the single biggest improvement you would make next?")
    print(f"Reflection saved: {reflection}")
    return score


def main() -> None:
    print("AI-103 Prompt Evaluation Trainer")
    print("Practice writing prompts, then grade yourself with a consistent rubric.")

    total = 0
    for idx, scenario in enumerate(SCENARIOS, start=1):
        total += run_scenario(scenario, idx)

    avg = total / len(SCENARIOS)
    print("\n" + "=" * 70)
    print(f"Final average score: {avg:.2f}/5")

    if avg >= 4.0:
        print("Readiness signal: strong. Focus on speed and consistency.")
    elif avg >= 3.0:
        print("Readiness signal: medium. Improve structure and grounding.")
    else:
        print("Readiness signal: needs work. Revisit quick-reference prompts.")


if __name__ == "__main__":
    main()
