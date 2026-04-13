# Trustdial - DevOps Project

A distributed system to verify business contact numbers using FastAPI, RabbitMQ, PostgreSQL, and Docker.

# Features

- Add and manage businesses
- Async verification using RabbitMQ
- Worker-based background processing
- Real-time UI updates
- Dockerized microservices architecture

# Architecture

Frontend (HTML/JS)  
⬇  
FastAPI Backend  
⬇  
RabbitMQ Queue  
⬇  
Worker Service  
⬇  
PostgreSQL Database

# Tech Stack

- FastAPI
- PostgreSQL
- RabbitMQ
- Docker & Docker Compose
- SQLAlchemy

# Run Locally

```bash
docker compose up --build -d
```
