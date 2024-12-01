import datetime

from flask import Blueprint, render_template, request, url_for, flash
from werkzeug.utils import redirect

from todo_board import db
from todo_board.forms import TODOForm
from todo_board.db_models import TODO

bp = Blueprint('todo', __name__, url_prefix='/todo')

@bp.route('/list/')
def list():
    form = TODOForm()
    todo_list = TODO.query.order_by(TODO.date.desc()).all()
    return render_template('todo_list.html', todo_list = todo_list, form = TODOForm)

@bp.route('/create/', methods=['POST'])
def create():
    form = TODOForm()
    if form.validate_on_submit():
        new_todo = TODO(
            date = datetime.datetime().now(),
            content = form.content.data,
            priority = form.priority.data,
            done = False
        )

        db.session.add(new_todo)
        db.session.commit()
    else:
        flash("cannot add TODO, failed form validation")
    return redirect(url_for('todo.list'))

@bp.route('/update/<int:todo_id>/', methods=['POST'])
def update(todo_id):
    todo = TODO.query.get_or_404(todo_id)
    # Toggle the 'done' status
    todo.done = not todo.done
    db.session.commit()
    return redirect(url_for('todo.list'))

@bp.route('/delete/<int:todo_id>/', methods=['POST'])
def delete(todo_id):
    todo = TODO.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    flash('TODO deleted successfully!', 'success')
    return redirect(url_for('todo.list'))