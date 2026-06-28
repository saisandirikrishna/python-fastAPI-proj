# Python FastAPI REST API

A backend REST API application built using FastAPI and Python as part of my journey from Angular Frontend Development to Full-Stack and Cloud-Native Engineering.

This project demonstrates the implementation of REST APIs using FastAPI, clean project architecture, request validation with Pydantic, service-based business logic, and API documentation through Swagger UI.

---

## Project Overview

The goal of this project is to learn and implement backend development concepts using Python and FastAPI while applying software engineering best practices such as:

* Layered Architecture
* REST API Design
* Request and Response Validation
* Service-Oriented Development
* Environment-Based Configuration
* Version Control with Git
* API Documentation

---

## Tech Stack

### Backend

* Python 3.x
* FastAPI
* Uvicorn
* Pydantic

### Development Tools

* Git & GitHub
* VS Code
* Virtual Environment (venv)

### Future Enhancements

* PostgreSQL
* SQLAlchemy ORM
* Alembic Migrations
* Docker
* Kubernetes
* CI/CD with GitHub Actions
* AWS Deployment

---

## Project Structure

```text
python-fastAPI-proj/
│
├── app/
│   ├── api/
│   │   └── user_routes.py
│   │
│   ├── services/
│   │   └── user_service.py
│   │
│   ├── schemas/
│   │   └── user_schema.py
│   │
│   ├── core/
│   │   └── config.py
│   │
│   ├── database/
│   │   └── db.py
│   │
│   └── main.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Features

* FastAPI REST API
* Modular Project Structure
* User Creation API
* User Retrieval API
* Pydantic Validation
* Swagger Documentation
* Environment Variable Support

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd python-fastAPI-proj
```

### Create Virtual Environment

```bash
python -m venv python-vm
```

### Activate Virtual Environment

Windows:

```bash
python-vm\Scripts\activate
```

Linux/Mac:

```bash
source python-vm/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
uvicorn app.main:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## Sample APIs

### Create User

POST /users

Request:

```json
{
  "name": "Sai Krishna",
  "email": "sai@example.com"
}
```

Response:

```json
{
  "id": 1,
  "name": "Sai Krishna",
  "email": "sai@example.com"
}
```

---

### Get Users

GET /users

Response:

```json
[
  {
    "id": 1,
    "name": "Sai Krishna",
    "email": "sai@example.com"
  }
]
```

---

## Learning Objectives

This project was created to gain hands-on experience with:

* Python Programming
* FastAPI Framework
* REST API Development
* Backend Architecture
* Cloud-Native Development Practices
* DevOps Integration
* Containerization and Deployment

---

## Roadmap

* [x] FastAPI Setup
* [x] Basic CRUD APIs
* [ ] PostgreSQL Integration
* [ ] SQLAlchemy ORM
* [ ] Authentication & Authorization (JWT)
* [ ] Dockerization
* [ ] GitHub Actions CI/CD
* [ ] Kubernetes Deployment
* [ ] AWS Deployment

---

## About Me

I am a Software Engineer with experience in Angular, TypeScript, JavaScript, Cloud Technologies, DevOps, Kubernetes, Terraform, and AWS.

Currently expanding my expertise into Python Backend Development and Cloud-Native Application Architecture to become a Full-Stack Cloud Engineer.

---

## License

This project is created for learning and portfolio purposes.
