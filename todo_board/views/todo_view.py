from flask import Blueprint, render_template, request, url_for, flash
from werkzeug.utils import redirect

from todo_board import db
from todo_board.forms import TODOForm
from todo_board.db_models import TODO, User

bp = Blueprint('todo', __name__, url_prefix='/todo')

@bp.route('/list/')
def list():
    form = TODOForm()
    todo_list = TODO.query.order_by(TODO.date.desc())
    return render_template('todo_list.html', todo_list = todo_list)

@bp.route('/create/')
def create():

    return render_template(url_for('todo.list'))

@bp.route('/update/')
def update():

    return render_template(url_for('todo.list'))

@bp.route('/delete/')
def delete():

    return render_template(url_for('todo.list'))