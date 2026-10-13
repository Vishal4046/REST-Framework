# Django REST Framework

A beginner-friendly project built using **Python, Django, and Django REST Framework (DRF)** to learn REST API development and backend programming.

## 🚀 Features

* Django REST Framework setup
* REST API development
* JSON data serialization using serializers
* API request and response handling
* Django models and database integration
* CRUD operations (Create, Read, Update, Delete)

## 🛠️ Technologies Used

* Python
* Django
* Django REST Framework
* SQLite / MySQL
* Git and GitHub

## 📁 Project Structure

```text
firstproject/
├── firstproject/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── userapp/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── tests.py
├── manage.py
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Vishal4046/REST-Framework.git
cd REST-Framework
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install django djangorestframework
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open the application at:

http://127.0.0.1:8000/

## 🔌 API Development

Django REST Framework helps build RESTful APIs that exchange data in JSON format.

The project includes a `serializers.py` file for converting model instances and other data into formats suitable for API responses and validating incoming data.

API endpoints depend on the URL patterns and views configured in the project.

## 📚 Learning Objectives

* Understand REST API concepts
* Learn serializers and data validation
* Work with Django models and views
* Handle HTTP methods such as GET, POST, PUT, PATCH, and DELETE
* Test APIs using a browser or Postman

## 👨‍💻 Author

**Vishal Patil**

* GitHub: [Vishal4046](https://github.com/Vishal4046)

## 📄 License

This project is intended for learning and educational purposes.
