"""
Pokemonbattle.
Test project.
"""
import pytest

from faker import Faker
from pytest_voluptuous import S
from common.helper.schema.trainer import valid_trainer, error_trainer, update_trainer


class TestTrainers():
    """
    Tests for trainers
    """
    CASE_TRAINERS = [
        {'id': None, 'status_code': 200},
        {'id': 1482, 'status_code': 200}
    ]
    
    @pytest.mark.parametrize('case', CASE_TRAINERS)
    def test_get_trainer(self, case, api):
        """
        Get trainers
        """
        response = api.get_trainer(trainer_id=case['id'])

        api.status_code_should_be(case['status_code'])

        if response.response.status_code in [400, 404]:
            assert response.response.json()['message'] == "Тренер отсутствует", ''
