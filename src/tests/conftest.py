import pytest
from transapp import app, db
from transapp.models import User, Wallet, Transaction

@pytest.fixture(scope='module')
def test_client():
    """This method is used to initiate a testing client that will be used to in as an 
        interface for requests for tests.
    """

    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client

@pytest.fixture(scope='module')
def new_user():
    """A fixture used to create a sample user objet.
    """
    user = User('admin@admin.com',"admin", 'admin')
    return user


@pytest.fixture(scope='module')
def new_wallet(new_user):
    """A fixture used to create wallet object.
    """
    wallet = Wallet(1000, new_user.id)
    return wallet


@pytest.fixture(scope='module')
def new_transaction(new_user, new_wallet):
    """A fixture used to create a new transaction object
    """
    transaction = Transaction("credit", "3212621212121", "bank", new_user.id, new_wallet.id)
    return transaction


@pytest.fixture(scope='module')
def init_db():
    """A fixture used to create a new database interface for running tests.
    """

    db.create_all()
    db.session.commit()

    yield

    db.drop_all()

@pytest.fixture(scope='function')
def login_default_user(test_client):
    """A fixture used to get a logged in user to test closed endpoints wallet object.
    """
    test_client.post('/login',data=dict(email='admin@admin.com', username="admin2", password='admin'), follow_redirects=True)
    yield

    test_client.get('/logout', follow_redirects=True)
