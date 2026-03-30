# DjangoCRUD 🐍🗄️

> A full-featured **Django ORM CRUD application** demonstrating database design, data modeling, and complex query patterns with a cloud-hosted **PostgreSQL** backend.

[![Python](https://img.shields.io/badge/Python-3.12.3-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Cloud-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Flake8](https://img.shields.io/badge/Linting-Flake8-informational?style=for-the-badge)](https://flake8.pycqa.org/)
[![python-dotenv](https://img.shields.io/badge/Config-python--dotenv-ECD53F?style=for-the-badge)](https://pypi.org/project/python-dotenv/)

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Technologies & Skills](#technologies--skills)
- [Features](#features)
- [Data Models & Relationships](#data-models--relationships)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
  - [Populate the Database](#populate-the-database)
  - [Query Instructors](#query-instructors)
  - [Query Learners](#query-learners)
  - [Query Courses](#query-courses)
- [Django ORM Examples](#django-orm-examples)
- [Database Schema](#database-schema)
- [Skills Demonstrated](#skills-demonstrated)

---

## About the Project

**DjangoCRUD** is a backend-focused project that models an educational platform's data layer. It showcases the full power of Django's Object-Relational Mapper (ORM) to define complex relational database schemas and perform sophisticated queries — all without writing a single line of raw SQL.

The application manages **Users**, **Instructors**, **Learners**, **Courses**, **Lessons**, and **Enrollments**, reflecting real-world relationships such as multi-instructor courses and many-to-many enrollment tables enriched with metadata.

---

## Technologies & Skills

| Category | Technology |
|---|---|
| **Language** | Python 3.12.3 |
| **Framework** | Django 4.2 |
| **Database** | PostgreSQL (via psycopg2) |
| **Cloud DB Host** | Aiven Cloud |
| **ORM** | Django ORM |
| **Config Management** | python-dotenv |
| **Code Quality** | Flake8 |
| **Version Control** | Git |

---

## Features

- 🏗️ **Model Inheritance** — `Instructor` and `Learner` extend a shared `User` base model using Django's multi-table inheritance
- 🔗 **Many-to-Many Relationships** — Courses are linked to multiple Instructors directly, and to Learners via a custom `Enrollment` through-table
- 🗂️ **Custom Through Table** — `Enrollment` stores extra metadata (enrollment date, mode) on the M2M relationship
- 🔍 **Advanced ORM Queries** — Demonstrates `.get()`, `.filter()`, `.exclude()`, chained filters, field lookups (`__gt`, `__startswith`), and ordering with slicing
- ⚙️ **Environment-Based Config** — Credentials and secrets managed safely via `.env` and `python-dotenv`
- 🧹 **Seeding & Cleanup Scripts** — Standalone scripts to populate and reset database state for development

---

## Data Models & Relationships

### Model Overview

```
User (base)
 ├── Instructor  (multi-table inheritance)
 └── Learner     (multi-table inheritance)

Course
 ├── instructors  →  ManyToMany(Instructor)
 └── learners     →  ManyToMany(Learner, through=Enrollment)

Lesson
 └── course  →  ForeignKey(Course)

Enrollment  [through table]
 ├── learner  →  ForeignKey(Learner)
 ├── course   →  ForeignKey(Course)
 ├── date_enrolled
 └── mode  (audit | honor)
```

### Model Details

#### `User`
| Field | Type | Notes |
|---|---|---|
| `id` | BigAutoField | Primary key |
| `first_name` | CharField(30) | Required |
| `last_name` | CharField(30) | Required |
| `email` | EmailField(50) | Required |
| `location` | CharField(100) | Optional |
| `dob` | DateField | Optional |

#### `Instructor` *(extends User)*
| Field | Type | Notes |
|---|---|---|
| `user_ptr` | OneToOneField | Parent link to User |
| `full_time` | BooleanField | Default: `True` |
| `total_learners` | IntegerField | |

#### `Learner` *(extends User)*
| Field | Type | Notes |
|---|---|---|
| `user_ptr` | OneToOneField | Parent link to User |
| `occupation` | CharField (choices) | `student`, `developer`, `data_scientist`, `dba` |
| `social_link` | URLField(200) | |

#### `Course`
| Field | Type | Notes |
|---|---|---|
| `id` | BigAutoField | Primary key |
| `name` | CharField(100) | Default: `"online course"` |
| `description` | CharField(500) | |
| `instructors` | ManyToManyField | → Instructor |
| `learners` | ManyToManyField | → Learner (through Enrollment) |

#### `Lesson`
| Field | Type | Notes |
|---|---|---|
| `id` | BigAutoField | Primary key |
| `title` | CharField(200) | |
| `content` | TextField | |
| `course` | ForeignKey | → Course (CASCADE) |

#### `Enrollment`
| Field | Type | Notes |
|---|---|---|
| `id` | BigAutoField | Primary key |
| `learner` | ForeignKey | → Learner (CASCADE) |
| `course` | ForeignKey | → Course (CASCADE) |
| `date_enrolled` | DateField | Default: now |
| `mode` | CharField (choices) | `audit` or `honor` |

---

## Project Structure

```
DjangoCRUD/
├── crud/                        # Main Django application
│   ├── models.py                # All data models (User, Instructor, Learner, Course, Lesson, Enrollment)
│   └── migrations/
│       ├── __init__.py
│       └── 0001_initial.py      # Auto-generated initial migration
├── manage.py                    # Django project management CLI
├── settings.py                  # Django configuration (DB, installed apps, secret key)
├── write.py                     # Seed script: creates instructors, learners, courses, lessons
├── read_courses.py              # Query script: retrieve all courses
├── read_instructors.py          # Query script: ORM filter/exclude/get examples for instructors
├── read_learners.py             # Query script: ORM filter/order_by examples for learners
├── .env.example                 # Environment variable template
├── .flake8                      # Flake8 linting configuration
└── .gitignore                   # Git ignore rules
```

---

## Getting Started

### Prerequisites

- Python **3.10+** (developed with 3.12.3)
- A running **PostgreSQL** instance (local or cloud)
- `pip` for package installation

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/rafael-a-g-n/DjangoCRUD.git
   cd DjangoCRUD
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate         # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install django psycopg2-binary python-dotenv
   ```

### Configuration

1. **Copy the environment template**
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env`** with your PostgreSQL credentials:
   ```env
   DB_NAME=your_database_name
   DB_USER=your_database_user
   DB_PASSWORD=your_database_password
   DB_HOST=your_database_host
   DB_PORT=your_database_port
   SECRET_KEY=your-secret-key-here
   ```

3. **Run migrations** to create the database schema:
   ```bash
   python manage.py migrate
   ```

---

## Usage

### Populate the Database

Run the seed script to create sample instructors, learners, courses, and lessons:

```bash
python write.py
```

This will:
- Delete any existing data (clean slate)
- Create **4 Instructors** (John Doe, Yan Luo, Joy Li, Peter Chen)
- Create **2 Courses** (Cloud Application Development, Introduction to Python)
- Create **2 Lessons**
- Create **4 Learners** (James Smith, Maria Garcia, Anthony Davidson, Mark Taylor)

### Query Instructors

Demonstrates `get`, `filter`, `exclude`, and chained lookups:

```bash
python read_instructors.py
```

### Query Learners

Demonstrates `filter` by field and `order_by` with slicing:

```bash
python read_learners.py
```

### Query Courses

Retrieves all course records:

```bash
python read_courses.py
```

---

## Django ORM Examples

This project showcases a range of Django ORM patterns:

```python
# Retrieve a single object by field value
instructor = Instructor.objects.get(first_name="Yan")

# Handle non-existent records gracefully
try:
    Instructor.objects.get(first_name="Andy")
except Instructor.DoesNotExist:
    print("Instructor not found")

# Filter by field value
part_time = Instructor.objects.filter(full_time=False)

# Exclude, then chain multiple filters with field lookups
result = (
    Instructor.objects
    .exclude(full_time=False)
    .filter(total_learners__gt=30000)
    .filter(first_name__startswith="Y")
)

# Equivalent combined filter
result = Instructor.objects.filter(
    full_time=True,
    total_learners__gt=30000,
    first_name__startswith="Y"
)

# Order by date of birth descending (most recent first = youngest), take top 2
youngest_two_learners = Learner.objects.order_by("-dob")[0:2]

# Retrieve all records
courses = Course.objects.all()
```

---

## Database Schema

```
┌─────────────────────────────────────────────┐
│                    User                      │
│  id · first_name · last_name · email        │
│  location · dob                             │
└──────────────┬──────────────────────────────┘
               │ (multi-table inheritance)
     ┌─────────┴──────────┐
     │                    │
┌────▼────────┐   ┌───────▼──────────┐
│ Instructor  │   │     Learner      │
│ full_time   │   │ occupation       │
│ total_      │   │ social_link      │
│ learners    │   └────────┬─────────┘
└────┬────────┘            │
     │  M2M                │ M2M (through)
     │              ┌──────▼──────────────┐
     │              │     Enrollment      │
     │              │ date_enrolled · mode│
     │              └──────┬──────────────┘
     │                     │
┌────▼─────────────────────▼──────────────────┐
│                   Course                     │
│  id · name · description                    │
└─────────────────────┬───────────────────────┘
                      │ FK
               ┌──────▼──────┐
               │   Lesson    │
               │ title       │
               │ content     │
               └─────────────┘
```

---

## Skills Demonstrated

| Skill | Details |
|---|---|
| **Django ORM** | Model definitions, migrations, complex queries |
| **Database Design** | Normalization, inheritance, M2M through-tables |
| **Python** | OOP, modules, exception handling, scripting |
| **PostgreSQL** | Cloud-hosted relational database integration |
| **Environment Management** | Secure config with `.env` and `python-dotenv` |
| **Code Quality** | PEP 8 compliance enforced with Flake8 |
| **Version Control** | Git with `.gitignore` and clean commit history |
| **Software Architecture** | Separation of concerns (models, config, scripts) |

---

> **Author:** [rafael-a-g-n](https://github.com/rafael-a-g-n)
