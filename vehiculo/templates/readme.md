pip install virtualenvwrapper
pip install virtualenv virtualenvwrapper-win
workon
C:\Windows>workon proyecto_vehiculos_django
(proyecto_vehiculos_django) C:\Windows>cd "C:\Users\csgut\Documents\Bootcamp python 0069 (2024)\REPO\Codeo en clases\DJANGO_APP\proyecto_vehiculos_django>"
(proyecto_vehiculos_django) C:\Users\csgut\Documents\Bootcamp python 0069 (2024)\REPO\Codeo en clases\DJANGO_APP\proyecto_vehiculos_django>pip install Django==4.0.5
(proyecto_vehiculos_django) C:\Users\csgut\Documents\Bootcamp python 0069 (2024)\REPO\Codeo en clases\DJANGO_APP\proyecto_vehiculos_django>pip install django-bootstrap-v5==1.0.11
(proyecto_vehiculos_django) C:\Users\csgut\Documents\Bootcamp python 0069 (2024)\REPO\Codeo en clases\DJANGO_APP\proyecto_vehiculos_django>pip install django-crispy-forms==1.14.0
(proyecto_vehiculos_django) C:\Users\csgut\Documents\Bootcamp python 0069 (2024)\REPO\Codeo en clases\DJANGO_APP\proyecto_vehiculos_django>pip install crispy-bootstrap5==0.6
(proyecto_vehiculos_django) C:\Users\csgut\Documents\Bootcamp python 0069 (2024)\REPO\Codeo en clases\DJANGO_APP\proyecto_vehiculos_django>django-admin startproject proyecto_vehiculos_django

(proyecto_vehiculos_django) C:\Users\csgut\Documents\Bootcamp python 0069 (2024)\REPO\Codeo en clases\DJANGO_APP\proyecto_vehiculos_django>cd proyecto_vehiculos_django

(proyecto_vehiculos_django) C:\Users\csgut\Documents\Bootcamp python 0069 (2024)\REPO\Codeo en clases\DJANGO_APP\proyecto_vehiculos_django\proyecto_vehiculos_django>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
October 23, 2024 - 23:06:17
Django version 4.0.5, using settings 'proyecto_vehiculos_django.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[23/Oct/2024 23:06:28] "GET / HTTP/1.1" 200 10697
[23/Oct/2024 23:06:28] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
[23/Oct/2024 23:06:28] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
[23/Oct/2024 23:06:28] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
[23/Oct/2024 23:06:28] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
Not Found: /favicon.ico
[23/Oct/2024 23:06:28] "GET /favicon.ico HTTP/1.1" 404 2129

(proyecto_vehiculos_django) C:\Users\csgut\Documents\Bootcamp python 0069 (2024)\REPO\Codeo en clases\DJANGO_APP\proyecto_vehiculos_django\proyecto_vehiculos_django>python manage.py startapp vehiculo

(proyecto_vehiculos_django) C:\Users\csgut\Documents\Bootcamp python 0069 (2024)\REPO\Codeo en clases\DJANGO_APP\proyecto_vehiculos_django\proyecto_vehiculos_django>python manage.py makemigrations
Migrations for 'vehiculo':
  vehiculo\migrations\0001_initial.py
    - Create model Vehiculo

(proyecto_vehiculos_django) C:\Users\csgut\Documents\Bootcamp python 0069 (2024)\REPO\Codeo en clases\DJANGO_APP\proyecto_vehiculos_django\proyecto_vehiculos_django>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, vehiculo
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
  Applying vehiculo.0001_initial... OK

(proyecto_vehiculos_django) C:\Users\csgut\Documents\Bootcamp python 0069 (2024)\REPO\Codeo en clases\DJANGO_APP\proyecto_vehiculos_django\proyecto_vehiculos_django>python manage.py createsuperuser
Username (leave blank to use 'csgut'): leadmin
Email address: csgutier@gmail.com
Password:
Password (again):
Superuser created successfully.

(proyecto_vehiculos_django) C:\Users\csgut\Documents\Bootcamp python 0069 (2024)\REPO\Codeo en clases\DJANGO_APP\proyecto_vehiculos_django\proyecto_vehiculos_django>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 23, 2024 - 23:15:23
Django version 4.0.5, using settings 'proyecto_vehiculos_django.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[23/Oct/2024 23:15:28] "GET / HTTP/1.1" 200 10697
[23/Oct/2024 23:15:28] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
Not Found: /favicon.ico
[23/Oct/2024 23:15:28,159] - Broken pipe from ('127.0.0.1', 56910)

[23/Oct/2024 23:16:08] "GET /admin HTTP/1.1" 301 0
[23/Oct/2024 23:16:08] "GET /admin/ HTTP/1.1" 302 0
[23/Oct/2024 23:16:08] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 2215
[23/Oct/2024 23:16:08] "GET /static/admin/css/login.css HTTP/1.1" 200 954
[23/Oct/2024 23:16:08] "GET /static/admin/css/nav_sidebar.css HTTP/1.1" 200 2616
[23/Oct/2024 23:16:08] "GET /static/admin/css/base.css HTTP/1.1" 200 19513
[23/Oct/2024 23:16:08] "GET /static/admin/css/responsive.css HTTP/1.1" 200 18575
[23/Oct/2024 23:16:08] "GET /static/admin/js/nav_sidebar.js HTTP/1.1" 200 3763
[23/Oct/2024 23:16:43] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0
[23/Oct/2024 23:16:43] "GET /admin/ HTTP/1.1" 200 4001
[23/Oct/2024 23:16:44] "GET /static/admin/css/dashboard.css HTTP/1.1" 200 380
[23/Oct/2024 23:16:44] "GET /static/admin/img/icon-changelink.svg HTTP/1.1"

Username (leave blank to use 'csgut'): leadmin
Email address: csgutier@gmail.com
checkpass


claudio
superpass



***20241112 modificaciones de registro en página...
comandos en orden inverso

(proyecto_vehiculos_django) C:\Users\csgut\Documents\Bootcamp python 0069 (2024)\REPO\Codeo en clases\DJANGO_APP\proyecto_vehiculos_django\proyecto_vehiculos_django>python manage.py runserver

workon proyecto_vehiculos_django

