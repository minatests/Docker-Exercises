# 🚢 BlogPlatform 🚀
[![Maintainer](https://img.shields.io/badge/Maintainer-MinaFatahi-blue)](mailto:fattahi123m@gmail.com)

Welcome to the BlogPlatform repository! 📝✨
This is a Django web application built with Docker for seamless development and deployment.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Clone the Repository](#1-clone-the-repository)
  - [Run the Application](#2-run-the-application)
  - [Access BlogPlatform](#3-access-blogplatform)
- [Environment Variables](#environment-variables)
- [Contributing](#contribute)

## Overview

BlogPlatform is a feature-rich blogging platform where you can create and explore posts, add comments, categorize your posts, and more!

## Features

- **Create Posts:** Share your thoughts with the world.
- **Add Comments:** Engage with other users through comments.
- **Categorize Posts:** Organize your content with categories.
- **Authorship:** Each post has its dedicated author.

## Prerequisites

Before you begin, make sure you have:

- [Docker](https://www.docker.com/get-started)

## Getting Started
Getting started is a piece of cake! 🍰 Follow these steps:

### 1. Clone the Repository 

    ```bash
        git clone https://github.com/your-username/BlogPlatform.git
        cd BlogPlatform

### 2. Run the Application

    ```bash
        docker-compose -f docker-compose.yaml up --build

### 3. Access BlogPlatform
Visit http://0.0.0.0:8000 in your browser to access BlogPlatform.


## Environment Variables

The `.env` file contains sensitive information such as secret keys and database credentials. This file is crucial for configuring your Django application and ensuring its secure operation.🔒

⚠️**Warning**⚠️: Keep your .env file confidential, and do not share it publicly. Exercise caution to prevent unintentional exposure of sensitive information.
   
    ```bash
        # .gitignore
        .env

### Why .env?

- **Security:** Storing sensitive information like secret keys and database credentials in a separate `.env` file adds an extra layer of security. This helps in keeping your sensitive information confidential.

- **Configuration Management:** The `.env` file centralizes configuration variables, making it easier to manage and update your application's settings.

### Example .env File:

    ```bash
        # Change these values with your own secret key and database credentials
         SECRET_KEY=your-secret-key
         DB_NAME=your-database-name
         DB_USER=your-database-user
         DB_PASSWORD=your-database-password
         DB_HOST=db
         DB_PORT=5432

## Contribute 🤝
I welcome contributions!✨ If you'd like to improve this project, feel free to open an issue, fork the repository, or submit a pull request. I would love to see your creativity and django skills to make this project complete as it's an incomplete project, having only an admin panel to work with. Together, let's make BlogPlatform even better!  🚀

