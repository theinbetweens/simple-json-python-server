# http://b.leppoc.net/2010/02/12/simple-webserver-in-python/

# http://stackoverflow.com/questions/9733638/post-json-using-python-request

# wget -O- --post-data='{"some data to post..."}' --header=Content-Type:application/json "http://127.0.0.1:3003"
import cgi
import Cookie
import sys
import json

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
  
class MainHandler(BaseHTTPRequestHandler):

  def do_GET(s):
    data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}

    s.send_response(200)
    s.send_header("Content-type", "application/json; charset=utf-8")
    s.send_header("Status", 200)
    s.end_headers()    

    s.wfile.write(data)

  def do_POST(s):
    content_len = int(s.headers.getheader('content-length'))
    post_body = s.rfile.read(content_len)
    json_input = '{ "one": 1, "two": { "list": [ {"item":"A"},{"item":"B"} ] } }'

    data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}

    obj = {'content' : 'something goes here'}
    json_obj = json.dumps(obj)
    json_size = len(json_obj)

    decoded = json.loads(post_body)  
          
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
