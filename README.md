Django Capstone Project
Overview

This is a Django-based capstone project demonstrating version control (Git), documentation (Sphinx), and containerisation (Docker). The project is built using Django and follows proper development workflows including branching, documentation generation, and container deployment.

🚀 Setup Instructions (Local Development)
1. Clone the repository
git clone https://github.com/JanieGrove28/django-capstone.git
cd django-capstone
2. Create a virtual environment
python -m venv venv

Activate it:

Windows:

venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Run database migrations
python manage.py migrate
5. Create superuser (optional)
python manage.py createsuperuser
6. Run the development server
python manage.py runserver

Open in browser:
http://127.0.0.1:8000/

🐳 Docker Setup
Build Docker image
docker build -t django-capstone .
Run Docker container
docker run -p 8000:8000 django-capstone

Open:
http://localhost:8000/

📚 Sphinx Documentation
Generate documentation
cd docs
sphinx-build source _build/html
View documentation
docs/_build/html/index.html
📁 Project Structure

config/ → Django project settings
store/ → Django app
templates/ → HTML templates
static/ → CSS files
docs/ → Sphinx documentation
Dockerfile → Container setup
requirements.txt → Python dependencies
manage.py → Django entry point

⚠️ Notes
Do NOT commit secrets (SECRET_KEY, passwords)
venv folder is excluded using .gitignore
Docker must be installed to run container version
👩‍💻 Author

Janie Grové
