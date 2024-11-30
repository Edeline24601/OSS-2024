from flask import Blueprint, render_template, request, flash, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import redirect

from todo_board import db
from todo_board.forms import UserLoginForm, UserSignUpForm
from todo_board.db_models import User


bp = Blueprint('auth', __name__, url_prefix="/auth")

@bp.route('/login/', methods=['GET', 'POST'])
def login():
    form = UserLoginForm()
    if (request.method == 'Post') and (form.validate_on_submit()):
        # TODO : complete qeury/check method
        error = False
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = True
            flash("no such user")
            return redirect(url_for('main.index')) # clear login screen
        elif not check_password_hash(user.password, form.password):
            error = True
            flash("Password does not match")
            return redirect(url_for('main.index')) # clear login screen

        if not error:
            session["user_id"] = user.id
            return redirect(url_for('todo.list')) # to main screen

    return render_template('auth/login.html', form=form)

@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.index'))

@bp.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = UserSignUpForm()
    if (request.method == 'POST') and (form.validate_on_submit()):
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            user = User(username = form.username.data,
                        password = generate_password_hash(form.password_check.data))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            flash("Account Already Taken")
            return redirect(url_for('auth.signup'))

    return render_template('auth/signup.html', form = form)