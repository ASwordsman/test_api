import requests
import json as json_parser
from api.role import *
headers = {
'AppType':'6',
'AppVersion':'2.1.10.107557',
'serverId':'1000',
'DeviceType': '0',
'uc':'TYTY',
'InstId':'170114',
'lan':'ch',
'Content-Type':'application/json',
'Accept-Encoding':'gzip',
'DeviceUniqueId':'ffffffff-b144-e045-ffff-ffffffc0aca9-com.lingshi.inst.klxt',
'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; OPPO R11s Build/OPM1.171019.011)',
'token':'13282:1620379720:24eda61a-ec6c-4c96-b6c2-3e6cb9d39a05:a382417eb49ec270748a6b616519b6b2:1000v'
}



class RestClient():
    def __init__(self, api_root_url, **kwargs):
        self.dict = {"username":admin, "password":password, "servername":"ys.51tyty.com", "api_root_url":"http://ys.51tyty.com"}
        self.session = requests.session()
        self.header = headers

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