Product Catalog Django
A full-fledged Django application for managing a product catalog with features such as adding, editing, deleting, and viewing products. This project is a great showcase for Django development, demonstrating the power of web frameworks in building robust and scalable web applications.

Features
Product Management: Add, edit, and delete products with essential details such as name, description, price, and image.

User Authentication: Secure user authentication using Django’s built-in authentication system.

Product Search: Search for products by name or category.

Responsive Design: Fully responsive UI, built with Bootstrap, to ensure compatibility across all devices.

Admin Panel: Easy management of products through Django's admin interface.

Installation
Prerequisites
Python 3.8+

Django 3.2+

PostgreSQL (optional, for production use)

Setup
Clone the repository:

bash
Copy
Edit
git clone https://github.com/arunabhasarkar1999/product_catalog.git
cd product_catalog
Create a virtual environment and activate it:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Apply migrations:

bash
Copy
Edit
python manage.py migrate
Create a superuser (for Django admin access):

bash
Copy
Edit
python manage.py createsuperuser
Run the development server:

bash
Copy
Edit
python manage.py runserver
Open the application in your browser:

bash
Copy
Edit
http://127.0.0.1:8000/
Configuration (Optional)
Configure PostgreSQL database by editing the DATABASES setting in settings.py.

Set DEBUG = False for production and configure static and media files handling.

Usage
Home Page: View a list of all available products.

Product Detail Page: View detailed information about each product.

Admin Panel: Manage products, users, and categories from the admin panel at http://127.0.0.1:8000/admin/.

Technologies Used
Django: Python-based web framework for rapid development.

PostgreSQL: Relational database used for storing product data.

Bootstrap: Frontend framework used for responsive UI design.

SQLite: Default development database.

Contributing
Fork the repository.

Create a new branch (git checkout -b feature-name).

Make your changes and commit them (git commit -m 'Add feature').

Push your changes to your forked repository (git push origin feature-name).

Open a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
Author: Arunabha Sarkar

GitHub: @arunabhasarkar1999
