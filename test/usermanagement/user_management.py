
import allure

from test_api.api.usermanagement import usermanagement


@allure.description('登录\n\n' +
    usermanagement.url + '\n\n' + str(usermanagement.header_print) + '\n\n' + usermanagement.response_text)
def test_login(login_code):
    assert login_code[0] == '0'


@allure.description('获取机构信息\n\n'+
    usermanagement.url + '\n\n' + str(usermanagement.header_print) + '\n\n' + usermanagement.response_text)
def Institutional_information_get(Institutional_information_get):
    # 获取机构信息
    assert Institutional_information_get[0] == '0'


@allure.description('获取机构信息\n\n'+
    usermanagement.url + '\n\n' + str(usermanagement.header_print) + '\n\n' + usermanagement.response_text)
def