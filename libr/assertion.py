import json
from requests import Response

class Assertions:
    #Проверка кода ответа
    def assert_status_code(self, response: Response, expected_status_code):
        assert response.status_code == expected_status_code, f"Код ответа не соответствует ожидаемому! Ожидемый код: " \
                                                             f"{expected_status_code}. Код ответа: {response.status_code}"

    # Проверка наличия ключа в ответе
    def assert_json_has_key(self, response, names: list):
        if type(response) == Response:
            try:
                key_json = response.json()
                object_to_check = dict.keys(key_json)
            except:
                assert False, f"Ответ не в формате JSON. Текст ответа '{response.text}'"
        else:
            object_to_check = response

        for name in names:
            assert name in object_to_check, f"Ответ JSON не имеет ключей '{name}'"

    # Проверка правильности значения ключа в ответе если приходит один объект
    def assert_json_value_by_name(self, response, name, expected_value):
        if type(response) == Response:
            try:
                key_json = response.json()
                object_to_check = dict.keys(key_json)
            except:
                assert False, f"Ответ не в формате JSON. Текст ответа '{response.text}'"
        else:
            object_to_check = response

        assert name in object_to_check, f"Ответ JSON не имеет ключа '{name}'"
        assert key_json[name] == expected_value, f"Значение '{expected_value}' параметра '{name}' не " \
                                                 f"соответсвует ожидаемому {key_json['data'][name]}"


