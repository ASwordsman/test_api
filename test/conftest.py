import pytest

from test_api.api.logins import Logins


class Test(Logins):

    def test_login(self):
        response = self.login_admin()
        return response['code'], response['token']


test = Test()
# test.test_login()
@pytest.fixture()
def login_code():
    # 登录返回值

    code, token = test.test_login()
    return code, token
