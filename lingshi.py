from api.repositories.hour import Hours

class LingShi(object):
    def __init__(self, api_root_url, **kwargs):
        self.api_root_url = api_root_url
        self.hour = Hours(self.api_root_url, **kwargs)
