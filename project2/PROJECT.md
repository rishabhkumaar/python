## 🎯 Software Requirements Specification (SRS)

### 📌 Project Title:

**The Perfect Guess — A Number Guessing Game**

---

### 🧾 1. Project Overview

**Description:**
A number-guessing game where the computer generates a random number, and the player attempts to guess it. Feedback such as "Higher" or "Lower" is given after each guess. The game includes difficulty settings, a scoring system, time tracking, leaderboard management, and optional GUI support.

**Objective:**
To create a modular, scalable, and interactive game that supports user feedback, records statistics, and enhances player engagement through difficulty, performance tracking, and optional GUI.

---

### ⚙️ 2. Functional Requirements

1. **Random Number Generator**

   * Use `random` module to generate numbers based on difficulty level.
   * Easy: 1–20
   * Medium: 1–100
   * Hard: 1–500

2. **Input System**

   * Accept player name
   * Accept guesses
   * Accept commands like `/hint` (optional)

3. **Guess Evaluation Logic**

   * Compare guess with the target number
   * Display “Higher” or “Lower” feedback
   * Track number of attempts

4. **Score System**

   * Base score affected by:

     * Number of attempts
     * Time taken
     * Difficulty multiplier

5. **Time Tracking**

   * Start timer at game begin
   * End timer when correct guess is made
   * Save total duration

6. **Leaderboard Management**

   * Save top scores per difficulty
   * Store: name, attempts, time, score
   * Load and display leaderboard at game start or end

7. **Data Storage**

   * Use JSON or CSV for saving game data
   * Load data at launch
   * Option to reset scores

8. **Difficulty Modes**

   * Easy: More attempts, hints
   * Medium: Moderate feedback
   * Hard: Limited hints, fewer attempts

9. **Hint System (Optional)**

   * One-time-use hint
   * Hint example: Divisibility, range clues

10. **GUI Support (Optional)**

    * Build interface using `tkinter` or `pygame`
    * Display input fields, results, and score table

---

### 📁 3. Non-Functional Requirements

1. **Usability**

   * Clear and beginner-friendly UI (text or graphical)
   * Descriptive error handling for invalid inputs

2. **Portability**

   * Cross-platform compatible (Windows/Linux/Mac)
   * Runs with Python 3.x

3. **Maintainability**

   * Modular code structure
   * Separation of concerns (game logic, UI, data)

4. **Scalability**

   * Allow more difficulty levels, player stats, or multiplayer in future

5. **Performance**

   * Fast load/save operations
   * Optimized for low system resources

---

### 🔐 4. Optional Enhancements

* Timer-based challenge mode
* Multiplayer (local turn-based)
* User accounts with persistent tracking
* Cloud score syncing (future)
* Audio feedback using `playsound` or `pygame.mixer`

---

### 📦 5. Tools & Technologies

| Component       | Technology                       |
| --------------- | -------------------------------- |
| Language        | Python 3.x                       |
| Randomization   | `random` module                  |
| Time tracking   | `time` module                    |
| File handling   | JSON, CSV                        |
| GUI             | `tkinter` or `pygame` (optional) |
| OS tools        | `os` module                      |
| Version Control | Git & GitHub                     |

---

### 🧪 6. Testing Plan

* Unit testing for:

  * Guess logic
  * Score calculations
  * Data saving/loading
* Manual testing for:

  * GUI input
  * Hint system
  * Leaderboard sorting

---

### 📊 7. Deliverables

* Python source files (`.py`)
* README.md with instructions
* `requirements.txt` (if using any external libraries)
* `scores.json` or similar for leaderboard
* Optional: GUI executable version using PyInstaller

---

### 📅 8. Timeline (Example)

| Week | Tasks                         |
| ---- | ----------------------------- |
| 1    | Core logic (guessing, input)  |
| 2    | Score system + time tracking  |
| 3    | File storage + leaderboard    |
| 4    | Add difficulty + hint system  |
| 5    | GUI integration (optional)    |
| 6    | Polish, test, finalize README |

---

### 🧑‍💻 9. Contributors

* **Rishabh Kumar** (Developer & Architect)
* Tools: VS Code, Python 3.12, Git

---