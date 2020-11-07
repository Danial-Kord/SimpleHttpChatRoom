import http.server
import socketserver
import re

messeges=[]

class KodeFunHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    # handle GET command
    def do_GET(self):
        try:
            # send code 200 response
            self.send_response(200,"Hi")
            self.send_header('Content-type', 'tex')
            self.end_headers()
            print("connection start")
            return

        except IOError:
            self.send_error(404, 'file not found')


    def do_POST(self):
        try:
            print("recieved " + self.requestline)
            # send code 200 response
            self.send_response(200,"Hi")
            # send header first
            self.send_header('Content-type', 'tex')
            self.end_headers()


            messeges.append(re.search("<(.+?)>",self.requestline).group(1))
            for messege  in messeges:
                print(messege)
            print("wtf")
            return

        except IOError:
            self.send_error(404, 'file not found')



def run():
    print('http server is starting...')
    Handler = KodeFunHTTPRequestHandler
    with socketserver.TCPServer(("127.0.0.1", 8000), Handler) as httpd:
        print("serving at port", 8000)
        httpd.serve_forever()



if __name__ == '__main__':
    run()