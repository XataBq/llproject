@REM start msedge http://0.0.0.0:8000/
call venv\Scripts\activate
cd polyakov
python manage.py runserver 0.0.0.0:8000
