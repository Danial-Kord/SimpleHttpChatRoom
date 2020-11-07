import http.client
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request("POST", "<Whasup>")
r1 = conn.getresponse()
print(r1.status, r1.reason)


if r1.status is 200:
    while True:
        str = input("enter message")
        conn.send(str.encode())