from test_api.api import CourseLibrary
from test_api.api.hour import Hours



class LingShi(object):

    def __init__(self, *args, **kwargs):
        self.hour = Hours(*args, **kwargs)
        self.coures = CourseLibrary.CourseLibrary(*args, **kwargs)

