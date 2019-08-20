import pytest

from test_api.lingshi import LingShi

class CouresTest(LingShi):

    def test_login(self):
        self.logins.login_admin()

