import pytest
import json
from pprint import pprint

from test_api.api.usermanagement import UserManagement, usermanagement


@pytest.fixture()
def login_code():
    # 登录返回值
    code, token = usermanagement.login_admin()
    return code, token


@pytest.fixture()
def Institutional_information_get():
    #获取机构信息
    return usermanagement.Institutional_information_get()


@pytest.fixture()
def Obtaining_Institutional_Configuration_Information():
    #获取机构配置信息
    return usermanagement.Obtaining_Institutional_Configuration_Information()

@pytest.fixture()
def user_add():
    usermanagement.user_add()

usermanagement.login_admin()
usermanagement.Obtaining_Institutional_Configuration_Information()


print(usermanagement.url)
pprint(dict(usermanagement.header_print))
print(' ')
pprint(json.loads(usermanagement.response_text))
