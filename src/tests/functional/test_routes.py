
def test_login_page(test_client):
    """
    GIVEN a Flask application routes
    WHEN the '/login' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/login')
    assert response.status_code == 200
    assert b'Login' in response.data
    assert b'Email' in response.data
    assert b'Password' in response.data


def test_valid_login_logout(test_client, init_db):
    """
    GIVEN a Flask application routes
    WHEN the '/login' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post('/login', data=dict(email='admin@admin.com', password='admin'), follow_redirects=True)
    assert response.status_code == 200

    """
    GIVEN a Flask application routes
    WHEN the '/logout' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Logout' not in response.data
    assert b'Login' in response.data
    assert b'Register' in response.data


def test_invalid_login(test_client, init_db):
    """
    GIVEN a Flask application routes
    WHEN the '/login' page is posted to with invalid credentials (POST)
    THEN check an error message is returned to the user
    """
    response = test_client.post('/login', data=dict(email='admin@admin.com', password='rusi'), follow_redirects=True)
    assert response.status_code == 200
    assert b'Logout' not in response.data
    assert b'Login' in response.data
    assert b'Register' in response.data


def test_login_already_logged_in(test_client, init_db, login_default_user):
    """
    GIVEN a Flask application routes
    WHEN the '/login' page is posted to (POST) when the user is already logged in
    THEN check an error message is returned to the user
    """
    response = test_client.post('/login', data=dict(email='patkennedy79@gmail.com', password='FlaskIsNotAwesome'), follow_redirects=True)
    assert response.status_code == 200


def test_valid_registration(test_client, init_db):
    """
    GIVEN a Flask application routes
    WHEN the '/register' page is posted to (POST)
    THEN check the response is valid and the user is logged in
    """
    response = test_client.post('/register',
                                data=dict(email='test12@test.com',
                                          password='test',
                                          confirm='test'),
                                follow_redirects=True)
    assert response.status_code == 200

def test_invalid_registration(test_client, init_db):
    """
    GIVEN a Flask application routes
    WHEN the '/register' page is posted to with invalid credentials (POST)
    THEN check an error message is returned to the user
    """
    response = test_client.post('/register',
                                data=dict(email='test12@gmail.com',
                                          password='test123',
                                          confirm='test'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'[This field is required.]' not in response.data
    assert b'Logout' not in response.data
    assert b'Login' in response.data
    assert b'Register' in response.data


def test_duplicate_registration(test_client, init_db):
    """
    GIVEN a Flask application routes
    WHEN the '/register' page is posted to (POST) using an email address already registered
    THEN check an error message is returned to the user
    """
    """This involves registering with one emil then retrying with another"""
    test_client.post('/register',data=dict(email='test@hotmail.com', password='test', confirm='test'), follow_redirects=True)
    response = test_client.post('/register', data=dict(email='test@hotmail.com@gmail.com', password='test', confirm='test'), follow_redirects=True)
    assert response.status_code == 200
    assert b'Login'  in response.data
    assert b'Register'  in response.data
