Simple Todo App Using Flask
===
---

# 1. Prerequisite (Development Environment)
- Debian 12 (or WSL2 Debian)
- Python 3.11.2
## 1.1 Setting up with Python Virtual environment

In project Directory, type in following commands.<br>

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install flask
pip install flask-wtf
pip install flask_migrate
pip install sqlalchemy
```
## 1.2 Firing up project
Type in following command in project Directory, to run flask app.
```bash
flask --app todo_board db init
flask --app todo_board db migrate
flask --app todo_board db upgrade
flask --app todo_board run
```

# 2. Using app
Refer to Attached "guide.pdf" PDF. <br>
(Screenshots cannot be seen via github page, so using PDF instead to explain how to use this project)