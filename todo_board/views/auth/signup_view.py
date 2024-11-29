from flask import Blueprint, render_template, request, url_for, flash
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

from todo_board import db
from todo_board.db_models import User
from todo_board.forms import UserSignUpForm

bp = Blueprint('auth', __name__, url_prefix="/auth")

@bp.route('/signup/', methods=('GET, POST'))
def signup():
    form = UserSignUpForm()
    if (request.method == 'POST') and (form.validate_on_submit()):
        # TODO : complete query/add method
        user = User.query
        if not user:
            user = User()
            db.session.add(user)
            db.session.commit()
            return redirect(url_for(''))
        else:
            flash("Account Already Taken")
            return redirect()


    return render_template('auth/login.html', form = form)