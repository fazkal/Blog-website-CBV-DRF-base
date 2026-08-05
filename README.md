# Blog-website-CBV-DRF-base

A professional blog website built with **Django**, leveraging **Class-Based Views (CBV)** for standard web views and **Django Rest Framework (DRF)** for API-driven features.

## Description

This project is a flexible blog platform. It combines the ease of use of Django's Class-Based Views for traditional page rendering with the power of Django Rest Framework for building robust APIs. This structure makes it ideal for projects that might later integrate a frontend framework like React or Vue, or simply need to provide data access for mobile apps.

## Features

- **Class-Based Views:** Clean, reusable code for standard blog pages.
- **Django Rest Framework (DRF):** API endpoints for posts, categories, and users.
- **Post Management:** Create, Read, Update, and Delete (CRUD) functionality.
- **User Authentication:** Secure access for authors and visitors.
- **Responsive Design:** Built with best practices for web accessibility.

## Requirements

- Python 3.x
- Django
- Django Rest Framework
- pip

## Installation

1. Clone the repository:
```bash
git clone https://github.com/fazkal/Blog-website-CBV-DRF-base.git
cd Blog-website-CBV-DRF-base

2. Install dependencies:
```bash
pip install -r requirements.txt

3. Run migrations:
```bash
python manage.py migrate

4. Create a superuser:
```bash
python manage.py createsuperuser

5. Run the development server:
```bash
python manage.py runserver
```
6.Open your browser and go to:

http://127.0.0.1:8000/

API Endpoints (DRF)

If you are using the API, you can access the following endpoints:

    Posts: /api/posts/
    Users: /api/users/

(Note: Ensure your urls.py is configured to route these requests properly.)
Contributing

Contributions are welcome! If you’d like to improve the project:

    Fork the repository
    Create a feature branch
    Make your changes
    Submit a pull request

Author

    fazkal

Repository

github.com/fazkal/Blog-website-CBV-DRF-base
