import pytest

from test_api.api.usermanagement import usermanagement


@pytest.fixture()
def login_code():
    # 登录返回值
    usermanagement.login_admin()

    return usermanagement.response_json['code']



