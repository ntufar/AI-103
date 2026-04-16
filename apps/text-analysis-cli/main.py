import argparse
import pathlib
import re
from collections import Counter

try:
    from rich.console import Console
    from rich.table import Table
except Exception:
    Console = None
    Table = None

POSITIVE_WORDS = {
    "love",
    "great",
    "good",
    "quick",
    "helpful",
    "useful",
    "excellent",
    "fast",
    "fixed",
}

NEGATIVE_WORDS = {
    "crash",
    "crashes",
    "bad",
    "high",
    "confusing",
    "missing",
    "irrelevant",
    "slow",
    "error",
}


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-zA-Z']+", text.lower())


def sentence_split(text: str) -> list[str]:
    parts = re.split(r"[.!?]+", text)
    return [p.strip() for p in parts if p.strip()]


def simple_sentiment_score(tokens: list[str]) -> int:
    pos = sum(1 for t in tokens if t in POSITIVE_WORDS)
    neg = sum(1 for t in tokens if t in NEGATIVE_WORDS)
    return pos - neg


def classify_sentiment(score: int) -> str:
    if score > 1:
        return "Positive"
    if score < -1:
        return "Negative"
    return "Neutral"


def extract_top_keywords(tokens: list[str], top_n: int = 8) -> list[tuple[str, int]]:
    stopwords = {
        "the", "a", "an", "and", "or", "of", "to", "for", "with", "is", "are", "was",
        "were", "i", "you", "it", "my", "your", "but", "on", "in", "this", "that", "too",
    }
    filtered = [t for t in tokens if len(t) > 2 and t not in stopwords]
    return Counter(filtered).most_common(top_n)


def print_plain(summary: dict) -> None:
    print("AI-103 Text Analysis Practice")
    print("=" * 32)
    print(f"Characters: {summary['characters']}")
    print(f"Words: {summary['words']}")
    print(f"Sentences: {summary['sentences']}")
    print(f"Sentiment Score: {summary['sentiment_score']}")
    print(f"Sentiment Label: {summary['sentiment_label']}")
    print("Top Keywords:")
    for word, count in summary["keywords"]:
        print(f"- {word}: {count}")


def print_rich(summary: dict) -> None:
    console = Console()
    table = Table(title="AI-103 Text Analysis Practice")
    table.add_column("Metric")
    table.add_column("Value")
    table.add_row("Characters", str(summary["characters"]))
    table.add_row("Words", str(summary["words"]))
    table.add_row("Sentences", str(summary["sentences"]))
    table.add_row("Sentiment Score", str(summary["sentiment_score"]))
    table.add_row("Sentiment Label", summary["sentiment_label"])
    console.print(table)

    kw_table = Table(title="Top Keywords")
    kw_table.add_column("Keyword")
    kw_table.add_column("Count")
    for word, count in summary["keywords"]:
        kw_table.add_row(word, str(count))
    console.print(kw_table)


def main() -> None:
    parser = argparse.ArgumentParser(description="Local text-analysis practice app for AI-103 prep.")
    parser.add_argument("--input", required=True, help="Path to a text file to analyze")
    args = parser.parse_args()

    file_path = pathlib.Path(args.input)
    if not file_path.exists():
        raise SystemExit(f"Input file not found: {file_path}")

    text = file_path.read_text(encoding="utf-8")
    tokens = tokenize(text)
    sentences = sentence_split(text)
    score = simple_sentiment_score(tokens)

    summary = {
        "characters": len(text),
        "words": len(tokens),
        "sentences": len(sentences),
        "sentiment_score": score,
        "sentiment_label": classify_sentiment(score),
        "keywords": extract_top_keywords(tokens),
    }

    if Console and Table:
        print_rich(summary)
    else:
        print_plain(summary)

    print("\nPractice task: extend this script with entity extraction or summarization logic.")


if __name__ == "__main__":
    main()
