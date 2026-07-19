# Quizzler 🧠

A desktop trivia quiz app built with Python and Tkinter. Questions are pulled live from the [Open Trivia Database](https://opentdb.com/) API, so the quiz content is never hardcoded, every playthrough can pull fresh questions.

## Features

- Fetches multiple-choice/true-false trivia questions in real time via API
- Clean Tkinter GUI with True/False answer buttons
- Running score tracker displayed on-screen
- Handles HTML-encoded characters in question text (e.g. `&quot;`, `&#039;`)

## How It Works

1. On launch, the app requests a batch of questions from the Open Trivia DB API.
2. Each question is displayed one at a time in the GUI.
3. The user selects **True** or **False**.
4. The app checks the answer, shows feedback, and updates the score.
5. Once all questions are answered, the quiz ends and displays the final score.

## Tech Stack

- **Python 3**
- **Tkinter** — GUI framework
- **Requests** — API calls to Open Trivia DB
- **html** — decoding HTML entities in question strings

## Project Structure

```
quizzler-app/
├── main.py             # Entry point — sets up the GUI window
├── ui.py               # GUI with Tkinter
├── quiz_brain.py       # Core quiz logic (scoring, question flow)
├── question_model.py   # Question class/data structure
├── data.py             # Handles the API request to Open Trivia DB
└── README.md
```
