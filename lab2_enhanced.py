import socket
import sys
import threading

class MyThread(threading.Thread):

    # Override for thread
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn
        self.starts = ''
        
    # Override for thread
    def run(self):
        while True:
            data = self.conn.recv(1024)
            if data[0:len(data)-2] == chr(27):
                break
            data2 = str(data)
            reply = '<<<Hello ' + data2[0:len(data2)-2] + '>>>' + '\r\n'
            self.conn.sendall(reply.encode('UTF8'))
        self.conn.close()
            

if __name__ == "__main__":
    host = ''
    port = 8888
    
    # Server: create a socket
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print('Failed to create socket!')
        print('Error code: ' + str(msg[0]) + ', error mesage: ' + msg[1])
        sys.exit()
    print('Socket created successfully.')
        
    # Server: bind and Listen
    try:
        s.bind((host, port))
    except socket.error:
        msg = str(socket.error)
        print('Bind failed! Error code: ' + str(msg[0]) + ', message: ' + msg[1])
        sys.exit()
    print('Socket bind complete.')
    s.listen(10)
    print('Socket is now listening.')
        
    # Server: accept connection, receive and reply msg
    while True:
        conn, addr = s.accept()
        thread = MyThread(conn)
        thread.start()
        
    # Cose the Socket    
    s.close()

    

'''
# Client: connection
try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print('Host name could not be resolved')
    sys.exit()
print('IP address of ' + host + ' is ' + remote_ip)
s.connect((remote_ip, port))
print('Socket connected to ' +host + ' on ip ' + remote_ip)

# Client: send Data
message = 'GET / HTTP/1.1\r\n\r\n'
try:
    s.sendall(message.encode("UTF8"))
except socket.error:
    print('Send failed!')
    sys.exit()
print('Message sent successfully.')

reply = s.recv(4096)
print(reply)
s.close()
'''