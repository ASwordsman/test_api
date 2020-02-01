from test_api.Data.execl_data import ExeclData
from test_api.core.rest_client import RestClient





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
    print(train.url)

