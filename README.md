# Heroes and Powers API

This is a Flask-based RESTful API for managing superheroes and their powers. The API allows users to retrieve heroes, powers, and assign powers to heroes with varying strengths. It uses SQLAlchemy for ORM, Flask-Migrate for database migrations, and SQLite for data storage during development.

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [API Endpoints](#api-endpoints)
6. [Database Models](#database-models)
7. [Running Migrations](#running-migrations)
8. [Seeding the Database](#seeding-the-database)

## Features

- Manage heroes and their superpowers.
- Create relationships between heroes and powers with a specified strength.
- SQLite used for database storage.
- Flask-Migrate for easy database schema updates.

## Requirements

- Python 3.8+
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLAlchemy-Serializer

## Installation

1. **Clone the repository:**

   ```bash
   git https://github.com/MUCHIRIJOHN1990/Phase-4-Code-Challenge-Superheroes.git
   cd Phase-4-Code-Challenge
   ```

2. **Install dependencies using Pipenv:**

   ```bash
   pipenv install
   ```

3. **Activate the virtual environment:**

   ```bash
   pipenv shell
   ```

4. **Set up the SQLite database:**

   ```bash
   flask db upgrade
   ```

## Usage

1. **Run the application:**

   ```bash
   flask run
   ```

2. The application will be available at `http://127.0.0.1:5000/`.

## API Endpoints

- **GET /heroes**: Retrieve all heroes.
- **GET /heroes/{id}**: Retrieve a specific hero by ID.
- **GET /powers**: Retrieve all powers.
- **GET /powers/{id}**: Retrieve a specific power by ID.
- **PATCH /powers/{id}**: Update an existing power.
- **POST /hero_powers**: Create a new relationship between a hero and a power. Requires the following JSON body:

  ```json
  {
      "strength": "Strong",
      "hero_id": 1,
      "power_id": 2
  }
  ```

## Database Models

- **Hero**:
  - `id`: Integer, Primary Key
  - `name`: String, Hero's real name
  - `super_name`: String, Hero's superhero name

- **Power**:
  - `id`: Integer, Primary Key
  - `name`: String, Name of the power
  - `description`: String, Detailed description of the power (must be at least 20 characters)

- **HeroPower**:
  - `id`: Integer, Primary Key
  - `strength`: String, Strength of the hero's power (`Strong`, `Weak`, `Average`)
  - `hero_id`: ForeignKey, Reference to a `Hero`
  - `power_id`: ForeignKey, Reference to a `Power`

## Running Migrations

Whenever changes are made to the database models, use Flask-Migrate to handle migrations:

1. **Create a migration:**

   ```bash
   flask db migrate -m "description of changes"
   ```

2. **Apply the migration:**

   ```bash
   flask db upgrade
   ```

## Seeding the Database

To populate the database with initial heroes and powers for testing:

1. Run the `seed.py` script:

   ```bash
   python seed.py
   ```

2. The script will clear the current database, create new records for heroes and powers, and assign random powers to the heroes.
