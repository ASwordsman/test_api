# coding:utf-8
import os

import allure
import pytest

import jsonpath

from Data.execl_data import ExeclData
from api.train_get import Train
from common.allure_report import allure_report_get

data = ExeclData('test')
train = Train()


class TestTrain(object):
    @pytest.mark.parametrize(('data_dict', 'path_dict', 'assert_dict'), data.list_data, ids=data.list_desc)
    def test_train_get(self, data_dict, path_dict, assert_dict):
        response = train.train_get(path_dict)
        allure_report_get(train.header_print, train.url, train.response_json)
        assert response.status_code == assert_dict['status_code'], 'HTTP状态码'
        for i in path_dict.keys():
            if '$' in i:
                res = jsonpath.jsonpath(response.json(), i)
                assert res == assert_dict['i']

    @pytest.mark.parametrize(('data_dict', 'path_dict', 'assert_dict'), [data.list_data[1]], ids=[data.list_desc[1]])
    def test_train_get_tiaoshi(self, data_dict, path_dict, assert_dict):
        # 用于调试 通过下标取值对应execl的值数
        response = train.train_get(path_dict)
        assert response.status_code == assert_dict['status_code'], 'HTTP状态码'
        for i in path_dict.keys():
            if '$' in i:
                res = jsonpath.jsonpath(response.json(), i)
                assert res == assert_dict['i']


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report_xml'])
    os.system('allure serve ./report_xml')
