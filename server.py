import socket

# 서버 IP address
serverName = '127.0.0.1'

# 서버에서 지정한 포트번호
serverPort = 12000

# 서버 소켓 객체 생성
# AF_INET: IPv4 주소체계 사용
# SOCK_STREAM : 소켓 타입으로 TCP 사용
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind : 서버가 사용 할 IP 주소와 port 번호를 결합 시키는 것
serverSocket.bind((serverName, serverPort))

# listen : client 로 부터 연결 요청이 수신이 되는지 주시 (1개의 client 만 허용)
serverSocket.listen(1)

print('Server Status : Healthy')
print(f"Server IP : {serverName}")
print(f"Server Port : {serverPort}\n")

# accept() 는 (소켓, 주소정보)로 구성되는 튜플을 리턴한다.
client_socket, addr = serverSocket.accept()

while True:

    # 클라이언트 소켓으로 부터 데이터를 읽어 온다.
    data = client_socket.recv(1024)
    request_data = data.decode().split()

    # client에서 end를 호출해 data가 넘어오지 않는 경우 반복문을 탈출한다.
    if not data:
        break

    # HTTP 프로토콜 method 및 version
    request_method = request_data[0]
    request_version = request_data[2]

    server_name = "Socket Server"

    # method 에 따른 status_code 설정
    status_code = {
        'GET': '200',
        'POST': '201',
        'HEAD': '203',
        'PUT': '202',
        'DELETE': '204',
    }

    # 해당 method 와 HTTP version 이 제대로 들어올 경우 처리
    if request_method in f"{status_code.keys()}" and request_version == "HTTP/1.1":
        print(request_method, request_version, f"{status_code[request_method]}\n")
        response_data = f"{request_version} {status_code[request_method]} OK\nServer: {server_name}\n"

    # 이외의 method 명령어 실행 시 405 Method Not Allowed 로 response
    else:
        print(request_method, request_version, "405 Method Not Allowed\n")
        response_data = f"{request_version} 405 Method Not Allowed\nServer: {server_name}\n"

    # 클라이언트에 response data 를 보낸다.
    client_socket.send(response_data.encode())

# client 에서 data 를 넘겨주지 않아 반복문 탈출 시 소켓 통신 종료
client_socket.close()
serverSocket.close()
