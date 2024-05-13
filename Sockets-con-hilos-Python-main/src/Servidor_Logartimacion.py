import math
import socket
from threading import Thread
import time
##SERVIDOR PRINCIPAL LOGARITMACION
TCP_IP = '127.0.0.1'
TCP_PORT = 5006
BUFFER_SIZE = 1024

class Client(Thread):
      
    def __init__(self, conn, addr):
        # Inicializar clase padre.
        Thread.__init__(self)
        
        self.conn = conn
        self.addr = addr
    
    def run(self):
        print("Se ha conectado un cliente solicitando la operacion logaritmacion")
        data1 = self.conn.recv(BUFFER_SIZE).decode("UTF-8")
        print ("Dato recibido: ", data1)
        numero2=[]
        ls=[]
        ls=data1
        for i in ls:
          if i != "@":
            numero2.append(i)
          if i == "@":
            numero1=numero2
            numero2=[]
        num1="".join(numero1)
        num2="".join(numero2)
  
        suma=math.log(int(num1),int(num2))
        print ("Dato enviado: ", suma)
        self.conn.send(str(suma).encode("UTF-8"))  

        
def main():
    cliente_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_server.connect(('127.0.0.1', 5000))
    cliente_server.send('<'.encode("UTF-8"))
    time.sleep(1)
    direccion='l'+'@'+TCP_IP+'@'+str(TCP_PORT)+'@'
    cliente_server.send(direccion.encode("UTF-8"))
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.listen(5)
    
    while True:
        conn, addr = s.accept()
        c = Client(conn, addr)
        c.start()
    conn.close()
    s.close()
if __name__ == "__main__":
    print ("Servidor logaritmacion escuchando...")
    main()
conn.close()
s.close()
