from test_api.core.rest_client import RestClient


class Logins(RestClient):

    def login_student(self):
        self.session.headers.update(self.header)
        # 登录
        response = self.put("/center/services/rest/user/Login/{}/{}".format(self.env_dict.env_dicts["student"],
                                                                                      self.env_dict.env_dicts["password"]))

        self.session.headers['token'] = response.json()['token']
        self.header_print = self.session.headers
        response.encoding = 'utf-8'
        self.response_text = response.text

        return response.json()

    def login_admin(self):
        self.session.headers.update(self.header)
        response = self.put("/center/services/rest/user/Login/{}/{}".format(self.env_dict.env_dicts["admin"],
                                                                                      self.env_dict.env_dicts["password"]))
        self.session.headers['token'] = response.json()['token']
        self.header_print = self.session.headers
        response.encoding = 'utf-8'
        self.response_text = response.text

        return response


logins = Logins()