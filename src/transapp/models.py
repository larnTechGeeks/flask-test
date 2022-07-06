from email.policy import default
from transapp import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from transapp import  bcrypt

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):

    __tablename__ = "users"

    def __init__(self, email, username, password):
        """Creates a new User object using the email address and hashing the
        form password using bcrypt.
        """
        self.email = email
        self.username = username
        self.password = self._generate_password_hash(password)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    transactions = db.relationship('Transaction', backref='owner', lazy=True)
    wallet = db.relationship('Wallet', backref='owner', lazy=True)

    def __repr__(self):
        """Returns the string representation of the object of the User class.
        """
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

    def compare_password(self, password_plaintext):
        """Returns true if the value of hashed_password is equal to the passed plain_password.
        """
        return bcrypt.check_password_hash(self.password, password_plaintext)

    def set_password(self, password_plaintext):
        """Used to update the value of password for an object.
        """
        self.password = self._generate_password_hash(password_plaintext)

    """The static class methods are helpers used by tests to test the Models.
        """
    @staticmethod
    def _generate_password_hash(password_plaintext):
        return bcrypt.generate_password_hash(password_plaintext).decode('utf-8')

    @property
    def is_active(self):
        """Always True, as all users are active."""
        return True

    def get_id(self):
        """Return the user ID as a unicode string (`str`)."""
        return str(self.id)


class Wallet(db.Model):

    __tablename__ = "wallets"

    def __init__(self, balance, user_id,):
        """Creates a new Wallet object using balance and user_id.
        """
        self.balance = balance
        self.user_id = user_id

    id              = db.Column(db.Integer, primary_key=True)
    balance         = db.Column(db.Float, nullable=False)
    user_id         = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    transactions    = db.relationship('Transaction', backref='wallet', lazy=True)

    def __repr__(self):
        """Returns the string representation of the object of the Wallet class.
        """
        return f"Wallet('{self.balance}')"

class Transaction(db.Model):

    __tablename__ = "transactions"

    def __init__(self, type, account_number, account_type, user_id, wallet_id):
        """Creates a new Transaction object using the type, account_number, 
        account_type, receiver, amount, user id and wallet id.
        """
        self.type = type
        self.account_number = account_number
        self.account_type = account_type
        self.wallet_id = wallet_id
        self.user_id = user_id

    id                  = db.Column(db.Integer, primary_key=True)
    receiver            = db.Column(db.String(100), nullable=False)
    type                = db.Column(db.String(100), nullable=False)
    account_number      = db.Column(db.String(100), primary_key=True)
    account_type        = db.Column(db.String(100), primary_key=True)
    amount              = db.Column(db.Float, default=1000)
    transaction_date    = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id             = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    wallet_id           = db.Column(db.Integer, db.ForeignKey('wallets.id'), nullable=False)

    def __repr__(self):
        """Returns the string representation of the object of the Transaction class.
        """
        return f"Transaction('{self.type}', '{self.transaction_date}')"

