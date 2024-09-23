class UpdateUser:
    def positive_update(self, name):
        job_user = f'Company "{name}"'
        payload = {"name": name,
                   "job": job_user}
        return payload, job_user

class VariablesUpdateUser():
    key = ['updatedAt', 'name', 'job']