import pytest
from mimesis import Person
class CreateUser:
    def positive_create(self):
        person = Person('en')
        name_user = person.full_name()
        job_user = f'Individual Entrepreneur "{name_user}"'
        payload = {"name": name_user,
                   "job": job_user}
        return payload, name_user, job_user

class VariablesCreateUser():
    key = ['id', 'createdAt', 'name', 'job']