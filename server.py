import socket
from datetime import datetime

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('127.0.0.1', 12345))
server_socket.listen(0)

print('The server is running')
print("Server IP : 127.0.0.1")
print("Server Port : 12345")
client_socket, addr = server_socket.accept()


while True:
    data = client_socket.recv(65535)

    request_data = data.decode().split()

    # client에서 end를 호출해 data가 넘어오지 않는 경우
    if not data:
        break

    # HTTP 프로토콜 method 및 version
    request_method = request_data[0]
    request_version = request_data[2]

    server_name = "Socket Server"

    # 해당 method와 HTTP version이 제대로 들어올 경우 처리
    if request_method == "GET" and request_version == "HTTP/1.1":
        print(request_method, request_version, "200")
        response_data = "{0} 200 OK\nServer: {1}\nDate: {2}\n".format(request_version, server_name,
                                                                      datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'))
    elif request_method == "POST" and request_version == "HTTP/1.1":
        print(request_method, request_version, "201")
        response_data = "{0} 201 OK\nServer: {1}\nDate: {2}\n".format(request_version, server_name,
                                                                      datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'))
    elif request_method == "HEAD" and request_version == "HTTP/1.1":
        print(request_method, request_version, "203")
        response_data = "{0} 203 OK\nServer: {1}\nDate: {2}\n".format(request_version, server_name,
                                                                      datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'))
    elif request_method == "PUT" and request_version == "HTTP/1.1":
        print(request_method, request_version, "202")
        response_data = "{0} 202 OK\nServer: {1}\nDate: {2}\n".format(request_version, server_name,
                                                                      datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'))
    elif request_method == "DELETE" and request_version == "HTTP/1.1":
        print(request_method, request_version, "204")
        response_data = "{0} 204 OK\nServer: {1}\nDate: {2}\n".format(request_version, server_name,
                                                                      datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'))

    # 위에서 정의한 5개 이외의 method 명령어를 실행 시 405 Method Not Allowed로 응답
    else:
        print(request_method, request_version, "405 Method Not Allowed")
        response_data = "{0} 405 Method Not Allowed\nServer: {1}\nDate: {2}\n".format(request_version, server_name,
                                                                                      datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'))


    client_socket.send(response_data.encode())

client_socket.close()
server_socket.close()