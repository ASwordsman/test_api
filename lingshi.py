from test_api.api import CourseLibrary
from test_api.api.hour import Hours
from test_api.api.usermanagement import Logins


class LingShi(object):

    def __init__(self, *args, **kwargs):
        self.hour = Hours(*args, **kwargs)
        self.coures = CourseLibrary.CourseLibrary(*args, **kwargs)
        self.logins = Logins(*args, **kwargs)
