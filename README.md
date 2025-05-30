#  COMLIE Fitness Tracker

COMLIE Fitness Tracker is a command-line based application designed to help users track their fitness journey. Users can log workouts, track progress on different exercises, and manage their workout data using an interactive CLI built with Python, SQLAlchemy, and Alembic.

---

## Project Structure

.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── cli.py
    ├── db
    │   ├── models.py
    │   └── seed.py
    ├── debug.py
    └── helpers.py

---

## Features

- Add and list users with unique emails
- Add and list exercises
- Log workouts by date and user
- Track exercises in each workout
- Record and update personal bests (progress) per exercise
- View full progress history per user
- Simple and clean CLI interface

---

## Technologies Used

- **Python 3**
- **SQLAlchemy** (ORM)
- **Alembic** (Migrations)
- **Click** (CLI Framework)
- **Pipenv** (Virtual Environment & Dependency Manager)
- **SQLite** (Database)

---

##  Getting Started

### 1. Clone the Repository

```bash
git clone git@github.com:LeslieKogi/COMLIE-FITNESS-TRAKCER.git
cd COMLIE-Fitness-Tracker
```

### 2. Install Dependencies
Make sure pipenv is installed. Then:

pipenv install
pipenv shell

### 3. Initialize the Database

python lib/cli.py init-db

## Commands Overview
All commands are run using:

python lib/cli.py [command] [arguments]

### Team members
Collins Kipngeno
Leslie Kogi
Milka Muthoni
