import allure
import pytest
from test_api.api.usermanagement import usermanagement
import warnings

warnings.simplefilter("ignore", ResourceWarning)


@allure.description(
    str(usermanagement.url) + '\n\n' + str(usermanagement.header_print) + '\n\n' + str(usermanagement.response_text))
class Test_Usermanagement():
    def test_test_login(self, login_code):
        assert login_code == '0'

    def test_Institutional_information_get(self, Institutional_information_get):
        # 获取机构信息
        usermanagement.Institutional_information_get()
        assert usermanagement.response_json['code'] == '0'

    def test_Obtaining_Institutional_Configuration_Information(self):
        # 获取机构配置信息
        usermanagement.Obtaining_Institutional_Configuration_Information()
        assert usermanagement.response_json['code'] == '0'

    def test_user_add(self, user_add):
        assert user_add[0]['code'] == '0'

    def test_usernew_login(self, user_add):
        usermanagement.login_student(usermanagement.data["RegisterOption"]["username"],
                                     usermanagement.data["RegisterOption"]["repassword"])
        assert usermanagement.response_json['code'] == '0'


def test_test_a():
    assert 1 == 1


if __name__ == '__main__':
    pytest.main()
