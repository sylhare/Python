import BaseHTTPServer
import SimpleHTTPServer
# import http.server for python 3 to replace from the above
import ssl

# generate server.xml with the following command:
#    openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
#
# Or from python
# from subprocess import call
# call(["openssl", "req", "-new", "-x509", "-keyout", "server.pem", "-out", "server.pem", "-days", "365", "-nodes"])
#
# run as follows:
#    python simple-https-server.py
#
# then in your browser, visit:
#    https://localhost:4443

httpd = BaseHTTPServer.HTTPServer(('localhost', 4443), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile='./server.pem', server_side=True)
httpd.serve_forever()

if __name__ == '__main__':
    """ local SSL-enabled HTTPS server """
