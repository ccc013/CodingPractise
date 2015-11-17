# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 18:46:17 2015

@author: cai
"""

import SimpleHTTPServer
import SocketServer

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()