import logging
import unittest

import app
from api.dep_api import DepApi
from api.login_api import LoginApi
import warnings

from until import dep_assert


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", ResourceWarning)

    def setUp(self):
        self.login = LoginApi()
        self.dep_api = DepApi()

    def test01_login(self):
        response = self.login.test_login()
        # print("登陆结果：", response.json())
        logging.info("登陆页面：{}".format(response.json()))
        app.TOKEN = "Bearer " + response.json().get("data")
        # self.assertEqual(200,response.status_code)
        # self.assertEqual(True,response.json().get("success"))
        # self.assertEqual(10000,response.json().get("code"))
        # self.assertEqual("操作成功！",response.json().get("message"))
        # print(TOKEN)
        dep_assert(self,200,True,10000,"操作成功！",response)

    def test02_insert(self):
        response = self.dep_api.test_insert(app.TOKEN)
        # print("添加页面结果：", response.json())
        logging.info("添加页面：{}".format(response.json()))
        app.DEP_ID = response.json().get("data").get("id")
        # print(app.DEP_ID)
        dep_assert(self,200,True,10000,"操作成功！",response)

    def test03_search(self):
        response = self.dep_api.test_search(app.DEP_ID, app.TOKEN)
        # print("查询结果：", response.json())
        logging.info("查询页面：{}".format(response.json()))
        dep_assert(self, 200, True, 10000, "操作成功！", response)

    def test04_update(self):
        response = self.dep_api.test_update(app.DEP_ID, app.TOKEN)
        # print("修改结果：", response.json())
        logging.info("修改页面：{}".format(response.json()))
        dep_assert(self,200,True,10000,"操作成功！",response)

    def test05_delete(self):
        response = self.dep_api.test_delete(app.DEP_ID, app.TOKEN)
        # print("删除结果：", response.json())
        logging.info("删除页面：{}".format(response.json()))
        dep_assert(self,200,True,10000,"操作成功！",response)
