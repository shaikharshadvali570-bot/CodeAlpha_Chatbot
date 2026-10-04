# PyChat — Basic Rule-Based Chatbot

## Overview
PyChat is a lightweight, console-based rule-driven chatbot developed using Python. It matches user inputs against predefined conversation patterns to return appropriate responses for greetings, identity queries, help requests, and exit commands.

> **Note:** This is a deterministic, rule-based program designed to demonstrate fundamental programming constructs. It does **not** use machine learning, neural networks, external APIs, or generative AI.

---

## Features
- **Interactive Console Session:** Continuous chat loop running directly inside the terminal.
- **Text Normalization:** Handles case differences (`.lower()`), extra whitespace (`.strip()`), and common ending punctuation (`.rstrip(".!?")`).
- **Predefined Rule Mapping:** Accurately recognizes greetings, identity inquiries, well-being checks, and gratitude.
- **Graceful Error & Edge Handling:** Manages empty lines without crashing and delivers friendly fallback responses for unknown queries.
- **Clean Exit Termination:** Supports `bye`, `goodbye`, `exit`, and `quit`.

---

## Technologies
- **Language:** Python 3.x
- **Libraries:** Python Standard Library only (no external packages)

---

## Concepts Demonstrated
- **Control Flow:** `if-elif-else` conditional evaluation.
- **Looping:** `while True` loop managing real-time session state.
- **Functions & Modularity:** Separation of display, text cleaning, rule evaluation, and main loop.
- **String Manipulation:** Methods such as `.lower()`, `.strip()`, and `.rstrip()`.
- **Standard I/O:** `input()` and formatted `print()`.

---

## How It Works

```
User Input ("  Hello!  ")
        │
        ▼
Input Normalization (.strip(), .lower(), .rstrip()) ➔ "hello"
        │
        ▼
Rule Matching (if-elif-else lookup)
        │
        ▼
Predefined Response Selected ("Hi! Nice to meet you.")
        │
        ▼
Output Displayed to Console
```

---

## Project Structure

```
pychat-rule-based-chatbot/
│
├── chatbot.py          # Main application code
├── requirements.txt    # Dependency notes (none required)
└── README.md           # Documentation and usage guide
```

---

## How to Run

1. Clone or download this repository.
2. Open a terminal inside the project directory:
   ```bash
   python chatbot.py
   ```
   (No virtual environment or `pip install` steps are required.)

---

## Sample Console Interaction

```
==================================================
             PyChat - Python Chatbot
==================================================

Hello! I'm PyChat, a simple rule-based chatbot.
Type "help" to see what I can do.
Type "bye" or "exit" to quit.

--------------------------------------------------

You: hello

PyChat: Hi! Nice to meet you.

You:    HELLO!

PyChat: Hi! Nice to meet you.

You: how are you?

PyChat: I'm fine, thanks! How can I help you today?

You: what is your name

PyChat: I'm PyChat, a simple Python rule-based chatbot.

You:

PyChat: Please type something so I can respond.

You: what is the weather today

PyChat: I'm not sure how to respond to that. Try typing "help" to see what I can do.

You: help

PyChat: I can respond to greetings, introduce myself, and answer a few basic questions.
Type "commands" to view a list of recognized topics.

You: thank you

PyChat: You're welcome!

You: bye!

PyChat: Goodbye! Have a great day!

==================================================
              Chat session ended
==================================================
```

---

## Testing Confirmation

The script satisfies all 11 required verification checks:

| # | Test Case | Sample Input | Handled Logic / Output | Status |
|---|-----------|--------------|------------------------|--------|
| 1 | Greeting | `hello` | Matches "hello" → "Hi! Nice to meet you." | Passed |
| 2 | Uppercase Input | `HELLO` | `.lower()` transforms to "hello" | Passed |
| 3 | Whitespace | `   hello   ` | `.strip()` removes outer whitespace | Passed |
| 4 | How Are You | `how are you?` | `.rstrip(".!?")` trims `?` → matches rule | Passed |
| 5 | Name Query | `what is your name` | Matches "what is your name" | Passed |
| 6 | Help | `help` | Outputs capabilities and points to "commands" | Passed |
| 7 | Thanks | `thank you` | Matches "thank you" → "You're welcome!" | Passed |
| 8 | Unknown Input | `tell me a joke` | Fallback branch reached without errors | Passed |
| 9 | Empty Input | `[Enter]` | Prompts user to type without crashing | Passed |
| 10 | Exit | `bye` | Sets `should_exit = True`, exits loop cleanly | Passed |
| 11 | Alternative Exits | `quit`, `exit`, `goodbye` | All mapped to termination branch | Passed |