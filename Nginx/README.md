# Welcome to Mina's Nginx Docker Container

[![Maintainer](https://img.shields.io/badge/Maintainer-Mina%20Fatahi-blue)](mailto:fattahi123m@gmail.com)

This repository contains a Docker configuration to run a simple Nginx web server serving a custom HTML page.

## Quick Start

1. Ensure you have Docker installed on your machine.
2. Clone this repository:

    ```bash
    git clone https://github.com/minatests/docker-exercises.git
    ```

3. Build the Docker image:

    ```bash
    docker build -t my-nginx:latest .
    ```

4. Run the Docker container:

    ```bash
    docker run -p 8080:80 my-nginx:latest
    ```

5. Open your browser and navigate to [http://localhost:8080](http://localhost:8080) to see the Nginx Container in action!

## Project Structure

- **`nginx.conf`**: Configuration file for Nginx, including server settings and location directives.
- **`index.html`**: Simple HTML page served by Nginx.
- **`Dockerfile`**: Instructions to build the Docker image.

---

**Note:** This is a basic setup for educational purposes. In a production environment, consider additional security measures and optimizations.
