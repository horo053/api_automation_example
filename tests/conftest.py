import pytest
import requests
from mimesis import Person
from libr.variable import URL, URL_FOR_MAIN_METHOD

@pytest.fixture
def create_user():
    person = Person('en')
    name_user = person.full_name()
    job_user = f'Individual Entrepreneur "{name_user}"'
    payload = {"name": name_user,
               "job": job_user}

    response = requests.post(URL + URL_FOR_MAIN_METHOD,
                                 json=payload)
    user_id = response.json()['id']

    return user_id, name_user