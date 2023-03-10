from http.server import BaseHTTPRequestHandler, HTTPServer
import sys, time
from urllib import parse
import urllib.request

hostName = "localhost"
serverPort = 80

class MyServer(BaseHTTPRequestHandler):
    
    tokens = {}
    
    # Set the HTTP status code and response headers
    def set_headers(self, responseCode):
        self.send_response(responseCode)
        self.send_header("Content-type", "text/html")
        self.send_header('Access-Control-Allow-Origin', "*")
        self.send_header('Access-Control-Allow-Headers', "*")
        self.end_headers()
    
    def do_GET(self):
        # TO-DO: Handle GET requests for our secure resource
        if self.getPage() == '/':
            parameters = self.getParams()
            if parameters.get('token'):
                clientIP = self.client_address[0]
                fetchedIP = self.getToken(parameters.get('token'))
                if clientIP == fetchedIP:
                    self.set_headers(200)
                    
                    # A special thing for you
                    self.wfile.write(bytes("<!doctype html><html><body bgcolor=\"#FFC6D1\">", "utf-8"))
                    
                    self.wfile.write(bytes("<font color = 'WHITE'>&#9608;&#9608;&#9608;&#9608;</font><font color='BLACK'>&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;</font><font color='WHITE'>&#9608;&#9608;&#9608;&#9608;</font></br>", "utf-8"))
                    self.wfile.write(bytes("<font color = 'WHITE'>&#9608;&#9608;&#9608;</font><font color='BLACK'>&#9608;&#9608;</font><font color='WHITE'>&#9608;&#9608;</font><font color='RED'>&#9608;&#9608;</font><font color='white'>&#9608;&#9608;</font><font color='BLACK'>&#9608;&#9608;</font><font color = 'WHITE'>&#9608;&#9608;&#9608;</font></br>", "utf-8"))
                    self.wfile.write(bytes("<font color = 'WHITE'>&#9608;&#9608;</font><font color='BLACK'>&#9608;&#9608;</font><font color='WHITE'>&#9608;&#9608;&#9608;</font><font color='RED'>&#9608;&#9608;</font><font color='white'>&#9608;&#9608;&#9608;</font><font color='BLACK'>&#9608;&#9608;</font><font color = 'WHITE'>&#9608;&#9608;</font></br>", "utf-8"))
                    self.wfile.write(bytes("<font color = 'WHITE'>&#9608;</font><font color='BLACK'>&#9608;&#9608;</font><font color='RED'>&#9608;</font><font color='WHITE'>&#9608;&#9608;</font><font color='RED'>&#9608;&#9608;&#9608;&#9608;</font><font color='WHITE'>&#9608;&#9608;</font><font color = 'RED'>&#9608;</font><font color='BLACK'>&#9608;&#9608;</font><font color='WHITE'>&#9608;<font></br>", "utf-8"))
                    
                    self.wfile.write(bytes("<font color = 'WHITE'>&#9608;</font><font color='BLACK'>&#9608;</font><font color='WHITE'>&#9608;</font><font color='RED'>&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;</font><font color='white'>&#9608;</font><font color='BLACK'>&#9608;</font><font color = 'WHITE'>&#9608;</font></br>", "utf-8"))
                    self.wfile.write(bytes("<font color = 'BLACK'>&#9608;&#9608;</font><font color='WHITE'>&#9608;&#9608;</font><font color='RED'>&#9608;&#9608;</font><font color='WHITE'>&#9608;&#9608;&#9608;&#9608;</font><font color='RED'>&#9608;&#9608;</font><font color='WHITE'>&#9608;&#9608;</font><font color = 'BLACK'>&#9608;&#9608;</font></br>", "utf-8"))
                    self.wfile.write(bytes("<font color = 'BLACK'>&#9608;</font><font color='WHITE'>&#9608;&#9608;&#9608;</font><font color='RED'>&#9608;</font><font color='WHITE'>&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;</font><font color='RED'>&#9608;</font><font color='WHITE'>&#9608;&#9608;&#9608;</font><font color = 'BLACK'>&#9608;</font></br>", "utf-8"))
                    self.wfile.write(bytes("<font color = 'BLACK'>&#9608;</font><font color='WHITE'>&#9608;&#9608;&#9608;</font><font color='RED'>&#9608;</font><font color='WHITE'>&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;</font><font color='RED'>&#9608;</font><font color='WHITE'>&#9608;&#9608;&#9608;</font><font color = 'BLACK'>&#9608;</font></br>", "utf-8"))
                    
                    self.wfile.write(bytes("<font color = 'BLACK'>&#9608;</font><font color='WHITE'>&#9608;&#9608;</font><font color='RED'>&#9608;&#9608;</font><font color='WHITE'>&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;</font><font color='RED'>&#9608;&#9608;</font><font color='WHITE'>&#9608;&#9608;</font><font color = 'BLACK'>&#9608;</font></br>", "utf-8"))
                    self.wfile.write(bytes("<font color = 'BLACK'>&#9608;</font><font color='RED'>&#9608;&#9608;&#9608;&#9608;&#9608;</font><font color='WHITE'>&#9608;&#9608;&#9608;&#9608;</font><font color='RED'>&#9608;&#9608;&#9608;&#9608;&#9608;</font><font color='BLACK'>&#9608;</font></br>", "utf-8"))
                    self.wfile.write(bytes("<font color = 'BLACK'>&#9608;</font><font color='RED'>&#9608;&#9608;</font><font color='BLACK'>&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;</font><font color='RED'>&#9608;&#9608;</font><font color='BLACK'>&#9608;</font></br>", "utf-8"))
                    self.wfile.write(bytes("<font color = 'BLACK'>&#9608;&#9608;&#9608;&#9608;</font><font color='WHITE'>&#9608;&#9608;</font><font color='BLACK'>&#9608;</font><font color='WHITE'>&#9608;&#9608;</font><font color='BLACK'>&#9608;</font><font color='WHITE'>&#9608;&#9608;</font><font color = 'BLACK'>&#9608;&#9608;&#9608;&#9608;</font></br>", "utf-8"))
                    
                    self.wfile.write(bytes("<font color = 'WHITE'>&#9608;</font><font color='BLACK'>&#9608;&#9608;</font><font color='WHITE'>&#9608;&#9608;&#9608;</font><font color='BLACK'>&#9608;</font><font color='white'>&#9608;&#9608;</font><font color='BLACK'>&#9608;</font><font color = 'WHITE'>&#9608;&#9608;&#9608;</font><font color='BLACK'>&#9608;&#9608;</font><font color='WHITE'>&#9608;</font></br>", "utf-8"))
                    self.wfile.write(bytes("<font color = 'WHITE'>&#9608;&#9608;</font><font color='BLACK'>&#9608;</font><font color='WHITE'>&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;</font><font color='BLACK'>&#9608;</font><font color = 'WHITE'>&#9608;&#9608;</font></br>", "utf-8"))
                    self.wfile.write(bytes("<font color = 'WHITE'>&#9608;&#9608;</font><font color='BLACK'>&#9608;&#9608;</font><font color='WHITE'>&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;</font><font color='BLACK'>&#9608;&#9608;</font><font color = 'WHITE'>&#9608;&#9608;</font></br>", "utf-8"))
                    self.wfile.write(bytes("<font color = 'WHITE'>&#9608;&#9608;&#9608;</font><font color='BLACK'>&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;</font><font color = 'WHITE'>&#9608;&#9608;&#9608;</font></br>", "utf-8"))
                elif clientIP != fetchedIP:
                    self.set_headers(401)
                    self.wfile.write(bytes("Error 401: Not Authorized", "utf-8"))
            else:
                self.set_headers(401)
                self.wfile.write(bytes("Error 401: Not Authourzed, no login token provided", "utf-8"))

    def getToken(self, token):
        # TO-DO: Fetches/caches a token for a set period of time, automatically re-fetches old tokens
        if token == "logout":
            return None
        if token not in self.tokens:
            try:
                fetchedIP = urllib.request.urlopen('http://127.0.0.1:8080/' + token).read()
                fetchedIP = fetchedIP.decode("utf-8")
                self.tokens[token] = [fetchedIP,time.time()]
                return fetchedIP
            except:
                return None
        else: 
            tokenVals = self.tokens[token]
            if (time.time() - tokenVals[1]) > 300:
                del self.tokens[token]
                return self.getToken(token)
            else:
                return tokenVals[0]
            
    # Gets the query parameters of a request and returns them as a dictionary
    def getParams(self):
        output = {}
        queryList = parse.parse_qs(parse.urlsplit(self.path).query)
        for key in queryList:
            if len(queryList[key]) == 1:
                output[key] = queryList[key][0]
        return output
    
    # Returns a string containing the page (path) that the request was for
    def getPage(self):
        return parse.urlsplit(self.path).path

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started at 127.0.0.1:80")

    try:
        webServer.serve_forever()
    except:
        webServer.server_close()
        print("Server stopped.")
        sys.exit()

    webServer.server_close()
    print("Server stopped.")
    sys.exit()