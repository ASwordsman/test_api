# coding:utf-8

import pytest

from test_api.Data.execl_data import ExeclData
from test_api.api.train_get import Train
import jsonpath

data = ExeclData('test')
# data_dict, path_dict, assert_dict = data.data_return()[0]
train = Train()


# print(data.data_return())

@pytest.mark.parametrize(('data_dict', 'path_dict', 'assert_dict'), data.list_data, ids=data.list_desc)
class Test_Train():
    def test_test_login(self, data_dict, path_dict, assert_dict):
        response = train.train_get(path_dict)
        assert response.status_code == assert_dict['status_code'], 'HTTP状态码'
        for i in path_dict.keys():
            if '$' in i:
                res = jsonpath.jsonpath(response.json(), i)
                assert res == assert_dict['i']


if __name__ == '__main__':
    pytest.main('v')
