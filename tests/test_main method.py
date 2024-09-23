import requests
from tests.parameter.variable import URL, CRETE_USER
from tests.payload.create_user import CreateUser as cr, VariablesCreateUser as vcr
from lib.assertion import Assertions as a


class TestPositiveUser:
    # Проверка создания пользователя
    def test_create_user(self):
        payload, name, job = cr.positive_create(self)
        response = requests.post(URL + CRETE_USER,
                                 json=payload)

        a.assert_status_code(self, response, 201)
        a.assert_json_has_key(self, response, vcr.key)
        a.assert_json_value_by_name(self, response, 'name', name)

        user_id = response.json()['id']

        return user_id


