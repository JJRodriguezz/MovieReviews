# Movie Showcase Web Application

## Overview

This project is a web application developed using Python, Django, and HTML that allows users to explore a collection of movies. The application provides advanced features such as searching, filtering, and statistical visualizations of movie data.

## Features

- **View movies**: Browse a list of movies with their titles, images, and descriptions.
- **Search functionality**: Search for movies by title.
- **Statistics module**: View graphical statistics of movie data, including:
  - Movies per year.
  - Movies per genre (based on the first genre assigned to each movie).

- **Bootstrap integration**: A user-friendly and responsive UI built with Bootstrap.

## Installation

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- pip (Python package manager)

### Steps

1. Clone this repository:
   ```sh
   git clone <repository_url>
   cd <repository_folder>
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate     # On Windows
3. Install the dependencies:
   ```h
   pip install -r requirements.txt
4. Apply database migrations:
   ```h
   python manage.py migrate
5. Create a superuser (optional, for admin access):
   ```h
   python manage.py createsuperuser
6. Run the development server:
   ```h
   python manage.py runserver
7. Open your browser and navigate to http://127.0.0.1:8000/