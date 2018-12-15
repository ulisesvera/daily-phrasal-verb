#!/usr/bin/env python
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import json 
import random

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'javascript/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        
        self.wfile.write(getRandomVerb())

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()



def getRandomVerb():
    try:
        # We get the json file content (phrasal verbs)
        with open('phrasal_verbs.json') as dataFile:
            phrasalVerbs = json.load(dataFile)

        # We get a random position to get the daily phrasal verb
        #for x in range(len(phrasalVerbs)):
        #    randomPosition = random.randint(0,len(phrasalVerbs))
        randomPosition = random.randint(0,len(phrasalVerbs))

        # Now, we have the choosen item
        #print("Content-Type: javascript/json")
        print(phrasalVerbs[randomPosition])
        #web.header('Content-Type', 'application/json')
        return json.dumps(phrasalVerbs[randomPosition])
    except ValueError:
        print("Ups, there is an error: ",ValueError)

#getRandomVerb()