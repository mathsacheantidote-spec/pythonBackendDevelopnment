# Django project

A small Django project with a homepage served by the `app` application.

## Run on Windows

From this directory, create and activate a virtual environment, then install dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ to view the homepage.

For deployments, set a stable `DJANGO_SECRET_KEY` environment variable. A random key is generated automatically for local development when it is unset.
