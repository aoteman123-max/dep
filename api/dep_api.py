import requests

import app


class DepApi:
    def __init__(self):
        self.dep_url = "http://ihrm-test.itheima.net/api/company/department"

    def test_insert(self,token):
        response = requests.Session().post(url=self.dep_url,
                                           headers={"Content-Type ": "application/json", "Authorization": token},
                                           json={"name": "后勤部门00", "code": "1001", "manager": "喜羊0羊",
                                                 "introduce": "很好的一个部门"})
        return response
    def test_search(self,dep_id,token):
        response = requests.Session().get(url=self.dep_url+"/"+dep_id,
                                           headers={"Authorization": token})
        return response
    def test_update(self,dep_id,token):
        response = requests.Session().put(url=self.dep_url+"/"+dep_id,
                                           headers={"Content-Type ": "application/json", "Authorization": token},
                                           json={"name": "睡觉部门",})
        return response
    def test_delete(self,dep_id,token):
        response = requests.Session().delete(url=self.dep_url + "/" + dep_id,
                                          headers={"Content-Type ": "application/json", "Authorization": token})
        return response

