import pandas as pd
import os

import settings


class ExeclData(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.df = pd.read_excel(os.path.join(os.path.join(settings.parent_path, 'execl'), ('{}.xlsx'.format(self.file_name))))
        self.list_desc = []
        self.list_data = self.data_return()


    def execl_body(self, loc):
        df = self.df
        num = 0
        list_body = list()
        list_path = list()
        list_assert = list()
        list_other = list()
        for i in df.loc[:, '变量位置']:

            if i == 'body':
                list_body.append(num)
            elif i == 'path':
                list_path.append(num)
            elif i == 'assert':
                list_assert.append(num)
            if i == 'other':
                list_other.append(num)
            num += 1
        dict_data = dict()
        dict_data1 = dict()
        dict_path = dict()
        dict_assert = dict()
        list_desc = list()
        for i in df.loc[list_body, ['变量', loc]].values:
            dict_data[i[0]] = i[1]
        for i in dict_data.keys():
            # print(i)
            p = i.split('.')
            dict_data1[p[1]] = dict_data[i]
        for i in df.loc[list_path, ['变量', loc]].values:
            dict_path[i[0]] = i[1]

        for i in df.loc[list_assert, ['变量', loc]].values:
            dict_assert[i[0]] = i[1]

        for i in df.loc[list_other, ['变量', loc]].values:
            # dict_other[i[0]] = i[1]
            list_desc.append(i[1])
        return dict_data1, dict_path, dict_assert, list_desc

    def data_return(self):
        list_data = []
        for i in self.df.columns[3:]:
            dict_data, dict_path, dict_assert, list_desc = self.execl_body(i)
            list_data.append((dict_data, dict_path, dict_assert))
            # print(list_desc[1])
            self.list_desc.append(list_desc[1])
        return list_data


if __name__ == '__main__':
    data = ExeclData('test')
    print(data.list_desc[1])
    print(data.list_data[1])
