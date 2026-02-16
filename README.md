# Software Engineering for Data Scientists — Data Dashboard Project

This repository contains the completed code for the Software Engineering for Data Scientists final project (Data Dashboard). It includes:
- a Python package (`employee_events`) that queries a SQLite database
- a dashboard app (`report/dashboard.py`)
- automated tests (`pytest`)
- CI workflows (GitHub Actions: Tests + Lint)

---

## Repository Structure

    ├── README.md
    ├── assets
    │   ├── model.pkl
    │   └── report.css
    ├── python-package
    │   ├── dist
    │   │   ├── employee_events-0.0.tar.gz
    │   │   └── employee_events-0.0-py3-none-any.whl
    │   ├── employee_events
    │   │   ├── __init__.py
    │   │   ├── employee.py
    │   │   ├── employee_events.db
    │   │   ├── query_base.py
    │   │   ├── sql_execution.py
    │   │   └── team.py
    │   ├── requirements.txt
    │   └── setup.py
    ├── report
    │   ├── base_components
    │   │   ├── __init__.py
    │   │   ├── base_component.py
    │   │   ├── data_table.py
    │   │   ├── dropdown.py
    │   │   ├── matplotlib_viz.py
    │   │   └── radio.py
    │   ├── combined_components
    │   │   ├── __init__.py
    │   │   ├── combined_component.py
    │   │   └── form_group.py
    │   ├── dashboard.py
    │   └── utils.py
    ├── requirements.txt
    ├── tests
    │   └── test_employee_events.py
    └── .github
        └── workflows
            ├── lint.yml
            └── test.yml

---

## Setup and Run (Reproducible)

### 1) Create and activate a virtual environment

Windows (PowerShell)
~~~
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
~~~
Mac/Linux

    python3 -m venv .venv
    source .venv/bin/activate

### 2) Install dependencies

    pip install -r requirements.txt

### 3) Install the package (editable)

    pip install -e python-package

### 4) Run tests

    pytest -q

### 5) Run the dashboard

    python report/dashboard.py

The app will print a local URL (usually `http://127.0.0.1:...`). Open it in your browser.

---

## Database: `employee_events.db`

The SQLite database is located at:

- `python-package/employee_events/employee_events.db`

High-level tables:

- `employee` (`employee_id`, `first_name`, `last_name`, `team_id`)
- `team` (`team_id`, `team_name`, `shift`, `manager_name`)
- `employee_events` (`event_date`, `employee_id`, `team_id`, `positive_events`, `negative_events`)
- `notes` (`employee_id`, `team_id`, `note`, `note_date`)

---

## CI (GitHub Actions)

This repo includes workflows that run automatically on pushes/pull requests to `main`:

- **Tests**: runs `pytest`
- **Lint**: runs `flake8` (relaxed rules for this project)
