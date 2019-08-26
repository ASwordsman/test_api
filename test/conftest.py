import pytest
import json
from pprint import pprint

from test_api.api.logins import Logins


class WE(Logins):

    def test_login(self):
        """
        :return: 返回状态码 token
        """
        response = self.login_admin()
        # print(self.header_print)
        # print(self.url)
        # print(self.data_print)
        return response.json()['code'], response.json()['token']


test = WE()
test.test_login()
@pytest.fixture()
def login_code():
    # 登录返回值
    code, token = test.test_login()
    return code, token


print(test.url)
pprint(dict(test.header_print))
pprint(json.loads(test.response_text))

