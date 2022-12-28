call python -m venv venv
call venv\Scripts\activate
pip install random2 Django Pillow django-ckeditor
cd polyakov
python manage.py runserver 127.0.0.1:8000
start msedge http://127.0.0.1:8000/
pause
