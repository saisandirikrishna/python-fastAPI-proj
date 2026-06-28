# 🚀 FastAPI on AWS ECS Fargate with GitHub Actions CI/CD

## 📌 Project Overview

This project demonstrates my transition from an Angular Frontend Developer to a Full Stack Cloud Engineer by building and deploying a Python FastAPI application using modern DevOps and AWS cloud practices.

The goal was not only to learn Python, but also to understand the complete software delivery lifecycle:

* Application Development
* Version Control
* Containerization
* Cloud Deployment
* CI/CD Automation
* AWS Container Services

This project was built from scratch and deployed to AWS ECS Fargate using GitHub Actions without Jenkins.

---

# 🎯 Learning Objectives

Through this project I focused on gaining hands-on experience in:

✅ Python Backend Development

✅ FastAPI Framework

✅ Git & GitHub

✅ Docker Containerization

✅ Amazon Elastic Container Registry (ECR)

✅ Amazon Elastic Container Service (ECS Fargate)

✅ IAM & Cloud Security

✅ GitHub Actions CI/CD

✅ Cloud Networking Concepts

---

# 🏗️ Project Architecture

```text
┌──────────────────────────┐
│ Local Development        │
│ Python + FastAPI         │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ GitHub Repository        │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ GitHub Actions Pipeline  │
│ Build & Deploy           │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ Docker Image             │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ AWS ECR Repository       │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ AWS ECS Fargate          │
│ Running Container        │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ FastAPI Application      │
└──────────────────────────┘
```

---

# 📂 Project Structure

```text
python-fastAPI-proj
│
├── app
│   ├── __init__.py
│   └── main.py
│
├── .github
│   └── workflows
│       └── deploy.yml
│
├── Dockerfile
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

---

# 🛠️ End-to-End Implementation Journey

## Phase 1: Python & FastAPI Development

Created a FastAPI project from scratch with proper folder structure.

Implemented:

* Root endpoint
* Health endpoint
* Swagger documentation
* Uvicorn server

Verified application locally:

```bash
uvicorn app.main:app --reload
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

## Phase 2: Python Virtual Environment

Created isolated Python environment:

```bash
python -m venv python-vm
```

Activated environment:

```bash
python-vm\Scripts\activate
```

Installed dependencies:

```bash
pip install fastapi uvicorn
```

---

## Phase 3: Git & GitHub Integration

Initialized local Git repository.

Connected local project to GitHub repository.

Implemented:

* Git initialization
* Commit management
* Push to GitHub
* Version control workflow

Commands used:

```bash
git init
git add .
git commit -m "Initial Commit"
git remote add origin <repo-url>
git push -u origin main
```

---

## Phase 4: Docker Containerization

Created Dockerfile for FastAPI application.

Built Docker image locally:

```bash
docker build -t fastapi-app .
```

Verified container execution:

```bash
docker run -p 8000:8000 fastapi-app
```

Validated application inside container using Swagger UI.

---

## Phase 5: AWS Cloud Setup

Configured AWS CLI.

Validated identity:

```bash
aws sts get-caller-identity
```

Configured:

* AWS Account
* IAM User
* AWS Credentials
* AWS CLI

---

## Phase 6: Amazon ECR

Created Amazon Elastic Container Registry.

Built image locally and pushed to AWS.

Workflow:

```text
Docker Image
      │
      ▼
AWS ECR Repository
```

Commands:

```bash
docker tag fastapi-app <ecr-uri>
docker push <ecr-uri>
```

Skills Learned:

* Container Registry
* Image Versioning
* AWS Authentication

---

## Phase 7: Amazon ECS Fargate

Created:

### ECS Cluster

Container orchestration environment.

### Task Definition

Defined:

* Container image
* CPU
* Memory
* Port Mapping
* Runtime configuration

### ECS Service

Configured:

* Desired task count
* Networking
* Public IP assignment
* Task management

Result:

FastAPI application successfully running on ECS Fargate.

---

## Phase 8: Security & Networking

Configured:

### IAM

* Access Keys
* Policies
* Cloud Permissions

### Security Groups

Opened inbound traffic:

```text
Port 8000
```

Allowed public access to FastAPI application.

Learned:

* VPC Networking
* Security Groups
* Inbound Rules
* Public vs Private Access

---

## Phase 9: GitHub Actions CI/CD

First hands-on implementation of GitHub Actions.

Created automated deployment pipeline.

Workflow:

```text
Git Push
    │
    ▼
GitHub Actions
    │
    ▼
Docker Build
    │
    ▼
Push to ECR
    │
    ▼
Deploy ECS Service
```

Configured GitHub Secrets:

| Secret                | Purpose               |
| --------------------- | --------------------- |
| AWS_ACCESS_KEY_ID     | AWS Authentication    |
| AWS_SECRET_ACCESS_KEY | AWS Authentication    |
| AWS_REGION            | Deployment Region     |
| ECR_REPOSITORY        | Target ECR Repository |
| ECS_CLUSTER           | ECS Cluster           |
| ECS_SERVICE           | ECS Service           |
| ECS_TASK_DEFINITION   | ECS Task Definition   |

---

# ☁ AWS Services Used

| Service         | Purpose                        |
| --------------- | ------------------------------ |
| IAM             | Authentication & Authorization |
| ECR             | Docker Image Repository        |
| ECS Fargate     | Container Runtime              |
| VPC             | Networking                     |
| Security Groups | Firewall Rules                 |
| CloudWatch      | ECS Logs                       |
| GitHub Actions  | CI/CD Automation               |

---

# 📈 Skills Demonstrated

## Backend Development

* Python
* FastAPI
* REST APIs

## DevOps

* Docker
* GitHub Actions
* CI/CD Pipelines

## Cloud

* AWS ECS
* AWS ECR
* IAM
* Networking

## Version Control

* Git
* GitHub

---

# 🚀 Current Status

| Feature                 | Status      |
| ----------------------- | ----------- |
| FastAPI Development     | ✅ Completed |
| Docker Containerization | ✅ Completed |
| GitHub Integration      | ✅ Completed |
| ECR Deployment          | ✅ Completed |
| ECS Deployment          | ✅ Completed |
| Security Groups         | ✅ Completed |
| GitHub Actions CI/CD    | ✅ Completed |
| Swagger Documentation   | ✅ Completed |

---

# 🔮 Future Enhancements

Next learning milestones:

* Kubernetes (EKS)
* Terraform Infrastructure as Code
* Application Load Balancer (ALB)
* Route53 Custom Domain
* HTTPS using ACM
* PostgreSQL Integration
* JWT Authentication
* Unit Testing
* Monitoring with CloudWatch
* Production-grade ECS Architecture

---

# 👨‍💻 About Me

Frontend Developer with professional experience in Angular.

Currently expanding expertise into:

* Python Backend Development
* Cloud Engineering
* AWS
* DevOps
* Containerization
* CI/CD Automation

This repository represents my hands-on learning journey toward becoming a Full Stack Cloud Engineer.
