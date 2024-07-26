# Institute Management System

## Overview

The Institute Management System is a Django-based web application designed to manage various aspects of an educational institute. It includes features for managing students, teachers, clubs, and books. The system supports user registration, profile management, and CRUD operations for different entities.

## Features

- **User Registration & Authentication**: Users can register, log in, and manage their profiles.
- **Student Management**: CRUD operations for student data including full name, date of birth, date of joining, and address.
- **Teacher Management**: CRUD operations for teacher data including full name, date of birth, date of joining, address, and compensation.
- **Club Management**: CRUD operations for club data including name, description, founded date, president, and members count.
- **Book Management**: CRUD operations for book data including title, author, published date, ISBN, pages, and language.

## Technologies Used

- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Python, Django
- **Database**: SQLite
- **JavaScript**: For form validation and dynamic interactions

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/institute-management-system.git
   cd institute-management-system
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

   On Windows:
   ```bash
   venv\Scripts\activate
   ```

   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install the Requirements**

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/` in your browser to access the application.

## Usage

1. **Registration**: Users can register by providing their name, email, password, and other details. Profile pictures can also be uploaded.

2. **Profile Management**: After logging in, users can update their profile details including name, email, mobile number, and institute name. Profile picture updates are also supported.

3. **Student Management**: Admins can create, view, edit, and delete student records.

4. **Teacher Management**: Admins can manage teacher records similarly to student records.

5. **Club Management**: Admins can manage club records, including adding new clubs, editing existing ones, and deleting clubs.

6. **Book Management**: Admins can manage book records, including adding new books, editing details, and deleting books.

## File Structure

- `manage_institute/`: Contains the main Django app files.
  - `models.py`: Defines the models for students, teachers, clubs, and books.
  - `views.py`: Contains the view functions for handling requests and rendering templates.
  - `urls.py`: URL routing configuration.
  - `templates/`: Contains HTML templates for the project.
    - `base.html`: Base template with common layout elements.
    - `profile.html`: User profile management page.
    - `edit_student.html`: Page for editing student records.
    - `edit_teacher.html`: Page for editing teacher records.
    - `create_teacher.html`: Page for creating new teacher records.
    - `create_club.html`: Page for creating new club records.
    - `create_book.html`: Page for creating new book records.
    - `edit_club.html`: Page for editing club records.
    - `create_student.html`: Page for creating new student records.
    - `edit_book.html`: Page for editing book records.





