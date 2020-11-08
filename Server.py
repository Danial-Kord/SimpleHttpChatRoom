import http.server
import socketserver
import re

messeges=[]

class KodeFunHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    # handle GET command
    def do_GET(self):
        try:
            index = int(re.search("<(.+?)>",self.requestline).group(1))

            str = "messegaes"
            for i in range(index,messeges.__len__()):
                str += ","
                str += messeges.__getitem__(i)
            str.replace(" ","_")
            # send code 200 response
            self.send_response(200,str)
            self.send_header('Content-type', 'tex')
            self.end_headers()
            return

        except IOError:
            self.send_error(404, 'file not found')


    def do_POST(self):
        try:
            print("recieved " + self.requestline)

            data = self.requestline


            data = re.search("POST (.+?) HTTP", data).group(1)
            data = bytes(data, 'utf-8')
            data = data.decode('utf-8')
            print(str(data))
            data = data.replace('-',' ')

            # send code 200 response
            self.send_response(200,"Hi")
            # send header first
            self.send_header('Content-type', 'tex')
            self.end_headers()

            name = re.search("_(.+?)_", data).group(1)
            data = name +" : " + re.search("<(.+?)>",data).group(1)
            messeges.append(data)
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