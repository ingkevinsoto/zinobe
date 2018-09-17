from render.utils import render_to_string


class View(object):

    template = None

    def __init__(self, request, GET=None, POST=None):
        self.GET = GET
        self.POST = POST
        self.request = request

    def get(self):
        return Response('GOEM', status=401)

    def post(self):
        return Response('GOEM', status=401)

    def render(self, context):
        return render_to_string(self.template, context)


class Response(object):
    def __init__(self, response, status=200, headers={}, data=None):
        self.response = response
        self.status = status or 200
        self.headers = headers or {}
        self.data = data
