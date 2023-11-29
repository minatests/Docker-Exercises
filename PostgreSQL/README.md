# Welcome to My PostgreSQL Dockerized Database

[![Maintainer](https://img.shields.io/badge/Maintainer-Your%20Name-blue)](mailto:fattahi123m@gmail.com)

This repository provides a Dockerized PostgreSQL database with initialization scripts.

## Overview

This project sets up a PostgreSQL database within a Docker container, pre-configured with a specific user, password, and initial database. The database initialization is done using SQL scripts located in the `init-scripts/` directory.

## Quick Start

1. Ensure you have Docker installed on your machine.
2. Clone this repository:

    ```bash
    git clone https://github.com/minatests/docker-exercises.git
    ```

3. Build the Docker image:

    ```bash
    docker build -t my-postgres-db:latest .
    ```

4. Run the Docker container:

    ```bash
    docker run -p 5432:5432 my-postgres-db:latest
    ```

5. Your PostgreSQL database is now running with the specified user, password, and database.

## Project Structure

- **`Dockerfile`**: Configuration for building the PostgreSQL Docker image.
- **`init-scripts/`**: Contains initialization SQL scripts.
- **`01_init.sql`**: Creates a sample table named `mytable`. This table has two columns: `id` (a serial primary key) and `name` (a non-null VARCHAR with a maximum length of 100 characters).

---

**Note:** Ensure that sensitive information like passwords is handled securely in production environments.

