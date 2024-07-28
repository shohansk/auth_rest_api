<div align="center">
    <h1>REST AUTH</h1>
    <h4>Django Rest Auth API</h4>
</div>

---


<div align="center">
    <img src="https://img.shields.io/badge/Python-3.10-green" />
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" />
</div>

---


---

## Indexes
- [Prerequisites](#prerequisites)
- [Project Setup](#project-setup)
- [Database Setup in Docker (Optional - Local)](#database-setup-in-docker-optional---local)
- [Create and Activate virtual environment](#create-and-activate-virtual-environment)
- [Install libraries](#install-libraries)
- [Apply format](#apply-code-formate)

---

### Prerequisites
- Python >= 3.9
- PostgreSQL

### Database setup in Docker (Optional - Local)
```shell
1. docker run -p 5432:5432 --name db -e POSTGRES_PASSWORD=postgres -d postgres:14
2. docker exec -it db bash
3. su - postgres
4. psql
5. create database 'database_name';
6. create user 'database_user' with encrypted password 'password';
7. grant all privileges on database 'database_name' to 'database_user';
8. exit 
```

### Project Setup:
```shell
1. git clone https://github.com/shohansk/auth_rest_api.git
2. git switch development
```
**Notes:**

***NB: Please convert the `env.example` to `.env` and put all necessary credentials*** 

##### Create and Activate virtual environment
```shell
1. python3 -m venv .venv
2. sourve .venv/bin/activate

```
##### For Run Project
```shell
1. pip install -r requirements.txt
2. python manage.py makemigrations
3. python manage.py migrate
4. python manage.py createsuperuser
5. python manage.py runserver
```
**Notes:**

***NB: For Doc (http://127.0.0.1:8000/redoc/)*** 

##### Apply Code Formate
```shell
ruff format .
```

##### Check linting
```shell
ruff check .
```

