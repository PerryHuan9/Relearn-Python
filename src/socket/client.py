import socket 


cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cs.connect(('127.0.0.1', 8888))
msg = cs.recv(1024)
cs.close()
print(msg.decode('utf-8'))