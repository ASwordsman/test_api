import requests

from test_api.env.env import Env


class RestClient(object):
    def __init__(self):
        self.header_print = None  # 请求头
        self.url = None  # url
        self.data_print = None  # 参数
        self.response_text = None
        self.env_dict = Env('ys')
        self.session = requests.session()
        self.header = self.env_dict.env_dicts['header']
        self.api_root_url = self.env_dict.env_dicts['api_root_url']

    def get(self, url, **kwargs):
        url = self.api_root_url + url
        self.url = url
        return self.session.get(url, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        url = self.api_root_url + url
        self.url = url

        if data:
            self.data_print = "请求参数" + data
        elif json:
            self.data_print = "请求参数" + json

        else:
            pass

        return self.session.post(url, data, json, **kwargs)

    def options(self, url, **kwargs):
        url = self.api_root_url + url
        self.url = url
        return self.session.options(url, **kwargs)

    def head(self, url, **kwargs):
        url = self.api_root_url + url
        self.url = url
        return self.session.head(url, **kwargs)

    def put(self, url, json=None, **kwargs):
        url = self.api_root_url + url
        self.url = url
        if json:
            self.data_print = "请求参数" + json

        self.url = url
        return self.session.put(url, json=json, **kwargs)

    def patch(self, url, data=None, **kwargs):
        url = self.api_root_url + url
        self.url = url
        if data:
            self.data_print = "请求参数" + data
        return self.session.patch(url, data, **kwargs)

    def delete(self, url, **kwargs):
        url = self.api_root_url + url
        self.url = url
        return self.session.delete(url, **kwargs)

    # def request(self, url, method_name, data=None, json=None, **kwargs):
    #     url = self.api_root_url + url
    #     if method_name == "get":
    #         return self.session.get(url, **kwargs)
    #     if method_name == "post":
    #         return self.session.post(url, data, json, **kwargs)
    #     if method_name == "options":
    #         return self.session.options(url, **kwargs)
    #     if method_name == "head":
    #         return self.session.head(url, **kwargs)
    #     if method_name == "put":
    #         return self.session.put(url, data, **kwargs)
    #     if method_name == "patch":
    #         if json:
    #             data = json_parser.dumps(json)
    #         return self.session.patch(url, data, **kwargs)
    #     if method_name == "delete":
    #         return self.session.delete(url, **kwargs)
