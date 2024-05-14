"""
Conftest file
"""
import pytest

from common.api.trainer import TrainerApi
from common.api.pokemons import PokemonApi
from common.helper.conf import Credential

@pytest.fixture(scope="session")
def api():
    """
    basic api fixture
    """
    trainer_api = TrainerApi()
    yield trainer_api

@pytest.fixture(scope="session")
def token():
    """
    Receive admin token 
    """
    yield Credential.trainer_token
