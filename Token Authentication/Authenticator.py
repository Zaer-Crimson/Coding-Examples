from http.server import BaseHTTPRequestHandler, HTTPServer
import sys, uuid
from urllib import parse

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    
    tokens = {}
    logins = {"myUser":"myPassword"}
    
    # Set the HTTP status code and response headers
    def set_headers(self, responseCode):
        self.send_response(responseCode)
        self.send_header("Content-type", "text/html")
        self.send_header('Access-Control-Allow-Origin', "*")
        self.send_header('Access-Control-Allow-Headers', "*")
        self.end_headers()
    
    def do_GET(self):
        # TO-DO: Handle GET Requests
        if self.getPage()[1:] in self.tokens.keys():
            self.set_headers(200)
            self.wfile.write(bytes(self.tokens[self.getPage()[1:]], "utf-8"))
        elif self.getPage() == '/logout':
            clientIP = self.client_address[0]
            for key, value in dict(self.tokens).items():
                if value == clientIP:
                    del self.tokens[key]
                    self.set_headers(200)
                    self.wfile.write(bytes("User logged out successfully!", "utf-8"))
        else:
            self.set_headers(404)
            self.wfile.write(bytes("Error 404: Page not found", "utf-8"))
        
    def do_POST(self):
        # TO-DO: Handle POST Requests
        if self.getPage() == '/login':
            requestData = self.getRequestData()
            if requestData['username'] in self.logins.keys():
                if self.logins[requestData['username']] == requestData['password']:
                    clientIP = self.client_address[0]
                    if clientIP not in self.tokens.values():
                        token = str(uuid.uuid4())
                        self.tokens[token] = clientIP
                        self.set_headers(200)
                        self.wfile.write(bytes("login successful, your token:" + token, "utf-8"))
                    else:
                        self.set_headers(409)
                        self.wfile.write(bytes("Login failed: Token already exists", "utf-8"))
                else:
                    self.set_headers(401)
                    self.wfile.write(bytes("Login failed: Username or password was incorrect.", "utf-8"))
            else:
                self.set_headers(401)
                self.wfile.write(bytes("Login failed: Username or password was incorrect.", "utf-8"))
                    
        
    # Fetches the requested path
    def getPage(self):
        return parse.urlsplit(self.path).path
    
    # Fetches the request body data (i.e. POST request parameters)
    def getRequestData(self):
        body = self.rfile.read(int(self.headers.get('Content-Length')))
        body = body.decode("utf-8")
        return dict(parse.parse_qsl(body))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except:
        webServer.server_close()
        print("Server stopped.")
        sys.exit()
    webServer.server_close()
    print("Server stopped.")
    sys.exit()