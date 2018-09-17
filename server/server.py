#!/usr/bin/python3
import cgi
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import urlparse, parse_qs
from Cookie import SimpleCookie

from urls.utils import resolved_url
from views.generic_views import Response

HOST_NAME = "localhost"
HOST_PORT = 8001


class Server(BaseHTTPRequestHandler):

    def _set_headers(self, headers):
        if not headers.get('Content-type'):
            self.send_header('Content-type', 'text/html')
        for key, value in headers.items():
            self.send_header(key, value)
        self.end_headers()

    def do_GET(self):
        # cookie = SimpleCookie(self.headers['cookie']) if self.headers.get('cookie') else SimpleCookie()
        view = resolved_url(self.path)
        url_parse = urlparse(self.path)
        GET = parse_qs(url_parse.query)
        response = Response('page not found', status=404)
        if view:
            response = view(self, GET=GET).get()
        if not view and '?' in self.path:
            view = resolved_url(url_parse.path)
            response = view(self, GET=GET).get()
            self.send_response(response.status)
            self._set_headers(response.headers)
            self.wfile.write(response.response)

        self.send_response(response.status)
        self._set_headers(response.headers)
        self.wfile.write(response.response)

    def do_POST(self):
        # cookie = SimpleCookie(self.headers['cookie']) if self.headers.get('cookie') else SimpleCookie()
        # cookie['username'] = 'hjkdahgsjahj'
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

        response = Response('page not found', status=404)
        if view:
            response = view(self, GET=GET, POST=POST).post()
        self.send_response(response.status)
        # self.send_header('Set-Cookie', cookie['username'].OutputString() + 'max-age=3600')
        self._set_headers(response.headers)
        self.wfile.write(response.response)


def run_server():
    my_server = HTTPServer((HOST_NAME, HOST_PORT), Server)

    print("Server running")

    try:
        my_server.serve_forever()
    except KeyboardInterrupt:
        pass

    my_server.server_close()


run_server()
