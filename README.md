# todo-list-django-api-first

In order to validate the API using the API Blueprint spec, prepare Django by following these steps:

```
$ python manage.py migrate

(...)

$ python manage.py loaddata apib-fixture.json

(...)

$ python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
March 06, 2020 - 14:00:19
Django version 3.0, using settings 'todo_list.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Now, everything is set to run `dredd`:

```
$ dredd api-draft.apib http://127.0.0.1:8000

pass: GET (200) /tasks/ duration: 67ms
pass: POST (201) /tasks/ duration: 20ms
pass: GET (200) /tasks/1/ duration: 16ms
pass: PUT (200) /tasks/1/ duration: 20ms
pass: DELETE (204) /tasks/1/ duration: 13ms
complete: 5 passing, 0 failing, 0 errors, 0 skipped, 5 total
complete: Tests took 144ms
```

Dredd is a tool to validate contracts against a running service, and you can [read more about installing it ](https://dredd.org/en/latest/quickstart.html#install-dredd).
