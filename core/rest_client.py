import requests
import json

from env_choice.env import Env


class RestClient(object):
    """
    该类是对request.session库的一个扩展类
    是这个框架的核心类
    """

    def __init__(self):
        self.response_type = 0  # 若为1时 response的返回值的类型是str 及可以取出
        self.header_print = None  # 请求头
        self.url = None  # url
        self.data_print = None  # 参数
        self.response_text = None
        self.response_json = None  # 可以直接调用 返回值为json格式的时候
        self.env_dict = Env('us')
        self.session = requests.session()
        self.header = self.env_dict.env_dicts['header']
        self.api_root_url = self.env_dict.env_dicts['api_root_url']
        self.data = None  # 用来存储请求的参数
        self.news = ''

    def get(self, url, **kwargs):
        url = self.api_root_url + url
        self.url = url
        response = self.session.get(url, **kwargs)
        self.header_print = response.headers
        self.header_print = self.header_prints()
        try:
            self.response_type = 0
            self.response_json = json.dumps(response.json(), indent=4, ensure_ascii=False)
        except Exception as e:
            self.response_type = 1
            self.response_json = response.text
        return response

    def post(self, url, data=None, json=None, **kwargs):
        url = self.api_root_url + url
        self.url = str(url)
        if data:
            self.data = data
            self.data_print = json.dumps(data, indent=4, ensure_ascii=False)
        elif json:
            self.data = json
            self.data_print = json.dumps(data, indent=4, ensure_ascii=False)

        else:
            pass
        response = self.session.post(url, data, json, **kwargs)
        self.response_json = self.response_json = json.dumps(response.json(), indent=4, ensure_ascii=False)
        self.header_print = response.headers
        self.header_print = self.header_prints()
        try:
            self.response_type = 0
            self.response_json = response.json()
        except Exception as e:
            self.response_type = 1
            self.response_text = response.text
        return response

    def options(self, url, **kwargs):
        url = self.api_root_url + url
        self.url = str(url)
        return self.session.options(url, **kwargs)

    def head(self, url, **kwargs):
        url = self.api_root_url + url
        self.url = str(url)
        return self.session.head(url, **kwargs)

    def put(self, url, json=None, data=None, **kwargs):
        url = self.api_root_url + url
        self.url = str(url)
        if json:
            self.data = json
            self.data_print = "请求参数" + str(json)

        else:
            self.data = data
            self.data_print = json.dumps(data, indent=4, ensure_ascii=False)
        response = self.session.put(url, json=json, **kwargs)
        self.response_json = json.dumps(response.json(), indent=4, ensure_ascii=False)
        self.header_print = response.headers
        self.header_print = self.header_prints()
        try:
            self.response_type = 0
            self.response_json = response.json()
        except Exception as e:
            self.response_type = 1
            self.response_text = response.text
        return response

    def patch(self, url, data=None, **kwargs):
        url = self.api_root_url + url
        self.url = str(url)
        if data:
            self.data = data
            self.data_print = json.dumps(data, indent=4, ensure_ascii=False)
        response = self.session.patch(url, data, **kwargs)
        self.response_json = json.dumps(response.json(), indent=4, ensure_ascii=False)
        return response

    def delete(self, url, **kwargs):
        url = self.api_root_url + url
        self.url = str(url)
        response = self.session.delete(url, **kwargs)
        self.response_json = json.dumps(response.json(), indent=4, ensure_ascii=False)

        self.header_print = response.headers
        self.header_print = self.header_prints()
        try:
            self.response_type = 0
            self.response_json = response.json()
        except Exception as e:
            self.response_type = 1
            self.response_text = response.text

    def header_prints(self):
        self.header_printss = ''
        for key, value in dict(self.header_print).items():
            self.header_printss += key + ":" + value + '<br>'
        return self.header_printss

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


if __name__ == '__main__':
    dict1 = {'start': '杭州', 'end': '北京', 'ishigh': 0}
    print(json.dumps(dict1, indent=4, ensure_ascii=False))
