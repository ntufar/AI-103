#!/usr/bin/env python3
"""
AI-103 Mock Exam Runner
Simulates timed exam conditions with instant grading and score breakdown by domain.
"""

import json
import pathlib
import time
import sys

# Question bank structured by domain
QUESTIONS = {
    "Plan & Manage AI Solutions": [
        {
            "id": 1,
            "text": "A startup needs to build a chatbot for FAQ automation. Which service is the primary choice?",
            "options": ["Azure AI Language", "Azure OpenAI Service", "Azure AI Vision", "Azure AI Speech"],
            "correct": 1,
        },
        {
            "id": 2,
            "text": "Your company processes 10M customer support tickets with unstructured text. Which indexing strategy minimizes latency while maintaining recall?",
            "options": [
                "Full-text search only",
                "Vector embeddings with semantic ranking",
                "Keyword search with BM25",
                "Regex pattern matching",
            ],
            "correct": 1,
        },
        {
            "id": 3,
            "text": "A manufacturing plant requires OCR on equipment photos daily. Latency must be <100ms per image. What is the best deployment?",
            "options": [
                "Batch processing in Logic App",
                "Real-time calls to Azure AI Vision",
                "Edge deployment with Docker container",
                "Store images and process weekly",
            ],
            "correct": 2,
        },
    ],
    "Generative AI Solutions": [
        {
            "id": 16,
            "text": "You need a model to extract action items from meeting notes. Which prompt structure is most effective?",
            "options": [
                "Extract action items.",
                "You are an AI assistant. Extract action items. Return JSON with {person, task, deadline}.",
                "Extract action items. Ignore unclear items. Return only confirmed tasks.",
                "Options B and C combined",
            ],
            "correct": 3,
        },
        {
            "id": 17,
            "text": "A prompt produces verbose 2000+ token responses when you need <200 tokens. Which fix is most direct?",
            "options": [
                "Use a cheaper model",
                "Add 'Response must be under 200 tokens. If too complex, say Too complex.'",
                "Fine-tune the model",
                "Truncate responses after 200 tokens",
            ],
            "correct": 1,
        },
    ],
    "Natural Language Processing": [
        {
            "id": 31,
            "text": "You analyze 50,000 customer reviews: 60% positive, 20% negative, 20% neutral. Which metric tells you confidence?",
            "options": [
                "Raw percentages",
                "Confidence scores per document; some predictions are <60% certain",
                "Average star rating",
                "Review length",
            ],
            "correct": 1,
        },
    ],
    "Computer Vision": [
        {
            "id": 39,
            "text": "Image analysis returns: dog (0.98), animal (0.95), pet (0.88), cat (0.45). Photo contains a cat, not dog. What happened?",
            "options": [
                "Model is broken",
                "Model trained on more dog data; threshold at 0.50+ filters false dog tag",
                "Use vision-language models instead",
                "Increase confidence threshold to 0.99",
            ],
            "correct": 1,
        },
    ],
    "Knowledge Mining": [
        {
            "id": 44,
            "text": "You index 10,000 documents averaging 5KB each. Search latency is 500ms. Expected improvement from vector search with semantic ranking?",
            "options": [
                "No improvement",
                "20-30% latency improvement; allows semantic relevance ranking",
                "10x improvement guaranteed",
                "Latency increases",
            ],
            "correct": 1,
        },
    ],
}


def print_header(text: str) -> None:
    print("\n" + "=" * 70)
    print(text.center(70))
    print("=" * 70 + "\n")


def run_exam(questions_per_domain: int = 2, time_limit_seconds: int = 1800) -> dict:
    """Run a timed mock exam."""
    print_header("AI-103 Mock Exam")
    print(f"Instructions: Answer {sum(len(q) for q in QUESTIONS.values())//len(QUESTIONS)} questions per domain.")
    print(f"Time limit: {time_limit_seconds // 60} minutes.")
    print("Type your answer (A/B/C/D or 0/1/2/3).\n")

    input("Press Enter to start...")

    start_time = time.time()
    results = {}
    total_correct = 0
    total_questions = 0

    for domain, questions in QUESTIONS.items():
        print_header(domain)
        domain_correct = 0

        for i, q in enumerate(questions[:questions_per_domain], start=1):
            elapsed = time.time() - start_time
            remaining = time_limit_seconds - elapsed

            if remaining <= 0:
                print("\nTime's up!")
                return results

            print(f"Question {i}/{questions_per_domain} (ID: {q['id']}) - {int(remaining)} seconds remaining")
            print(q["text"])
            print()

            for idx, opt in enumerate(q["options"]):
                label = chr(65 + idx)  # A, B, C, D
                print(f"  {label}) {opt}")
            print()

            while True:
                user_input = input("Your answer (A/B/C/D): ").strip().upper()
                if user_input in ["A", "B", "C", "D"]:
                    user_answer = ord(user_input) - 65
                    break
                elif user_input in ["0", "1", "2", "3"]:
                    user_answer = int(user_input)
                    break
                else:
                    print("Invalid input. Please enter A, B, C, or D.")

            is_correct = user_answer == q["correct"]
            if is_correct:
                domain_correct += 1
                total_correct += 1
                print("✓ Correct!\n")
            else:
                print(f"✗ Incorrect. Correct answer: {chr(65 + q['correct'])}\n")

            total_questions += 1

        results[domain] = {"correct": domain_correct, "total": min(len(questions), questions_per_domain)}

    print_header("Exam Complete")
    return results


def print_score_report(results: dict) -> None:
    """Print detailed score report by domain."""
    print("Score Breakdown by Domain:\n")
    total_correct = 0
    total_questions = 0

    for domain, scores in results.items():
        correct = scores["correct"]
        total = scores["total"]
        percentage = (correct / total * 100) if total > 0 else 0
        total_correct += correct
        total_questions += total

        status = "✓" if percentage >= 80 else "!" if percentage >= 60 else "✗"
        print(f"{status} {domain}: {correct}/{total} ({percentage:.1f}%)")

    print()
    overall_percentage = (total_correct / total_questions * 100) if total_questions > 0 else 0
    print(f"Overall Score: {total_correct}/{total_questions} ({overall_percentage:.1f}%)")
    print()

    if overall_percentage >= 80:
        print("Status: EXAM READY ✓")
    elif overall_percentage >= 70:
        print("Status: SOLID FOUNDATION - Review weak domains")
    elif overall_percentage >= 60:
        print("Status: NEEDS WORK - Focused prep required")
    else:
        print("Status: REVIEW FUNDAMENTALS - More study needed")


def main() -> None:
    try:
        # For testing: use 5 min, 2 questions per domain
        results = run_exam(questions_per_domain=2, time_limit_seconds=300)
        print_score_report(results)
    except KeyboardInterrupt:
        print("\nExam cancelled.")
        sys.exit(0)


if __name__ == "__main__":
    main()
