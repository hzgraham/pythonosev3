#!/user/bin/env python
import datetime
import yaml
import requests
import re

HELP='''
<html>
<head>
<title>
{appname} Help
</title>
<style>
body {{
  font-family: "Helvetica Neue",Helvetica,"Liberation Sans",Arial,sans-serif;
  font-size: 14px;
  line-height: 1.4;
}}

html {{
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}}

pre {{
  display: block
  font-family: Menlo,Monaco,"Liberation Mono",Consolas,monospace !important;
}}
</style>
</head>
<body>
<h1>
{appname} Help
</h1>
</body>
</html>

'''

def application(environ, start_response):
    response_body = HELP.format(
        giturl  = 'GITOLITE_SERVER:puppet-cfg/modules/soctools/data/',
        appuri  = wsgiref.util.application_uri(environ),
        appname = environ['OPENSHIFT_APP_NAME'])
    return [response_body.encode('utf-8')]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8051, application)
    httpd.serve_forever()
