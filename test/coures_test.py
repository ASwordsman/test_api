import pytest


def test_login(login_code):
    assert login_code[0] == '0'


def test_login1(login_code):
    assert login_code[1]
