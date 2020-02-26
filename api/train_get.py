from Data.execl_data import ExeclData
from core.rest_client import RestClient


class Train(RestClient):
    def train_get(self, path_dict):
        self.api_root_url = ''
        self.url = "https://api.jisuapi.com/train/station2s?start={start}&end={end}&ishight={ishigh}".format(
            **path_dict)
        response = self.get(self.url)
        response.encoding = 'utf-8'
        return response


if __name__ == '__main__':
    train = Train()
    train.train_get({'start': '杭州', 'end': '北京', 'ishigh': 0})
    print(train.header_print)
    for key, value in train.header_print.items():
        print(key + ":" + value)
