from socket import *

serverName = '127.0.0.1'
serverPort = 12345

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
method = {
    'GET': 'GET / HTTP/1.1\r\nHost: 127.0.0.1:12345\r\nUser-Agent: insomnia/2022.2.1\r\nAccept: */*\r\n\r\n',
    'POST': 'POST / HTTP/1.1\r\nHost: 127.0.0.1:12345\r\nUser-Agent: insomnia/2022.2.1\r\nAccept: */*\r\nContent-Length: 0\r\n\r\n',
    'HEAD': 'HEAD / HTTP/1.1\r\nHost: 127.0.0.1:12345\r\nUser-Agent: insomnia/2022.2.1\r\nAccept: */*\r\n\r\n',
    'PUT': 'PUT / HTTP/1.1\r\nHost: 127.0.0.1:12345\r\nUser-Agent: insomnia/2022.2.1\r\nAccept: */*\r\nContent-Length: 0\r\n\r\n',
    'DELETE': 'DELETE / HTTP/1.1\r\nHost: 127.0.0.1:12345\r\nUser-Agent: insomnia/2022.2.1\r\nAccept: */*\r\n\r\n',
}
while True:
    msg = input('msg:')

    # end 명령어를 치면 소켓 통신 종료
    if msg == "end":
        break
    if msg in method.keys():
        request_message = method[msg]
    else:
        request_message = 'NotAllowed / HTTP/1.1\r\nHost: 127.0.0.1:12345\r\nUser-Agent: insomnia/2022.2.1\r\nAccept: */*\r\n\r\n'
    clientSocket.send(request_message.encode('utf-8'))
    recieve_message = clientSocket.recv(65535)
    print(recieve_message.decode())

clientSocket.close()
