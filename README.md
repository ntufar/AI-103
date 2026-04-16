# AI-103 Certification Prep Workspace

This repository is a complete preparation kit for **Microsoft AI-103** exam practice.

It includes:
- Study guides with an exam-focused roadmap
- Quick reference sheets for fast revision
- 55+ question mock exam with timed runner and scoring
- Runnable practice apps (local and Azure-connected versions)
- Self-grading rubrics and checkpoints

## Recommended Study Flow

1. Read `study-guides/exam-objectives-map.md` to understand what is covered.
2. Follow `study-guides/30-day-plan.md` day by day.
3. Use `quick-reference/` before each practice session.
4. Complete each lab in `labs/` and score yourself using `labs/scorecard.md`.
5. Run mock exams in `apps/mock-exam-runner/` to assess readiness.
6. Run and modify apps in `apps/` for hands-on confidence.

## Project Structure

- `study-guides/` - structured learning and study plan
- `quick-reference/` - concise, high-yield cheat sheets
- `labs/` - guided tasks with grading rubrics and scorecard
- `labs/mock-exam-questions.md` - 55+ questions across all AI-103 domains
- `apps/` - runnable Python practice apps (local and Azure versions)
- `data/sample-inputs/` - sample text and prompts for exercises

## Quick Start

### 1) Create and activate a virtual environment (recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Run the mock exam

```bash
python apps/mock-exam-runner/main.py
```

### 4) Run local text analysis CLI

```bash
python apps/text-analysis-cli/main.py --input data/sample-inputs/customer-feedback.txt
```

### 5) Run local prompt evaluation trainer

```bash
python apps/prompt-eval-trainer/main.py
```

## Azure-Connected Apps (Optional)

To use Azure AI services for real cloud practice:

1. Read `AZURE-SETUP.md` for credential setup
2. Install Azure dependencies: `pip install -r requirements-azure.txt`
3. Add `.env` file with Azure resource details (see `AZURE-SETUP.md` template)
4. Run Azure text analysis: `python apps/text-analysis-cli-azure/main.py --input data/sample-inputs/customer-feedback.txt`
5. Run Azure OpenAI prompt trainer: `python apps/prompt-eval-trainer-azure/main.py`

## Practice Rules

- Timebox exercises like exam conditions.
- Write your answers first, then compare with references.
- Use mock exam every week to track progress.
- Track scores in `labs/scorecard.md` after each session.
- Revisit weak domains every 3-4 days.

## Success Checklist

- [ ] 80%+ on two consecutive mock exams
- [ ] Consistent lab scores 4/5 or higher
- [ ] Can justify architectural choices in <2 minutes
- [ ] Understand trade-offs: cost, latency, quality, risk
- [ ] Reviewed all quick-reference sheets

## Files Overview

| File | Purpose |
|------|---------|
| `study-guides/exam-objectives-map.md` | AI-103 domains and learning outcomes |
| `study-guides/30-day-plan.md` | Weekly study schedule |
| `quick-reference/azure-ai-services.md` | Service selection decision tree |
| `quick-reference/prompt-engineering.md` | Prompt best practices and patterns |
| `quick-reference/responsible-ai-checklist.md` | Safety and governance checklist |
| `labs/lab-01-solution-design.md` | Architecture scenario tasks |
| `labs/lab-02-prompt-engineering.md` | Prompt refinement and grading |
| `labs/lab-03-nlp-vision-search.md` | Integrated capability mapping |
| `labs/mock-exam-questions.md` | 55+ practice questions with answers |
| `labs/scorecard.md` | Progress tracker |
| `apps/mock-exam-runner/main.py` | Timed mock exam simulator |
| `apps/text-analysis-cli/main.py` | Local text analysis (sentiment, entities, phrases) |
| `apps/prompt-eval-trainer/main.py` | Local prompt evaluation with self-scoring |
| `apps/text-analysis-cli-azure/main.py` | Azure Language service integration |
| `apps/prompt-eval-trainer-azure/main.py` | Azure OpenAI integration |
| `AZURE-SETUP.md` | Azure resource setup guide |
| `requirements.txt` | Python dependencies (local apps) |
| `requirements-azure.txt` | Python dependencies (Azure apps) |

## Notes

- Local apps run entirely offline without cloud credentials.
- Azure apps require valid subscriptions and API keys.
- Extend apps to add custom features (e.g., multi-language support, advanced metrics).
- Use mock exam as a diagnostic tool to identify weak domains.

