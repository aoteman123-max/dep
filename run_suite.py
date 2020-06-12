import unittest

import HTMLTestRunner_PY3

import app
from script.test_dep import TestLogin

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
file_path=app.BASE_PATH+"/report/ihrm.html"
with open(file_path,mode="wb") as f:
    runnner=HTMLTestRunner_PY3.HTMLTestRunner(f,verbosity=1,title="ihrm系统部门管理模块",
                                              description="ihem接口测试报告")
    runnner.run(suite)