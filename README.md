# sqlinspector2
Middleware that allow check the times applied and the SQL amount used on any request and response process on django 2.x

## Installation using PIP command
1) Use the command "pip install sqlinspector2"
2) Add 'sqlinspector2' inside INSTALLED_APPS
3) Add 'sqlinspector2.middleware.SqlInspectorMiddleware' inside MiDDLEWARE settings
4) You need configure the logging settings first and after to configure it, you need to add the following logger: 

'sqlinspector2': {
      'handlers': ['console'], # You can add 'file' or email handler too
      'level': 'DEBUG',
      'propagate': True,
  },
