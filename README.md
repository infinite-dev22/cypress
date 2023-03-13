# Cypress SMS

School Management System

## Run Locally For Tests

Clone the project

```bash
  git clone https://github.com/CyconeraInc/cypress
```

Go to the project directory

```bash
  cd cypress
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Create the database

```bash
  python manage.py makemigrations
  python manage.py migrate
```

Start the server

```bash
  python manage.py runserver
```

The system runs initially at http://localhost:8000

## Contributing

Contributions are always welcome!

See [`contributing.md`](https://github.com/CyconeraInc/cypress/blob/main/CONTRIBUTING.md) for ways to get started.

Please adhere to this
project's [`code of conduct`](https://github.com/CyconeraInc/cypress/blob/main/CODE_OF_CONDUCT.md).

