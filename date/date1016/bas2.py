#-*-coding:utf-8-*-
import BaseHTTPServer
import os
class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    Page= '''\
<html>
<body>
<p>Hello, Lin!</p>
</body>
</html>
'''
    def do_GET(self):
        try:
            full_path=os.getcwd()+self.path
            #not
            if not os.path.exists(full_path):
                raise ServerException('{0} not found').format(self.path)
            #yes
            elif os.path.exists(full_path):
                self.handle_file(full_path)
            else:
                #ServerException don't work and we design it purposely
                raise ServerException("Unknown object '{0}'".format(self.path))

        except Exception as msg:
            self.handle_error(msg)
    def handle_file(self,full_path):
        try:
            with open(full_path,'rb') as f:
                content=f.read()
            self.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(self.path, msg)
            self.handle_error(msg)

    Error_Page = """\
            <html>
            <body>
            <h1>Error accessing {path}</h1>
            <p>{msg}</p>
            </body>
            </html>
            """
    def handle_error(self,msg):
        content=self.Error_Page.format(path=self.path,msg=msg)
        self.send_content(content,404)#add the paras status=200 to deal with the error situation
    def send_content(self,content,status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(content)))
        self.end_headers()
        self.wfile.write(content)
if __name__=='__main__':
    serverAddress=('',8080)
    server=BaseHTTPServer.HTTPServer(serverAddress,RequestHandler)
    server.serve_forever()