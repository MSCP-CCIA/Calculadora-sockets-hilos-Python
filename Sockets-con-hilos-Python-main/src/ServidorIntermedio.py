import socket
from threading import Thread

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
lsum=[]
lsresta=[]
lsmulti=[]
lsdivi=[]
lspote=[]
lslogarit=[]

#Clase para recibir a los clientes
class Client(Thread):
      
    def __init__(self, conn, addr):
        # Inicializar clase padre.
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr
    def run(self):

        # Recibir datos del cliente.
        recibido = self.conn.recv(BUFFER_SIZE).decode("UTF-8")
        print (recibido)
        if recibido== '<':
            print('Se ha conectado un servidor de operación matematica')
            infoserver=self.conn.recv(BUFFER_SIZE).decode("UTF-8")
            ls=[]
            lisnum=[]
            lis=[]
            ls=infoserver
            for i in ls:
                if i == "@":
                    lis.append(lisnum)
                    lisnum=[]
                if i != "@":
                    lisnum.append(i)
            print (lis)
            opera="".join(lis[0])
            if opera=='+':
                print('Operación matematica: Suma')
                lsum.append("".join(lis[1]))
                lsum.append("".join(lis[2]))
            if opera=='-':
                print('Operación matematica: Resta')
                lsresta.append("".join(lis[1]))
                lsresta.append("".join(lis[2]))
            if opera=='*':
                print('Operación matematica: Multiplicacion')
                lsmulti.append("".join(lis[1]))
                lsmulti.append("".join(lis[2]))
            if opera=='/':
                print('Operación matematica: Division')
                lsdivi.append("".join(lis[1]))
                lsdivi.append("".join(lis[2]))
            if opera=='^':
                print('Operación matematica: Potenciacion')
                lspote.append("".join(lis[1]))
                lspote.append("".join(lis[2]))
            if opera=='l':
                print('Operación matematica: Logaritmacion')
                lslogarit.append("".join(lis[1]))
                lslogarit.append("".join(lis[2]))
           
        if recibido == '1':
            print("Se ha conectado un cliente solicitando la operacion Suma")
            if len(lsum) > 1:   
                direccion='si@'+lsum[0]+'@'+lsum[1]+'@SUMA@'
                self.conn.send(direccion.encode("UTF-8"))
            self.conn.send('o'.encode("UTF-8"))
            
        if recibido == '2':
            print("Se ha conectado un cliente solicitando la operacion Resta")
            if len(lsresta) > 1:   
                direccion='si@'+lsresta[0]+'@'+lsresta[1]+'@RESTA@'
                self.conn.send(direccion.encode("UTF-8"))
            self.conn.send('o'.encode("UTF-8"))
            
        if recibido == '3':
            print("Se ha conectado un cliente solicitando la operacion Multiplicacion")
            if len(lsmulti) > 1:   
                operacion='MULTIPLICACION' 
                direccion='si@'+lsmulti[0]+'@'+lsmulti[1]+'@MULTIPLICACION@'
                self.conn.send(direccion.encode("UTF-8"))
            self.conn.send('o'.encode("UTF-8"))
            
        if recibido =='4':
            print("Se ha conectado un cliente solicitando la operacion Division")
            if len(lsdivi) > 1:   
                direccion='si@'+lsdivi[0]+'@'+lsdivi[1]+'@DIVICION@'
                self.conn.send(direccion.encode("UTF-8"))
            self.conn.send('o'.encode("UTF-8"))
            
        if recibido == '5':
            print("Se ha conectado un cliente solicitando la operacion Potenciacion")
            if len(lspote) > 1:   
                direccion='si@'+lspote[0]+'@'+lspote[1]+'@POTENCIACION@'
                self.conn.send(direccion.encode("UTF-8"))
            self.conn.send('o'.encode("UTF-8"))
            
        if recibido == '6':
            print("Se ha conectado un cliente solicitando la operacion Logaritmacion")
            if len(lslogarit) > 1:    
                direccion='si@'+lslogarit[0]+'@'+lslogarit[1]+'@LOGARITMACION@'
                self.conn.send(direccion.encode("UTF-8"))
            self.conn.send('o'.encode("UTF-8"))
            
        
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.listen(5)
    print("Servidor intermedio multihilo esperando peticiones...")
    try:
        while True:
            conn, addr = s.accept()
            c = Client(conn, addr)
            c.start()
    except KeyboardInterrupt:
        print("Servidor detenido.")
    finally:
        s.close()

if __name__ == "__main__":
    main()