from flask import Blueprint, render_template, request, flash, session
from werkzeug.security import check_password_hash
from werkzeug.utils import redirect

from todo_board import db
from todo_board.forms import UserLoginForm
from todo_board.db_models import User


bp = Blueprint('auth', __name__, url_prefix="/auth")

@bp.route('/login/', methods=('GET, POST'))
def login():
    form = UserLoginForm()
    if (request.method == 'Post') and (form.validate_on_submit()):
        # TODO : complete qeury/check method
        error = False
        user = User.query
        if not user:
            error = True
            flash("no such user")
            return redirect() # clear login screen
        elif not check_password_hash(user.password, form.password):
            error = True
            flash("Password does not match")
            return redirect() # clear login screen

        if not error:
            session["user_id"] = user.id
            return redirect() # to main screen

@bp.route('logout')
def logout():
    session.clear()
    # TODO : return to main screen
    return redirect(url_for())




    return render_template('auth/login.html', form = form)