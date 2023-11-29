# 🐳 FastAPI Dockerized App 🚀

Welcome to the FastAPI Dockerized App repository! This project demonstrates a simple FastAPI application, packaged with Docker for easy deployment.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project showcases a FastAPI application that counts the number of visits to the root endpoint. The application is Dockerized for seamless deployment and scalability.

## Project Structure
   ```bash
   fastapp/
   |-- Dockerfile
   |-- requirements.txt
   |-- fast-app.py

- **Dockerfile:** Specifies the Docker image and configurations.
- **requirements.txt:** Lists the Python dependencies for the FastAPI app.
- **fast-app.py:** The FastAPI application code.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Python](https://www.python.org/downloads/) (if you want to run the app locally without Docker)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/fastapi-docker-app.git
   cd fastapi-docker-app
2. Build the Docker Image:
  ```bash
     docker build -t fastapi-app .
3. Run with Docker
  ```bash
  docker run -p 80:80 fastapi-app
  
Visit http://localhost in your browser to see the FastAPI app in action.

###Run Locally (Without Docker)
1. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   Run the FastAPI App:
2. **run**
   ```bash
   uvicorn fast-app:app --host 0.0.0.0 --port 80
  
Visit http://localhost in your browser.
