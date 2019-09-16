import pytest
import json
from pprint import pprint
from test_api.api.usermanagement import UserManagement, usermanagement


@pytest.fixture()
def login_code():
    # 登录返回值
    usermanagement.login_admin()

    return usermanagement.response_json['code']


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
    usermanagement.user_add(Data={"RegisterOption":{"duration":0,"endDate":"2099-12-31","gender":0,"isTrial":False,"nickname":"zhaos016464","nicknameNote":"zhaos016464","password":"016464","registerType":"mobile","remark":"坐等","repassword":"016464","role":"groupMember","smsCode":"","timeType":"end","username":"17820016464"}})
    data = ('17820016464', '016464')
    return usermanagement.response_json, data





# @pytest.fixture()
# def login_newuser(user_add):
#     usermanagement.login_admin(user_add[1][], "016464")
#     return usermanagement.response_json









# usermanagement.Obtaining_Institutional_Configuration_Information()
# # response = usermanagement.user_add(Data=)
# print(usermanagement.url)
# pprint(dict(usermanagement.header_print))
# print(' ')
# # print(type(usermanagement.user_add()))
#
#
#
# if usermanagement.response_type == 1:
#     print(usermanagement.response_text)
# else:
#     pprint(usermanagement.response_json)