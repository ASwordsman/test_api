import pytest
import allure

from test_api.test.conftest import test
@allure.description(test.url + '\n\n' + str(test.header_print) + '\n\n' + test.response_text)
def test_login(login_code):
    assert login_code[0] == '0'


def test_login1(login_code):
    assert login_code[1]
