import yaml
import pprint

from test_api import settings


class Env(object):

    def __init__(self, env_name):
        self.env_name = env_name
        self.abspath = settings.parent_path + '\\yaml_dict'

        self.env_dicts = self.choose_env()

    def choose_env(self):
        dirpath = ''
        if self.env_name == 'ys':
            dirpath = self.abspath + '\\ys.yaml'
        elif self.env_name == 'vs':
            dirpath = self.abspath + '\\vs.yaml'

        elif self.env_name == ' fs':
            dirpath = self.abspath + '\\vs.yaml'
        elif self.env_name == 'ws':
            dirpath = self.abspath + '\\ws.yaml'

        elif self.env_name == 'us':
            dirpath = self.abspath + '\\us.yaml'
        else:
            pass
        with open(dirpath, 'r+') as f:
            # 切换环境
            env_dict = yaml.safe_load(f)
            return env_dict

