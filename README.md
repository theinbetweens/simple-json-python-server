simple-json-python-server
=========================

A very basic python webserver that returns a reversed message string. The initial code was taken from this http://b.leppoc.net/2010/02/12/simple-webserver-in-python/ but modified to handle JSON.

Server
======

Start the server with the following:
```
python server.py 51714
```

The call it with the following POST request
```
wget -O- --post-data='{"message": "A red Ball"}' --header=Content-Type:application/json "http://127.0.0.1:51714"
```

Reason
======

I am working on a ruby on rails product that includes some natural language processing. Python has much better libraries so wanted a way for them both to talk to each other. Below is some Ruby code to call the server.

```ruby
require 'net/http'
require 'uri'
require 'json'

uri = URI.parse('http://localhost:51714')

header = {'Content-Type' => 'application/json'}
data = { 'message' => 'A blue ball' }

# Create the HTTP objects
http = Net::HTTP.new(uri.host, uri.port)
request = Net::HTTP::Post.new(uri.request_uri, header)
request.body = data.to_json

# Send the request
response = http.request(request)
puts response.body
```