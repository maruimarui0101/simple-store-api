import pytest
from models.store import StoreModel
from models.item import ItemModel

@pytest.fixture(scope="module")
def new_store():
    store = StoreModel('emptystore')
    return store

def test_new_user(new_store):
    """
    Given user model, assert that a user can be successfully created 
    """

    assert new_store.name == 'emptystore'
