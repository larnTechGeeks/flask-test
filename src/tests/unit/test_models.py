from transapp.models import User

def test_user_id(new_user):
    """
    GIVEN an existing User
    WHEN the ID of the object is updated to a value
    THEN check the user ID returns a string (and not an integer) as needed by Flask-WTF
    """
    new_user.id = 234
    assert new_user.get_id() == '234'
    assert isinstance(new_user.get_id(), str)
    assert not isinstance(new_user.get_id(), int)


def test_new_user_with_fixture(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check if the email, password fields are defined correctly
    """
    assert new_user.email == 'admin@admin.com'
    assert new_user.password != 'admin'


def test_new_wallet_with_fixture(new_wallet):
    """
    GIVEN a Wallet Model, with exisiting user
    WHEN a new wallet is created
    THEN check if the balance, user id fields are defined correctly
    """
    assert new_wallet.balance == 1000
    assert new_wallet.user_id > 0

def test_new_transaction_with_fixture(new_transaction,new_user,  new_wallet):
    """
    GIVEN a Wallet Model, with exisiting user
    WHEN a new wallet is created
    THEN check if the balance, user id fields are defined correctly
    """
    assert new_transaction.user_id == new_user.id
    assert new_transaction.wallet_id == new_wallet.id
    assert new_transaction.account_type == "bank"
