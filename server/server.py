#!/usr/bin/python3
import cgi
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import urlparse, parse_qs
from urls.utils import resolved_url

HOST_NAME = "localhost"
HOST_PORT = 8001


class Server(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        if self.headers.getheader('Location'):
            self.path = self.headers.getheader('Location')
        view = resolved_url(self.path)
        url_parse = urlparse(self.path)
        GET = parse_qs(url_parse.query)
        render = 'page not found'
        status_code = 404
        if view:
            render, status_code = view(self, GET=GET).get()
        self.send_response(status_code)
        self.wfile.write(render)

    def do_POST(self):
        self._set_headers()
        if self.headers.getheader('Location'):
            self.path = self.headers.getheader('Location')
        view = resolved_url(self.path)
        url_parse = urlparse(self.path)
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        if ctype == 'multipart/form-data':
            postvars = cgi.parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers.getheader('content-length'))
            postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
        else:
            postvars = {}
        GET = parse_qs(url_parse.query)
        POST = postvars

        render = 'page not found'
        status_code = 404
        if view:
            render, status_code = view(self, GET=GET, POST=POST).post()
        self.send_response(status_code)
        self.wfile.write(render)


def run_server():
    my_server = HTTPServer((HOST_NAME, HOST_PORT), Server)

    print("Server running")

    try:
        my_server.serve_forever()
    except KeyboardInterrupt:
        pass

    my_server.server_close()


run_server()
