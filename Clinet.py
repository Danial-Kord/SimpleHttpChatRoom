import http.client


name = input("enter your name : ")
index = 0
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request("GET", "<" + str(index) +">")
r1 = conn.getresponse()
print(r1.status, r1.reason)



def sendMessage():

    while True:
        try:
            str = input("enter message : ")
            conn = http.client.HTTPConnection("127.0.0.1:8000")
            str = ("_" + name + "_" + "<" + str + ">")
            str = str.encode()
            conn.request("POST",str)
        except:
            print("oops")
            conn = http.client.HTTPConnection("127.0.0.1:8000")


def recieveMessage():
    try:
        while True:
            str = input("enter message : ")
            conn.request("POST", "_" + name + "_" + "<" + str + ">")

    except:
        print("fuk")
sendMessage()