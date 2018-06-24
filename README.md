# Welcome to the sqlinspector2!
Middleware that allow check the times applied and the SQL amount used on any request and response process on django 2.x

## Installation using PIP command
- Use the command "pip install sqlinspector2"
## Configuring sqlinspector2 on django project
- Add 'sqlinspector2' inside INSTALLED_APPS
- Add 'sqlinspector2.middleware.SqlInspectorMiddleware' inside MiDDLEWARE settings
- Set inside your settings.py the variable ENABLE_SQL_INSPECTOR by example:
```
ENABLE_SQL_INSPECTOR = True # If you want display the LOGS then set True else False
```
- You need configure the logging settings first and after to configure it, you need to add the following logger:
```
'sqlinspector2': {
      'handlers': ['console'], # You can add 'file' or email handler too
      'level': 'DEBUG',
      'propagate': True,
  },
```
- Run using the command "python manage.py runserver"