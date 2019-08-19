import requests
import json as json_parser


class RestClient():
    def __init__(self, api_root_url, header, env_dict,**kwargs):
        self.env_dict = env_dict
        self.session = requests.session()
        self.header = header
        self.api_root_url = api_root_url

    def get(self, url, **kwargs):
        url = self.api_root_url + url
        return self.session.get(url, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        url = self.api_root_url + url
        return self.session.post(url, data, json, **kwargs)

    def options(self, url, **kwargs):
        url = self.api_root_url + url
        return self.session.options(url, **kwargs)

    def head(self, url, **kwargs):
        url = self.api_root_url + url
        return self.session.head(url, **kwargs)

    def put(self, url, json=None, **kwargs):
        url = self.api_root_url + url
        return self.session.put(url, json=json, **kwargs)

    def patch(self, url, data=None, **kwargs):
        url = self.api_root_url + url
        return self.session.patch(url, data, **kwargs)

    def delete(self, url, **kwargs):
        url = self.api_root_url + url
        return self.session.delete(url,  **kwargs)

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