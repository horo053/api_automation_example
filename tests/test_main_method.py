import requests
from libr.variable import URL, URL_FOR_MAIN_METHOD
from tests.payload.create_user import CreateUser as cr, VariablesCreateUser as vcr
from tests.payload.update_user import UpdateUser as up, VariablesUpdateUser as vur
from libr.assertion import Assertions as a


class TestPositiveUser:
    # Проверка создания пользователя
    def test_create_user(self):
        payload, name, job = cr.positive_create(self)
        response = requests.post(URL + URL_FOR_MAIN_METHOD,
                                 json=payload)

        a.assert_status_code(self, response, 201)
        a.assert_json_has_key(self, response, vcr.key)

        a.assert_json_value_by_name(self, response, 'name', name)
        a.assert_json_value_by_name(self, response, 'job', job)

    # Проверка изменения пользователя
    def test_update_user(self, create_user):
        user_id, name = create_user
        payload, job = up.positive_update(self, name)
        response = requests.put(URL + URL_FOR_MAIN_METHOD + f'/{user_id}',
                                json=payload)

        a.assert_status_code(self, response, 200)
        a.assert_json_has_key(self, response, vur.key)

        a.assert_json_value_by_name(self, response, 'name', name)
        a.assert_json_value_by_name(self, response, 'job', job)

    # Удаление пользователя
    def test_delete_user(self, create_user):
        user_id, name = create_user
        response = requests.delete(URL + URL_FOR_MAIN_METHOD + f'/{user_id}')

        a.assert_status_code(self, response, 204)