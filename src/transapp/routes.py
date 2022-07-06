from datetime import date
from anyio import wait_all_tasks_blocked
from flask import render_template, url_for, flash, redirect, request
from transapp.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required
from transapp.models import User, Transaction, Wallet
from transapp import app, db
from transapp.utils import Util


@app.route("/", methods=['GET', 'POST'])
@login_required
def index():
    """This is the default view function, it returns a list of transactions for a logged in user.
        """

    transactions = Transaction.query.filter_by(user_id = current_user.id).all()[:5]
    wallet = Wallet.query.filter_by(user_id = current_user.id).first()

    return render_template('index.html', transactions=transactions, wallet=wallet)


@app.route("/transactions", methods=['GET', 'POST'])
@login_required
def transactions():

    """This view function returns a list of all logged in users transacrions and 
        gives a provision to filter transactions by date.
    """

    start_date = None
    end_date = None

    if request.method == "POST":
        start_date, success = Util.parse_string_to_date(request.form.get("start"))
        if not success:
            flash('You have entered wrong date format', 'warning')
            return redirect(url_for('index'))
        end_date, success = Util.parse_string_to_date(request.form.get("end"))
        if not success:
            flash('You have entered wrong date format', 'warning')
            return redirect(url_for('index'))

    if end_date is not None:
        transactions = Transaction.query.filter_by(user_id = current_user.id).filter(Transaction.transaction_date <= end_date).filter(Transaction.transaction_date >= start_date).all()
    else:
        transactions = Transaction.query.filter_by(user_id = current_user.id).all()
    return render_template('transactions.html', transactions=transactions)


@app.route("/register", methods=['GET', 'POST'])
def register():
    """This view function, is used to register new users to the system. Handles forms authentications
        and creation of new user objects.
    """

    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Sign Up', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    """This view function, handles logging in users into the system and setting sessions for 
        logged in users.
    """

    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.compare_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('signin.html', title='Login', form=form)


@app.route("/logout")
def logout():
    """This view function, handles logging users out of the system and destroying sessions for 
        logged in users.
    """
    logout_user()
    return redirect(url_for('login'))
