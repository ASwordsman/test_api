import os

import yaml

import settings


class Env(object):

    def __init__(self, env_name):
        self.env_name = env_name
        self.abspath = os.path.join(settings.parent_path, 'yaml_dict')

        self.env_dicts = self.choose_env()

    def choose_env(self):
        dirpath = ''
        if self.env_name == 'ys':
            dirpath = os.path.join(self.abspath, 'ys.yaml')
        elif self.env_name == 'vs':
            dirpath = os.path.join(self.abspath, 'vs.yaml')

        elif self.env_name == ' fs':
            dirpath = os.path.join(self.abspath, 'vs.yaml')
        elif self.env_name == 'ws':
            dirpath = os.path.join(self.abspath, 'ws.yaml')

        elif self.env_name == 'us':
            dirpath = os.path.join(self.abspath, 'us.yaml')
        else:
            pass
        with open(dirpath, 'r+') as f:
            # 切换环境
            env_dict = yaml.safe_load(f)
            return env_dict

if __name__ == '__main__':
    print(settings.parent_path)