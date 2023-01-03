from socket import *

# 서버 IP address
serverName = '127.0.0.1'

# 서버에서 지정한 포트번호
serverPort = 12000

# 클라이언트 소켓 객체 생성
# AF_INET: IPv4 주소체계 사용
# SOCK_STREAM : 소켓 타입으로 TCP 사용
clientSocket = socket(AF_INET, SOCK_STREAM)

# 지정한 Host 와 Port 로 서버에 접속
clientSocket.connect((serverName, serverPort))

# Client 측에서 요청하는 HTTP Method 와 HTTP request message
User_Agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)'
method = {
    'GET': f'GET / HTTP/1.1\r\nHost: {serverName}:{serverPort}\r\nUser-Agent: {User_Agent}\r\nAccept: */*\r\n\r\n',
    'POST': f'POST / HTTP/1.1\r\nHost: {serverName}:{serverPort}\r\nUser-Agent: {User_Agent}\r\nAccept: */*\r\nContent-Length: 0\r\n\r\n',
    'HEAD': f'HEAD / HTTP/1.1\r\nHost: {serverName}:{serverPort}\r\nUser-Agent: {User_Agent}\r\nAccept: */*\r\n\r\n',
    'PUT': f'PUT / HTTP/1.1\r\nHost: {serverName}:{serverPort}\r\nUser-Agent: {User_Agent}\r\nAccept: */*\r\nContent-Length: 0\r\n\r\n',
    'DELETE': f'DELETE / HTTP/1.1\r\nHost: {serverName}:{serverPort}\r\nUser-Agent: {User_Agent}\r\nAccept: */*\r\n\r\n',
}
# HTTP 1.1 이므로 tcp 통신을 유지한 채 여러 데이터를 병렬식으로 보낼 수 있다.
while True:
    msg = input('Request Method:')

    # end 를 입력하면 반복문을 빠져나간다.
    if msg == "end":
        break

    # 사용자가 입력한 method 에 해당하는 request_message 를 만든다.
    if msg in method.keys():
        request_message = method[msg]

    # 이외 method 를 입력하거나 잘못 입력 한 경우 'Method Not Allowed' request message 를 전달한다.
    else:
        request_message = f'NotAllowed / HTTP/1.1\r\nHost: {serverName}:{serverPort}\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)\r\nAccept: */*\r\n\r\n'

    # 서버로 request_message 를 보낸다.
    clientSocket.send(request_message.encode('utf-8'))

    # 클라이언트 소켓으로부터 최대 1024 bytes 만큼의 데이터를 읽어 온다.
    receive_message = clientSocket.recv(1024)

    # 읽어온 데이터를 출력한다.
    print(receive_message.decode())

# 소켓 통신 종료
clientSocket.close()
