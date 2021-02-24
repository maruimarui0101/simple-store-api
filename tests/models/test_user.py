import pytest
from models.user import UserModel

@pytest.fixture(scope="module")
def new_user():
    user = UserModel('patkennedy79@gmail.com', 'FlaskIsAwesome')
    return user

def test_new_user(new_user):
    """
    Given user model, assert that a user can be successfully created 
    """

    assert new_user.username == 'patkennedy79@gmail.com'
    assert new_user.password == 'FlaskIsAwesome'
