import pytest

from test_api.api.logins import Logins


class WE(Logins):


    def test_login(self):
        response = self.login_admin()
        # print(self.header_print)
        # print(self.url)
        # print(self.data_print)
        return response.json()['code'], response.json()['token']



test = WE()
test.test_login()
print(test.header_print)
# test.test_login()
@pytest.fixture()
def login_code():
    # 登录返回值

    code, token = test.test_login()
    return code, token