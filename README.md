# Module 11 - FastAPI Calculator App

This project is a secure and testable FastAPI application that performs calculations using SQLAlchemy models and Pydantic schemas.

## Features

- FastAPI app with calculation routes
- SQLAlchemy ORM with PostgreSQL
- Pydantic schemas for validation
- Factory pattern (optional)
- Unit and integration tests with `pytest`
- Docker support for local development
- GitHub Actions CI/CD
- DockerHub deployment

## Project Structure
- module11/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   └── calculation.py
│   ├── schemas/
│   │   └── calculation.py
│   ├── services/
│   │   └── calculation_factory.py 
│   │   └── session.py
│   └── tests/
│       ├── test_unit/
│       │   └── test_factory.py
│       └── test_integration/
│           └── test_calculation.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── README.md

## Getting Started

- Clone the Repository:
- git clone https://github.com/YOUR_USERNAME/module11.git
- cd module11

## Run with Docker

- docker-compose up --build
- Visit the app at: http://localhost:8000/docs

## Run Tests
- pytest

## CI/CD
- This repo uses GitHub Actions to:
- Run tests on push/pull requests
- Build Docker image
- Push image to DockerHub

## DockerHub
- Image: eddysantana/module11-fastapi

## Author
- Eddy Santana