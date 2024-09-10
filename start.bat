echo Please Wait Process Started
echo off

call color 05

echo :::-:-::: Starting fatmag Backend :::-:-:::
echo ======__-_-__-_-_-__-_-_-__-_-_-__-_-_-__-=======__-_-_-__-_-_-__-_-_-__-=======
echo 

@REM Activate the virtual environment
call python -m venv menv
echo activating the virtual environments
call menv\Scripts\activate.bat
echo :::-:-::: activated :::-:-:::
echo =======__-_-__-_-_-__-_-_-__-_-_-__-_-_-__-=======__-_-_-__-_-_-__-_-_-__-=======

rem Install requirements
echo Installing the all requirements
echo :::-:-::: Installing.... :::-:-:::
echo ======__-_-__-_-_-__-_-_-__-_-_-__-_-_-__-=======__-_-_-__-_-_-__-_-_-__-=======
pip install -r requirements.txt
echo :::-:-::: Installed :::-:-:::
echo ======__-_-__-_-_-__-_-_-__-_-_-__-_-_-__-=======__-_-_-__-_-_-__-_-_-__-=======


@REM  Run Django migrations
@REM python manage.py makemigrations
@REM echo :::-:-::: migrating the DB.... :::-:-:::
python manage.py migrate
@REM echo :::-:-::: Ohoo! DB migrated!.... :::-:-:::

@REM  Start the Django development server
echo :::-:-::: starting The Server.... :::-:-:::
echo :::-:-::: Server started .... :::-:-:::
echo ======__-_-__-_-_-__-_-_-__-_-_-__-_-_-__-=======__-_-_-__-_-_-__-_-_-__-=======
echo ======__-_-__-_-_-__-_-_-__-_-_-__-_-_-__-=======__-_-_-__-_-_-__-_-_-__-=======
echo :::-:-::: Happy Coding! .... :::-:-:::

@REM comment out if working on local machine
python manage.py runserver 8000

@REM comment out if working on production note- this is importent for the Docker
@REM gunicorn --bind 0.0.0.0:8000 fatmag.wsgi
pause