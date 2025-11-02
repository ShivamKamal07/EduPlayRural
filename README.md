# EduPlayRural

EduPlayRural ek web-based educational app hai jo rural students ke liye subjects, quizzes, progress tracking, smart notebook, leaderboard, chatbot aur bhi bahut kuch access karna aasan banata hai. Dashboard Hindi aur English dono languages support karta hai aur students ke liye ek personalized learning experience provide karta hai.

## Features

- **User Dashboard:** Personalized welcome, class info, board, language, and selected subjects.
- **Profile Management:** Roll number, father/guardian name, mobile, address, school details.
- **Subjects & Progress Tracking:** Hindi, English, Math, Science jaise subjects me progress dekh sakte hain.
- **Quizzes:** Self-assessment ke liye interactive quizzes.
- **Progress Tracker:** Apne progress ko real time me dekhein.
- **Smart Notebook:** Digital notebook.
- **Leaderboard:** Peer competition ke liye rankings.
- **Chatbot:** AI based help aur support ke liye.

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript, WordPress (frontend focus)
- **Backend:** Python (`manage.py` aur structure dekh ke shayad Django/Flask)
- **Database:** SQLite (`db.sqlite3`)
- **Templates & Static Files:** `/templates` aur `/static`
- **Virtual Environment:** Python dependencies ke liye `/venv`

## Project Structure


## Getting Started

### Prerequisites

- Python 3.x
- pip
- (Optional) venv
- Node.js & npm (agar frontend ke liye use ho raha ho)

### Installation

1. **Clone the repository:**
    ```
    git clone <repo-url>
    cd EduPlayRural
    ```

2. **Virtual environment setup:**
    ```
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Linux/Mac:
    source venv/bin/activate
    ```

3. **Dependencies install karo:**
    ```
    pip install -r requirements.txt
    ```

4. **Run database migrations (agar Django hai):**
    ```
    python manage.py migrate
    ```

5. **Start development server:**
    ```
    python manage.py runserver
    ```

6. **App access:**
    open your browser and copy paste your `http://localhost:8000`







