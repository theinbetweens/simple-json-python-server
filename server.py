# Initial References
# http://b.leppoc.net/2010/02/12/simple-webserver-in-python/
# http://stackoverflow.com/questions/9733638/post-json-using-python-request

import cgi
import Cookie
import sys
import json

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
  
class MainHandler(BaseHTTPRequestHandler):

  def do_POST(s):
    content_len = int(s.headers.getheader('content-length'))
    post_body = s.rfile.read(content_len)

    decoded = json.loads(post_body)  
    reversed_message = decoded['message'][::-1]

    new_message = {'message': reversed_message}
    json_obj = json.dumps(new_message)
    json_size = len(json_obj)
          
    s.send_response(200)
    s.send_header("Status", 200)
    s.send_header("Content-type", "application/json; charset=utf-8")
    s.end_headers()
    s.wfile.write(json_obj)  

def main(port):
  try:
    server = HTTPServer(('', int(port)), MainHandler)
    print 'started httpserver...'
    server.serve_forever()
  except KeyboardInterrupt:
    print '^C received, shutting down server'
    server.socket.close()
 
if __name__ == '__main__':
  main(sys.argv[1])
