import socket


ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
print('host:',host)

port = 8888

ss.bind(('localhost', port))

ss.listen(5)
while True:
    cs, addr = ss.accept()
    print('连接地址：{}'.format(addr))
    cs.send('天若有情天易老， 人间正道是沧桑\r\n'.encode('utf-8'))
    cs.close()








