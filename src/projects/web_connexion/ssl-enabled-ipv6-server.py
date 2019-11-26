# Source SSL part : https://gist.github.com/dergachev/7028596
# Source IPv6 part : https://gist.github.com/akorobov/7903307
# taken from http://www.piware.de/2011/01/creating-an-https-server-in-python/
# generate server.xml with the following command:
#    openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
# run as follows:
#    python simple-https-server.py
# then in your browser, visit:
#    https://localhost:62001
import socket
import ssl
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler


class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        print(self.headers)
        return


class HTTPServerV6(HTTPServer):
    address_family = socket.AF_INET6


def main():
    server = HTTPServerV6(('::', 62001), MyHandler)
    server.socket = ssl.wrap_socket(server.socket, certfile='./server.pem', server_side=True)
    server.serve_forever()


if __name__ == '__main__':
    main()
