

class View(object):

    def __init__(self, request, GET=None, POST=None):
        self.GET = GET
        self.POST = POST
        self.request = request

    def get(self):
        return 'GONE', 401

    def post(self):
        return 'GONE', 401
