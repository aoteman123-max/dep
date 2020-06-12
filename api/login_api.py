import requests


class LoginApi:
    def __init__(self):
        self.login_url = "http://ihrm-test.itheima.net/api/sys/login"

    def test_login(self):
        response = requests.session().post(url=self.login_url,headers={"Content-Type":"application/json"},
                                 json={"mobile":"13800000002","password":"123456"})
        return response
