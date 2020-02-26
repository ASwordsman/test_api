import logging

import pytest
import json

from api.usermanagement import UserManagement, usermanagement
from faker import Faker
# @pytest.fixture()
# def login_code():
#     # 登录返回值
#     usermanagement.login_admin()
#
#     return usermanagement.response_json['code']

from faker import Faker

fake = Faker("zh_CN")


@pytest.fixture()
def Institutional_information_get():
    # 获取机构信息
    return usermanagement.Institutional_information_get()


@pytest.fixture()
def Obtaining_Institutional_Configuration_Information():
    # 获取机构配置信息
    return usermanagement.Obtaining_Institutional_Configuration_Information(), '获取机构配置信息'


@pytest.fixture()
def user_add():
    username = fake.phone_number()
    password = fake.bank_country()
    usermanagement.user_add(Data={
        "RegisterOption": {"duration": 0, "endDate": "2099-12-31", "gender": 0, "isTrial": False,
                           "nickname": "zhaos016464", "nicknameNote": "zhaos016464", "password": password,
                           "registerType": "mobile", "remark": "坐等", "repassword": password, "role": "groupMember",
                           "smsCode": "", "timeType": "end", "username": username}})
    logging.error(usermanagement.response_json)
    usermanagement.new_user_data = {"username": username, "password": password, "userid": usermanagement.response_json['user']['userId']}
    return usermanagement.new_user_data
