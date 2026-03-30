# DjangoCRUD

A backend Django application demonstrating **CRUD operations**, **ORM relationships**, and **database model design** with PostgreSQL.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2-092E20?style=flat&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Aiven%20Cloud-4169E1?style=flat&logo=postgresql&logoColor=white)
![Flake8](https://img.shields.io/badge/Linted%20with-Flake8-brightgreen?style=flat)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Data Models](#data-models)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [ORM Query Examples](#orm-query-examples)
- [Code Quality](#code-quality)

---

## Overview

DjangoCRUD is a backend-only Django project that showcases:

- **Model design** using Django ORM — single-table, multi-table inheritance, and many-to-many relationships
- **CRUD operations** — creating, reading, updating, and deleting records via scripts
- **Advanced ORM queries** — filtering, excluding, chaining, and field lookups
- **PostgreSQL integration** — cloud-hosted database via [Aiven](https://aiven.io/)
- **Environment-based configuration** — secrets and connection strings managed with `python-dotenv`

This project is built as a demonstration of backend data engineering skills rather than a web-facing application — there are no views, templates, or URL routes.

---

## Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.x** | Primary programming language |
| **Django 4.2** | Web framework / ORM |
| **PostgreSQL** | Relational database |
| **psycopg2** | PostgreSQL adapter for Python |
| **python-dotenv** | Environment variable management |
| **Aiven Cloud** | Managed cloud PostgreSQL hosting |
| **Flake8** | PEP 8 linting and code style enforcement |

---

## Features

- ✅ **Multi-table model inheritance** — `Instructor` and `Learner` both inherit from a base `User` model
- ✅ **Many-to-many relationships** — `Course` ↔ `Instructor` and `Course` ↔ `Learner` (via `Enrollment` through-model)
- ✅ **Foreign key relationships** — `Lesson` belongs to a `Course`; `Enrollment` links `Learner` and `Course`
- ✅ **Choice fields** — `Learner.occupation` and `Enrollment.mode` use typed constant choices
- ✅ **Timezone-aware defaults** — `Enrollment.date_enrolled` defaults to the current timestamp via `django.utils.timezone.now`
- ✅ **Database migrations** — Clean initial migration generated with Django's migration framework
- ✅ **Sample data scripts** — `write.py` populates courses, instructors, lessons, and learners
- ✅ **ORM query scripts** — `read_courses.py`, `read_instructors.py`, `read_learners.py` demonstrate a range of Django ORM query patterns
- ✅ **Environment-based secrets** — Database credentials and `SECRET_KEY` loaded from `.env`

---

## Data Models

### Entity Relationship Overview

```
User (base)
 ├── Instructor (inherits User)  ─── ManyToMany ──► Course
 └── Learner    (inherits User)  ─── through Enrollment ──► Course
                                                                 │
                                                              Lesson (ForeignKey)
```

### Model Descriptions

#### `User`
Base model for all users. Uses multi-table inheritance so `Instructor` and `Learner` each get their own database table linked to `User`.

| Field | Type | Notes |
|---|---|---|
| `first_name` | `CharField(30)` | Required, default `"john"` |
| `last_name` | `CharField(30)` | Required, default `"doe"` |
| `email` | `EmailField(50)` | Required |
| `location` | `CharField(100)` | Optional, default `"Unknown"` |
| `dob` | `DateField` | Optional |

---

#### `Instructor` _(extends User)_
Represents a course instructor.

| Field | Type | Notes |
|---|---|---|
| `full_time` | `BooleanField` | Default `True` |
| `total_learners` | `IntegerField` | Total number of learners taught |

---

#### `Learner` _(extends User)_
Represents a course learner.

| Field | Type | Notes |
|---|---|---|
| `occupation` | `CharField` with choices | `student`, `developer`, `data_scientist`, `dba` — default `student` |
| `social_link` | `URLField(200)` | Learner's social/portfolio URL |

---

#### `Course`
Represents an online course.

| Field | Type | Notes |
|---|---|---|
| `name` | `CharField(100)` | Default `"online course"` |
| `description` | `CharField(500)` | Course description |
| `instructors` | `ManyToManyField(Instructor)` | Direct M2M |
| `learners` | `ManyToManyField(Learner)` | Through `Enrollment` |

---

#### `Enrollment` _(through model)_
Junction table connecting `Learner` and `Course` with extra enrollment data.

| Field | Type | Notes |
|---|---|---|
| `learner` | `ForeignKey(Learner)` | CASCADE on delete |
| `course` | `ForeignKey(Course)` | CASCADE on delete |
| `date_enrolled` | `DateField` | Defaults to `now()` |
| `mode` | `CharField` with choices | `audit` or `honor` — default `audit` |

---

#### `Lesson`
Represents a lesson that belongs to a course.

| Field | Type | Notes |
|---|---|---|
| `title` | `CharField(200)` | Default `"title"` |
| `course` | `ForeignKey(Course)` | Nullable, CASCADE on delete |
| `content` | `TextField` | Full lesson content |

---

## Project Structure

```
DjangoCRUD/
├── .env.example            # Environment variable template
├── .flake8                 # Flake8 linting configuration
├── .gitignore              # Git ignore rules
├── manage.py               # Django management CLI entry point
├── settings.py             # Django project settings
├── write.py                # Script: create sample data in the database
├── read_courses.py         # Script: query and display all courses
├── read_instructors.py     # Script: advanced instructor ORM queries
├── read_learners.py        # Script: learner filtering and ordering queries
└── crud/                   # Main Django app
    ├── migrations/
    │   ├── __init__.py
    │   └── 0001_initial.py # Initial database migration
    └── models.py           # All data models (User, Instructor, Learner, Course, Enrollment, Lesson)
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL (or access to a cloud PostgreSQL instance)
- `pip`

### 1. Clone the repository

```bash
git clone https://github.com/rafael-a-g-n/DjangoCRUD.git
cd DjangoCRUD
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install django psycopg2-binary python-dotenv
```

### 4. Configure environment variables

Copy the example environment file and fill in your database credentials:

```bash
cp .env.example .env
```

Edit `.env`:

```dotenv
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=your_database_port
SECRET_KEY=your-secret-key-here
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Populate the database with sample data

```bash
python write.py
```

---

## Environment Variables

| Variable | Description | Example |
|---|---|---|
| `DB_NAME` | PostgreSQL database name | `defaultdb` |
| `DB_USER` | PostgreSQL username | `avnadmin` |
| `DB_PASSWORD` | PostgreSQL password | `s3cr3t` |
| `DB_HOST` | Database host | `your-host.aivencloud.com` |
| `DB_PORT` | Database port | `16579` |
| `SECRET_KEY` | Django secret key | `django-insecure-...` |

> **Never commit your `.env` file.** It is already listed in `.gitignore`.

---

## Usage

All scripts bootstrap Django settings before importing models, so they can be run directly from the project root.

### Populate sample data

```bash
python write.py
```

Creates:
- 4 instructors (John Doe, Yan Luo, Joy Li, Peter Chen)
- 2 courses (Cloud Application Development, Introduction to Python)
- 2 lessons
- 4 learners (James Smith, Maria Garcia, Anthony Davidson, Mark Taylor)

> **Note:** `write.py` calls `clean_data()` first, wiping all existing records before inserting fresh data.

### Read courses

```bash
python read_courses.py
```

Lists all courses stored in the database.

### Read instructors

```bash
python read_instructors.py
```

Demonstrates several ORM query patterns against the `Instructor` model (see [ORM Query Examples](#orm-query-examples) below).

### Read learners

```bash
python read_learners.py
```

Filters learners by last name and retrieves the two youngest learners sorted by date of birth.

---

## ORM Query Examples

The read scripts demonstrate a variety of Django ORM techniques:

```python
# Get a single record by field value
instructor = Instructor.objects.get(first_name="Yan")

# Handle missing records gracefully
try:
    Instructor.objects.get(first_name="Andy")
except Instructor.DoesNotExist:
    print("Instructor not found")

# Filter by a boolean field
part_time = Instructor.objects.filter(full_time=False)

# Chain exclude, filter, and field lookups
results = (
    Instructor.objects
    .exclude(full_time=False)
    .filter(total_learners__gt=30000)
    .filter(first_name__startswith="Y")
)

# Equivalent combined filter
results = Instructor.objects.filter(
    full_time=True,
    total_learners__gt=30000,
    first_name__startswith="Y",
)

# Filter by related field value
learners_named_smith = Learner.objects.filter(last_name="Smith")

# Order by dob descending (most recent birth date first = youngest) and slice
youngest = Learner.objects.order_by("-dob")[:2]
```

---

## Code Quality

This project uses [Flake8](https://flake8.pycqa.org/) for style and linting enforcement.

**Configuration (`.flake8`):**

```ini
[flake8]
max-line-length = 88
extend-ignore = E203, W503
```

Run the linter:

```bash
flake8 .
```

---

## License

This project is open source and available for educational use.
