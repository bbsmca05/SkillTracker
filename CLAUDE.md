# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**SkillTracker** is a Streamlit-based web application for managing student registration for tuition classes. Students can register with their name, class, mobile number, and subject of study. Data is persisted in a MySQL database.

## Architecture

The project uses a simple three-layer architecture:

- **Presentation Layer** (`src/module1.py`): Streamlit UI handling user input and form submission
- **Application Layer** (`src/main.py`): Entry point (currently minimal)
- **Data Access Layer** (`src/StudentRegistrationDB.py`): MySQL database operations

**Key Design Points:**
- Form-based UI in Streamlit with real-time validation
- Direct database operations without ORM abstraction
- Simple insertion workflow without update/delete functionality yet

## Common Commands

### Running the Application

```bash
# Run the Streamlit app (serves on http://localhost:8501)
streamlit run src/module1.py
```

### Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run a specific test file
python -m pytest tests/test_main.py

# Run with verbose output
python -m pytest tests/ -v
```

### Installing Dependencies

```bash
# Install from requirements.txt
pip install -r requirements.txt
```

## Database Setup

The application requires a running MySQL server with the following configuration:

- **Host**: localhost (configured in `StudentRegistrationDB.py`)
- **User**: root
- **Database**: brijmysql
- **Table**: students (columns: student_name, class, mobile_number, subject)

**Note:** Database credentials are currently hardcoded in `StudentRegistrationDB.py`. Before deployment, move credentials to environment variables or a configuration file.

## Current Limitations & TODOs

- Database credentials are hardcoded (security concern)
- No update/delete functionality
- `tests/test_main.py` exists but is empty—tests need to be written
- No error handling for database connection failures
- No input validation for mobile number format
- Form validation is minimal (only checks for empty fields)

## Key Files to Know

| File | Purpose |
|------|---------|
| `src/module1.py` | Main Streamlit UI and form handling |
| `src/StudentRegistrationDB.py` | MySQL connection and data insertion functions |
| `src/main.py` | Application entry point |
| `tests/test_main.py` | Test file (currently empty) |
| `requirements.txt` | Python dependencies |
