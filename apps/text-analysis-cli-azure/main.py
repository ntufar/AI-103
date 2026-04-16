#!/usr/bin/env python3
"""
Azure AI-103 Text Analysis with Azure AI Language
Performs sentiment analysis, entity extraction, and key phrase detection.
Requires: AZURE_LANGUAGE_ENDPOINT and AZURE_LANGUAGE_KEY in .env
"""

import argparse
import os
import pathlib
import sys
from typing import Optional

from dotenv import load_dotenv

# Optional rich for formatting
try:
    from rich.console import Console
    from rich.table import Table

    HAS_RICH = True
except ImportError:
    HAS_RICH = False

# Import Azure SDK
try:
    from azure.ai.textanalytics import TextAnalyticsClient
    from azure.core.credentials import AzureKeyCredential
except ImportError:
    print("Error: Azure SDK not installed. Run: pip install -r requirements-azure.txt")
    sys.exit(1)


def load_env() -> tuple[str, str]:
    """Load Azure credentials from .env file."""
    load_dotenv()
    endpoint = os.getenv("AZURE_LANGUAGE_ENDPOINT")
    key = os.getenv("AZURE_LANGUAGE_KEY")

    if not endpoint or not key:
        raise ValueError(
            "AZURE_LANGUAGE_ENDPOINT and AZURE_LANGUAGE_KEY must be set in .env file. "
            "See AZURE-SETUP.md for instructions."
        )

    return endpoint, key


def analyze_sentiment(client: TextAnalyticsClient, text: str) -> dict:
    """Analyze document-level sentiment."""
    try:
        result = client.analyze_sentiment(documents=[text], language="en")[0]
        return {
            "sentiment": result.sentiment,
            "positive_score": result.confidence_scores.positive,
            "neutral_score": result.confidence_scores.neutral,
            "negative_score": result.confidence_scores.negative,
        }
    except Exception as e:
        print(f"Sentiment analysis error: {e}")
        return {}


def extract_entities(client: TextAnalyticsClient, text: str) -> list[dict]:
    """Extract named entities (Person, Location, Organization, etc)."""
    try:
        result = client.recognize_entities(documents=[text], language="en")[0]
        entities = []
        for entity in result.entities:
            entities.append(
                {
                    "text": entity.text,
                    "category": entity.category,
                    "confidence": entity.confidence_score,
                }
            )
        return entities
    except Exception as e:
        print(f"Entity extraction error: {e}")
        return []


def extract_key_phrases(client: TextAnalyticsClient, text: str) -> list[str]:
    """Extract key phrases."""
    try:
        result = client.extract_key_phrases(documents=[text], language="en")[0]
        return list(result.key_phrases)
    except Exception as e:
        print(f"Key phrase extraction error: {e}")
        return []


def print_results_rich(
    sentiment: dict, entities: list[dict], phrases: list[str]
) -> None:
    """Pretty print results using rich."""
    console = Console()

    # Sentiment table
    table = Table(title="Sentiment Analysis")
    table.add_column("Metric")
    table.add_column("Score")
    if sentiment:
        table.add_row("Overall Sentiment", sentiment.get("sentiment", "N/A"))
        table.add_row("Positive", f"{sentiment.get('positive_score', 0):.3f}")
        table.add_row("Neutral", f"{sentiment.get('neutral_score', 0):.3f}")
        table.add_row("Negative", f"{sentiment.get('negative_score', 0):.3f}")
    console.print(table)

    # Entities table
    if entities:
        entity_table = Table(title="Named Entities")
        entity_table.add_column("Entity")
        entity_table.add_column("Category")
        entity_table.add_column("Confidence")
        for ent in entities:
            entity_table.add_row(ent["text"], ent["category"], f"{ent['confidence']:.3f}")
        console.print(entity_table)

    # Key phrases
    if phrases:
        console.print(f"\n[bold]Key Phrases:[/bold] {', '.join(phrases)}")


def print_results_plain(sentiment: dict, entities: list[dict], phrases: list[str]) -> None:
    """Print results in plain text."""
    print("Azure AI Language Analysis Results")
    print("=" * 50)

    if sentiment:
        print(f"Sentiment: {sentiment.get('sentiment', 'N/A')}")
        print(f"Positive: {sentiment.get('positive_score', 0):.3f}")
        print(f"Neutral: {sentiment.get('neutral_score', 0):.3f}")
        print(f"Negative: {sentiment.get('negative_score', 0):.3f}")
    print()

    if entities:
        print("Named Entities:")
        for ent in entities:
            print(f"  - {ent['text']} ({ent['category']}: {ent['confidence']:.3f})")
    print()

    if phrases:
        print(f"Key Phrases: {', '.join(phrases)}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Azure AI Language text analysis for AI-103 practice."
    )
    parser.add_argument("--input", required=True, help="Path to text file to analyze")
    args = parser.parse_args()

    # Load credentials
    try:
        endpoint, key = load_env()
    except ValueError as e:
        print(f"Configuration error: {e}")
        sys.exit(1)

    # Read input file
    file_path = pathlib.Path(args.input)
    if not file_path.exists():
        print(f"Error: Input file not found: {file_path}")
        sys.exit(1)

    text = file_path.read_text(encoding="utf-8")

    # Initialize client
    client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

    print("Analyzing text with Azure AI Language...")
    print()

    # Perform analyses
    sentiment = analyze_sentiment(client, text)
    entities = extract_entities(client, text)
    phrases = extract_key_phrases(client, text)

    # Print results
    if HAS_RICH:
        print_results_rich(sentiment, entities, phrases)
    else:
        print_results_plain(sentiment, entities, phrases)

    print()
    print("Practice task: Extend this to sentiment per sentence or entity linking.")


if __name__ == "__main__":
    main()
