from http.server import HTTPServer, BaseHTTPRequestHandler

class ChunkedRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length'))
        data = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Received data: ' + data)

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, ChunkedRequestHandler)
    httpd.serve_forever()
