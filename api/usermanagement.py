from test_api.core.rest_client import RestClient


class UserManagement(RestClient):

    def login_student(self, username, password):
        self.session.headers.update(self.header)
        # 登录
        response = self.put("/center/services/rest/user/Login/{}/{}".format(username, password))
        self.session.headers['token'] = response.json()['token']
        self.header_print = self.session.headers
        response.encoding = 'utf-8'

        return response

    def login_admin(self):
        self.session.headers.update(self.header)
        response = self.put("/center/services/rest/user/Login/{}/{}".format(self.env_dict.env_dicts["admin"],
                                                                                      self.env_dict.env_dicts["password"]))
        self.session.headers['token'] = response.json()['token']
        self.header_print = self.session.headers
        response.encoding = 'utf-8'

        return response

    def Obtaining_Institutional_Configuration_Information(self):
        #获取机构配置信息

        response = self.get('/user/services/rest/user/Startup')
        return response



    def Institutional_information_get(self):
        #获取机构信息

        response = self.get('/user/services/rest/user/Startup')
        return response

    def user_add(self, Data):
        #添加用户

        response = self.post('/user/services/rest/user/', json=Data)

        return response

    def username_get(self, groupid):
        #获取用户列表

        response = self.get('/social/services/rest/group/GetUsers/{}/all'.format(groupid))

        return response


    def revise_remarks(self, Data):
        #修改用户备注
        response = self.put('/user/services/rest/user/Nickname', json=Data)

        return response


    def modify_user_validity_period(self, Data):
        # 修改用户有效期
        response = self.post('/user/services/rest/transaction/UserTime', data=Data)

        return response

    def search_user(self, groupid):
        #搜索用户

        response = self.get('/social/services/rest/group/GetUsers/{}/all?search=student'.format(groupid))

        return response

    def reset_password(self, Data):
        #重置密码

        response = self.put('/user/services/rest/user/ResetPassword', json=Data)

        return response

    def user_delete(self, groupid, userid):
        #删除用户

        response = self.delete('/social/services/rest/group/User/{}/{}'.format(groupid, userid))

        return response


usermanagement = UserManagement()
print(usermanagement.login_admin())
