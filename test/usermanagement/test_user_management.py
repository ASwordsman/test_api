import time


import allure
import pytest
from api.usermanagement import usermanagement
import warnings
from Logs.logs import logging

warnings.simplefilter("ignore", ResourceWarning)


@allure.description(
    str(usermanagement.url) + '\n\n' + str(usermanagement.header_print) + '\n\n' + str(usermanagement.response_text))
class Test_Usermanagement():
    def test_test_login(self, login_code):
        assert login_code == '0'

    def test_Institutional_information_get(self):
        # 获取机构信息
        usermanagement.Institutional_information_get()
        groupid = usermanagement.response_json['institution']['groupId']
        usermanagement.groupid = groupid  # 将groupid添加到属性里
        logging.error(usermanagement.url + str(usermanagement.header_print) + str(usermanagement.response_json))
        assert usermanagement.response_json['code'] == '0'

    def test_Obtaining_Institutional_Configuration_Information(self):
        # 获取机构配置信息
        usermanagement.Obtaining_Institutional_Configuration_Information()
        logging.debug(usermanagement.response_json)
        assert usermanagement.response_json['code'] == '0'

    def test_get_the_user_list_1(self):
        # 获取用户列表
        usermanagement.get_the_user_list(usermanagement.groupid)
        usermanagement.user_total = int(usermanagement.response_json['total'])  # 用户总数
        logging.error(usermanagement.response_json)
        assert usermanagement.response_json['code'] == '0'

    def test_user_add(self, user_add):
        # 添加新用户
        usermanagement.new_add_username = user_add['username']
        usermanagement.new_add_password = user_add['password']
        usermanagement.new_add_userid = user_add['userid']
        assert usermanagement.response_json['code'] == '0'

    def test_get_the_user_list_2(self):
        # 获取用户列表
        usermanagement.get_the_user_list(usermanagement.groupid)
        assert usermanagement.user_total + 1 == int(usermanagement.response_json['total']), '添加新用户之后获取用户列表'

    def test_usernew_login(self):
        # 新用户登录
        time.sleep(0.5)
        usermanagement.login_student(usermanagement.new_add_username,
                                     usermanagement.new_add_password)

        logging.error(usermanagement.response_json)
        assert usermanagement.response_json['code'] == '0'

    def test_modify_user_name(self):
        # 修改用户昵称
        usermanagement.login_admin()
        usermanagement.modify_user_name(newuserid=usermanagement.new_user_data['userid'])

        logging.error(usermanagement.response_json)
        assert usermanagement.response_json['code'] == '0'

    def test_get_the_user_list_3(self):
        # 获取用户列表
        usermanagement.get_the_user_list(usermanagement.groupid)

        assert int(usermanagement.response_json['total']) + 1 == int(usermanagement.user_total)

    def test_modify_user_validity_period(self):
        # 修改用户的有效期
        usermanagement.modify_user_validity_period([''.format(usermanagement.groupid)])

        assert usermanagement.response_json['code'] == '0'

    def test_search_user(self):
        # 搜索用户
        usermanagement.search_user(usermanagement.groupid)

        assert usermanagement.response_json['code'] == '0'

    def test_reset_password(self):
        # 重置密码
        userid = usermanagement.new_user_data['userid']
        logging.error(userid)
        usermanagement.reset_password(newuserid=userid), '重置密码'
        logging.error(usermanagement.data)
        assert usermanagement.response_json['code'] == '0'

    def test_reset_password_login(self):
        # 重置密码后使用新密码登录
        usermanagement.login_student(usermanagement.new_user_data['username'],
                                     '888888')

        assert usermanagement.response_json['code'] == '0'

    def test_password_login(self):
        # 重置密码后使用旧密码登录
        try:
            usermanagement.login_student(usermanagement.new_add_username, usermanagement.new_add_password)
        except Exception as e:
            pass
        logging.error(usermanagement.response_json)
        assert usermanagement.response_json['code'] == '-1000'

    def test_newuser_delete(self):
        # 删除用户
        usermanagement.login_admin()
        usermanagement.user_delete(usermanagement.groupid, usermanagement.new_add_userid)
        logging.error(usermanagement.url)
        logging.error(usermanagement.response_json)
        assert usermanagement.response_json['code'] == '0'

    def test_get_the_user_list_4(self):
        usermanagement.get_the_user_list(usermanagement.groupid)
        assert usermanagement.user_total == int(usermanagement.response_json['total']), "删除用户之后获取用户，列表"


if __name__ == '__main__':
    pytest.main()

# usermanagement.Institutional_information_get()
#
# pprint(usermanagement.response_json)
