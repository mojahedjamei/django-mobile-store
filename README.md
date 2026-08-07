# 📱 Django Mobile Store

A lightweight and efficient e-commerce web application developed with the Django Framework.  
This project demonstrates core backend engineering principles, focusing on product management, secure user authentication, and dynamic data rendering.

## 🌟 Key Features

- **Dynamic Product Catalog:** Custom database models using `DecimalField` for precise pricing and `ImageField` for handling product images.
- **Secure Authentication System:** Fully functional user registration (Signup), Login, and Logout capabilities integrated natively with Django's built-in authentication views and forms.
- **Modular Views & Routing:** Implementation of functional views to handle:
  - A curated Home page (displaying the 3 most recent items).
  - A comprehensive Product List page.
  - Individual Product Detail pages safely rendered using `get_object_or_404`.
- **Template Inheritance:** Structured and maintainable frontend using Django's template language (DTL), checking authentication states directly in the UI (`{% if user.is_authenticated %}`).

## 📁 Project File Structure

- **`models.py`:** Contains the `Item` model with automated timestamps (`created_at`, `updated_at`) and metadata configurations.
- **`views.py`:** Core backend logic handling user requests, database queries, and the `UserCreationForm` for secure onboarding.
- **`urls.py`:** URL routing configuration, including local development setup for serving media files.
- **`base.html`:** The foundational HTML layout providing the navigation bar and dynamic authentication states.

## 🛠️ Technology Stack

- **Backend:** Python, Django
- **Database:** SQLite (Default Development Database)
- **Frontend:** HTML5, CSS
- **Media Management:** Pillow (Python Imaging Library)

## 🚀 How to Run Locally

1. **Clone the repository** and navigate to the project directory.

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment and install the requirements:**

   ```bash
   # On Windows:
   venv\Scripts\activate

   # On macOS/Linux:
   source venv/bin/activate

   pip install django pillow
   ```

4. **Apply database migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

The application will be available at **http://127.0.0.1:8000/**.
