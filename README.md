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
- `pip install djangorestframework`
- `pip install djangorestframework-jwt`
- `pip install drf-yasg`
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


##### Create and Activate virtual environment
```shell
python3 -m venv .venv
sourve .venv/bin/activate
```

##### Apply Code Formate
```shell
ruff format .
```

##### Check linting
```shell
ruff check .
```

