SET INSTALL_PATH=C:\Users\Jerry\Desktop\code\venv3\Scripts
SET PRJ_NAME=ttsx.ttsx
PATH = %INSTALL_PATH%;%PATH%;%INSTALL_PATH%\Scripts;
SET DJANGO_SETTINGS_MODULE=%PRJ_NAME%.settings

CALL python -V
CALL pip list
PAUSE

ECHO Let's go!
%INSTALL_PATH%\python manage.py runserver  0.0.0.0:8000

