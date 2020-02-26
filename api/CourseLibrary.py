from core.rest_client import RestClient


class CourseLibrary(RestClient):

    def coursewaregroup_get(self):

        # 获取学校教程库的课件集
        response = self.get('/social/services/rest/coursewareGroup/Inst/Coursewares?startPos=0&endPos'
                            '=19&categoryType=music_inst_all&search= ')
        return response

    def coursemusice_get(self):

        # 获取学校音乐库
        response = self.get('/social/services/rest/coursewareGroup/Inst/Coursewares?startPos=0&endPos=19'
                            '&categoryType=music_inst_all&search= ')
        return response

    def works_create(self, data, json):

        # 创建作品
        response = self.post('/social/services/rest/agc', data=data)
        response.json()
        self.put('/social/services/rest/agc/Pages', json=json)

    def works_delete(self, contenid):
        # contentid  作品的id
        # 删除作品

        response = self.delete('/social/services/rest/agc/Content/Agc/{}?serino=143').format(contenid)

        return response

