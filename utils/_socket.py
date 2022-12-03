import socket
import threading

srv = socket.socket()

class Server():
    def __init__(self, port: int, hostIp: str, listenNum = 5) -> None:
        self.ip = hostIp
        self.port = port
        self.listenNum = listenNum
        srv.bind((hostIp, port))
        srv.listen(listenNum)
        print("Server Side Init!")

    def info(self):
        text = f"=====Server Info=====\nIP: {self.ip}\nPort: {self.port}\nlistenNum: {self.listenNum}\n====================="
        return text

    def connect(self):
        while True:
            print("waitting connect... (press \"crtl + c\" to exit)")
            connect_socket, client_addr = srv.accept()
            print(f"successful connect from {client_addr}")
            recevent = connect_socket.recv(1024)
            print(f"recive message from {client_addr}: {str(recevent, encoding='utf-8')}")
            connect_socket.send(bytes(f"Here are {self.ip}, successful recive your message: {recevent}", encoding='utf-8'))

    def open(self):
        t = threading.Thread(target=self.connect)
        t.start()

class Client():
    def __init__(self, hostIp: str, port: int) -> None:
        self.Ip = hostIp
        self.port = port
        clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSock.connect((hostIp, port))
        print("Client Side Init!")
    
    def connenct(self):
        pass