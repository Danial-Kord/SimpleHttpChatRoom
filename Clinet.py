import http.client
import threading
import time
import os

name = input("enter your name : ")
index = 0
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request("GET", "<" + str(index) +">")
r1 = conn.getresponse()
print(r1.status, r1.reason)





def sendMessage():

    while True:
        try:
            msg = input("enter message : ")
            if str(msg) is 'END':
                return
            conn = http.client.HTTPConnection("127.0.0.1:8000")
            print("here")
            msg = str("_" + name + "_" + "<" + msg + ">")
            msg = msg.replace(" ","-")
            msg = msg.encode('utf-8')
            print(msg)
            conn.request("POST",str(msg))
        except:
            print("oops")
            conn = http.client.HTTPConnection("127.0.0.1:8000")


def recieveMessage():
    try:
        while True:
            time.sleep(10)
            conn = http.client.HTTPConnection("127.0.0.1:8000")
            conn.request("GET", "<" + str(index) + ">")
            data = conn.getresponse().reason
            data = data.replace("_"," ")
            data = data.replace(",","\n")
            print(data)
    except:
        print("fuk")

t1 = threading.Thread(target=sendMessage, name='t1')
t2 = threading.Thread(target=recieveMessage, name='t2')

# starting threads
t1.start()
t2.start()

