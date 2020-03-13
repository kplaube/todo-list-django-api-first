# TODO List with Django and API-First

This is a pet project used to ilustrate how to approach web development with Django + API-First.

It's based on an article of my own, ["API-First: Process and tools"](https://medium.com/@kplaube/api-first-process-and-tools-b16ae90d2a5c), and in different
references cited in this article.

## Installing

Make sure you have [pipenv](https://pipenv.readthedocs.io/en/latest/) and Python>=3.6 installed.

You can start by cloning the project and installing its dependencies:

```shell
$ git clone git@github.com:kplaube/todo-list-django-api-first.git

$ cd todo-list-django-api-first
$ pipenv install
```

## Running

To see the API working, you can use Django's development server:

```shell
$ pipenv run python manage.py migrate

(...)

$ pipenv run python manage.py runserver
```

You should get something on `localhost:8000`.

### Validating the schema

In order to validate the API using the API Blueprint spec, prepare Django by following these steps:

```
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
