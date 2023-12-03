# Welcome to My Python Dockerized Application 🐍🐳

[![Maintainer](https://img.shields.io/badge/Maintainer-MinaFatahi-blue)](mailto:fattahi123m@gmail.com)

This repository contains a simple Python application that greets the user by asking for their name and prints a personalized message.

## Quick Start

1. Ensure you have Docker installed on your machine.
2. Clone this repository:

    ```bash
    git clone https://github.com/minatests/docker-exercises.git
    ```

3. Build the Docker image:

    ```bash
    docker build -t my-python-app:latest .
    ```

4. Run the Docker container:

    ```bash
    docker run -it my-python-app:latest
    ```

5. Follow the prompts to enter your name and experience a personalized greeting from the application.

## Project Structure

- **`app.py`**: Python script that prompts the user for their name and prints a personalized greeting.
- **`Dockerfile`**: Configuration for building the Docker image.


