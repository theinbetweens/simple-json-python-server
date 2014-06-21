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
