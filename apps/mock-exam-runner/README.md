---
title: AI-103 Mock Exam Web App
tags: [exam, preparation, ai-103, web-app, interactive]
created: 2026-04-17
updated: 2026-04-17
type: guide
---

> 📌 **Navigation:** [[../../../GH-300-refresh/INDEX|← Back to Index]]

## Overview

The AI-103 Mock Exam Web App is a modern, interactive HTML/JavaScript application for practicing Azure AI Engineer Associate certification exam questions. It replaces the CLI Python version with a fully-featured browser-based exam simulator.

## Features

### ✓ Core Exam Features
- **10 randomized questions** from 5 knowledge domains
- **30-minute timed exam** with visual countdown timer
- **Instant feedback** on correct/incorrect answers
- **Answer review** before final submission
- **Progress tracking** with visual progress bar

### ✓ Enhanced User Experience
- **Beautiful gradient UI** with modern design
- **Responsive layout** works on desktop, tablet, mobile
- **Domain badges** show which area each question covers
- **Color-coded feedback** - green for correct, red for incorrect
- **Timer warnings** - yellow at 5 min, red at 1 min with pulse animation

### ✓ Score Management
- **Score breakdown by domain** - see your performance per area
- **Overall percentage score** with certification readiness status
- **Score history** - track your progress across multiple attempts
- **localStorage persistence** - history saves between sessions

### ✓ Navigation Features
- **Previous/Next buttons** to move between questions
- **Question counter** showing current position
- **Review screen** with all answers before submission
- **Ability to go back** and edit answers before review

## How to Use

### Quick Start

1. **Open the app** - Simply open `index.html` in any modern web browser
2. **Click "Start Exam"** - Begins a 30-minute timed session
3. **Answer questions** - Select an option (A/B/C/D) for each question
4. **Navigate freely** - Use Previous/Next buttons to review answers
5. **Submit exam** - Click "Review & Submit" on the last question
6. **Review answers** - Check all answers on the review screen
7. **Submit final** - Click "Submit Exam" to finalize and see results

### Question Flow

```
Welcome Screen
    ↓
    [Start Exam]
    ↓
Exam Screen (Questions 1-10)
    ↓
    [Previous/Next Navigation]
    ↓
    [Review & Submit on Last Question]
    ↓
Review Screen (All Answers)
    ↓
    [Submit Exam]
    ↓
Results Screen (Scores & History)
    ↓
    [Retake Exam or Go Home]
```

## Knowledge Domains

The exam covers 5 key domains with 2 questions each:

1. **Plan & Manage AI Solutions** - Service selection, indexing strategies, deployment
2. **Generative AI Solutions** - Prompt engineering, response optimization
3. **Natural Language Processing** - Confidence scoring, analysis metrics
4. **Computer Vision** - Image classification, threshold handling
5. **Knowledge Mining** - Search optimization, vector embeddings

## Score Interpretation

| Score | Status | Meaning |
|-------|--------|---------|
| 80-100% | **EXAM READY ✓** | Prepared for certification |
| 70-79% | **SOLID FOUNDATION** | Review weak domains before exam |
| 60-69% | **NEEDS WORK** | Focused prep required |
| Below 60% | **REVIEW FUNDAMENTALS** | More study needed |

## Technical Details

### Browser Compatibility
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile)

### Technology Stack
- **Pure HTML5** - No dependencies
- **Vanilla JavaScript** - No frameworks needed
- **localStorage** - Browser persistence
- **CSS3 Animations** - Smooth interactions

### File Structure
```
mock-exam-runner/
├── index.html          # Complete web app (HTML + CSS + JS)
├── main.py            # Original Python CLI version
└── README.md          # This file
```

## Features Detail

### Timer Management
- Displays remaining time in MM:SS format
- Auto-advances to review if time expires
- Visual warnings:
  - Yellow background at 5 minutes
  - Red background + pulse at 1 minute

### Answer Review
- Shows all questions with your answers
- Highlights correct answers in green
- Shows incorrect answers in red
- Displays correct answer option for reference
- Sort by domain for learning

### Score History
- Last 10 exam attempts stored
- Shows date, score, and correct/total count
- Clear History button to reset
- Persists across browser sessions

### Responsive Design
- **Desktop** - Full sidebar view (if added)
- **Tablet** - Optimized grid layout
- **Mobile** - Single column, touch-friendly buttons

## Tips for Exam Prep

1. **Take full 30-minute exams** - Don't skip time constraints
2. **Review weak domains** - Focus on areas scoring <80%
3. **Retake multiple times** - Aim to increase score with each attempt
4. **Track your progress** - Use score history to monitor improvement
5. **Time management** - With 10 questions in 30 min = 3 min per question

## Troubleshooting

### Score History Not Saving
- Check if localStorage is enabled in browser settings
- Clear browser cache and try again
- Some browsers disable storage in private mode

### Timer Issues
- Ensure browser system time is correct
- Close other tabs that may consume resources
- Refresh page to reset timer

### Display Issues on Mobile
- Rotate to landscape for better view
- Use Chrome or Safari (best performance)
- Zoom may need adjustment - pinch to fit

## Future Enhancements

Potential features to add:
- [ ] Adjustable time limits
- [ ] Question difficulty levels
- [ ] Explanations for each answer
- [ ] Spaced repetition scheduling
- [ ] Export results as PDF
- [ ] Compare scores across attempts
- [ ] Dark mode toggle
- [ ] Bookmark questions for later review

## Development Notes

The application is built as a **single HTML file** for maximum portability. All code (HTML, CSS, JavaScript) is embedded and self-contained. To modify:

1. **Add questions** - Edit the `QUESTIONS` object in `<script>` section
2. **Change time limit** - Modify `timeLimit: 30 * 60` value
3. **Customize styling** - Edit CSS in `<style>` section
4. **Adjust question count** - Add/remove questions from each domain

## Version History

- **v1.0** (April 17, 2026) - Initial web app release
  - Complete exam flow with timer
  - Answer review before submission
  - Score history with localStorage
  - Responsive design
  - All 10 original questions

---

**Last Updated:** April 17, 2026  
**Version:** 1.0  
**Status:** Ready for use
