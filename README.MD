# DjangoCRUD Portfolio Project

![Python](https://img.shields.io/badge/Python-3.12.3-blue)
![Django](https://img.shields.io/badge/Django-4.2-092E20)
![MySQL](https://img.shields.io/badge/MySQL-TiDB-4479A1)
![Code Quality](https://img.shields.io/badge/Code_Quality-10%2F10_Pylint-brightgreen)

Welcome! This is a portfolio project showcasing a full-featured Django CRUD application for managing an educational platform. It models the data layer for courses, instructors, learners, and enrollments, and features a clean, responsive frontend UI.

**Live Demo:** [djangocrud-3enc.onrender.com](https://djangocrud-3enc.onrender.com/)

## 🚀 Features
* **Full CRUD Operations:** Create, Read, Update, and Delete capabilities for all major entities.
* **Frontend UI:** Clean, responsive HTML/CSS/Bootstrap templates with intuitive navigation and form handling.
* **Relational Database:** Powered by a cloud-hosted MySQL database via TiDB.
* **Secure Coding:** Follows OWASP Top 10 guidelines, utilizing `.env` files for secure credential management.
* **Flawless Code Quality:** Strictly adheres to PEP 8. The codebase scores a **perfect 10/10 on Pylint** and has **0 Flake8 errors**.
* **Production Ready:** Configured for seamless deployment on platforms like Render.

## 🛠️ Technical Stack
* **Backend:** Python 3.12.3, Django 4.2
* **Frontend:** Django Templates, HTML, CSS, Bootstrap
* **Database:** MySQL (Cloud-hosted via TiDB)
* **Code Quality Tools:** Flake8, Pylint
* **Environment Management:** `python-dotenv`

## 🗄️ Database Schema & Architecture
This project demonstrates advanced Django ORM patterns to handle complex data relationships without relying on raw SQL:
* **Model Inheritance:** `Instructor` and `Learner` models extend a shared `User` base model using Django's multi-table inheritance.
* **Many-to-Many Relationships:** `Course` models are linked to `Instructor` models directly, and linked to `Learner` models via a custom `Enrollment` through-table.
* **Metadata Storage:** The custom `Enrollment` table tracks additional data such as enrollment dates, grades, and course modes (audit/honor).

## 💻 How to Run Locally

1. **Clone the repository:**
   `git clone https://github.com/rafael-a-g-n/DjangoCRUD.git`
   `cd DjangoCRUD`

2. **Set up a virtual environment and install dependencies:**
   `python -m venv .venv`
   `source .venv/bin/activate`  *(On Windows use: `.venv\Scripts\activate`)*
   `pip install -r requirements.txt`

3. **Configure Environment Variables:**
   * Create a `.env` file in the root directory based on `.env.example`.
   * Add your TiDB MySQL database credentials and Django secret key.

4. **Apply database migrations:**
   `python manage.py migrate`

5. **Create a superuser (optional, for admin access):**
   `python manage.py createsuperuser`

6. **Run the development server:**
   `python manage.py runserver`
   Access the app at `http://localhost:8000/`

## 🧪 Running Code Quality Checks
This project maintains strict code quality standards. To run the linters locally:

* **Run Flake8 (PEP 8 compliance):**
  `flake8 .`

* **Run Pylint (Advanced logic and style checking):**
  `pylint crud`

## 📚 API/Feature Table

| Entity      | Endpoint/URL Pattern                  | Method   | Feature/Description                |
|-------------|--------------------------------------|----------|------------------------------------|
| Course      | /courses/                            | GET      | List all courses                   |
| Course      | /courses/create/                     | GET/POST | Create a new course                |
| Course      | /courses/<int:pk>/                   | GET      | View course details                |
| Course      | /courses/<int:pk>/edit/              | GET/POST | Update a course                    |
| Course      | /courses/<int:pk>/delete/            | GET/POST | Delete a course                    |
| Instructor  | /instructors/                        | GET      | List all instructors               |
| Instructor  | /instructors/create/                 | GET/POST | Create a new instructor            |
| Instructor  | /instructors/<int:pk>/               | GET      | View instructor details            |
| Instructor  | /instructors/<int:pk>/edit/          | GET/POST | Update an instructor               |
| Instructor  | /instructors/<int:pk>/delete/        | GET/POST | Delete an instructor               |
| Learner     | /learners/                           | GET      | List all learners                  |
| Learner     | /learners/create/                    | GET/POST | Create a new learner               |
| Learner     | /learners/<int:pk>/                  | GET      | View learner details               |
| Learner     | /learners/<int:pk>/edit/             | GET/POST | Update a learner                   |
| Learner     | /learners/<int:pk>/delete/           | GET/POST | Delete a learner                   |
| Enrollment  | /courses/<int:course_id>/enroll/     | GET/POST | Enroll a learner in a course       |
| Enrollment  | /enrollments/<int:pk>/edit/          | GET/POST | Update an enrollment               |
| Enrollment  | /enrollments/<int:pk>/delete/        | GET/POST | Delete an enrollment               |

## 📝 Portfolio Notice
This project is intended for portfolio purposes to demonstrate backend architecture, frontend integration, and Django best practices. Feel free to explore the code, use it for learning, or contribute!

## 📄 License

This project is licensed under the [MIT License](LICENSE).