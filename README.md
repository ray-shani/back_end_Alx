ALX Hub Access Management System

This project is a Django-based backend application that manages user access to the ALX Hub in Westlands. It replaces manual Google Sheets sign-ins with a secure system that categorizes users as Students, Alumni, Staff, or Community Members. The system allows administrators to track hub usage in real-time and ensure that only authorized people can access the space.

🚀 Features

User Management (CRUD):

Create a new user profile

Read/view user details

Update existing user information

Delete a user record

Role-based Categorization:

Users are identified as Student, Alumni, Staff, or Community Member.

Admin Panel:

Manage users via Django’s built-in admin interface.

REST API:

Exposed endpoints for programmatic user management.

API Integration (Optional):

Fetch sample users/emails from external APIs for testing.

📂 Project Structure
alx_hub_access/          # Django project root
│
├── alx_hub_access/      # Project settings and configuration
│   ├── __init__.py
│   ├── settings.py      # Project settings
│   ├── urls.py          # Root URL routes
│   └── wsgi.py
│
├── users/               # App handling user profiles
│   ├── __init__.py
│   ├── admin.py         # Register models in Django admin
│   ├── apps.py
│   ├── migrations/      # Database migrations
│   ├── models.py        # UserProfile model (name, email, status)
│   ├── serializers.py   # DRF serializer for UserProfile
│   ├── tests.py
│   ├── urls.py          # API endpoints for CRUD
│   └── views.py         # API views (CRUD logic)
│
├── db.sqlite3           # SQLite database
└── manage.py            # Django management tool


📡 API Endpoints

Base URL: http://127.0.0.1:8000/api/users/

Method	Endpoint	Description	Example Body
GET	/api/users/	Get all users	–
POST	/api/users/	Create a new user	{"name": "Alice", "email": "alice@example.com", "status": "student"}
GET	/api/users/{id}/	Get a single user by ID	–
PUT	/api/users/{id}/	Update a user completely	{"name": "Alice J", "email": "alicej@example.com", "status": "alumni"}
PATCH	/api/users/{id}/	Update a user partially	{"status": "staff"}
DELETE	/api/users/{id}/	Delete a user	–

👉 Note: status must be one of:

student

staff

alumni

community

🔑 Admin Access

Visit: http://127.0.0.1:8000/admin/

Log in with your superuser credentials.

Manage user profiles directly from the web UI.

🧪 Testing with Postman

Open Postman.

Use http://127.0.0.1:8000/api/users/ as the base URL.

Try each CRUD operation (Create, Read, Update, Delete) with JSON requests.

📌 Future Improvements

Add JWT Authentication to secure API endpoints.

Add check-in/check-out tracking with timestamps.

Generate hub usage reports by role (student, staff, alumni, community).
