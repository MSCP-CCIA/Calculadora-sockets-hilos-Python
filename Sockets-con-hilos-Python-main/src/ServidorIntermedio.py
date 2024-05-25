# Importa el módulo 'socket' para realizar operaciones de red, como la creación de conexiones TCP/IP.
import socket

# Importa la clase 'Thread' del módulo 'threading' para manejar subprocesos.
from threading import Thread

# Define la dirección IP del servidor.
TCP_IP = '127.0.0.1'

# Define el puerto del servidor.
TCP_PORT = 5000

# Define el tamaño del buffer que se usará para recibir datos.
BUFFER_SIZE = 1024

# Inicializa listas para almacenar la información de los servidores de operaciones matemáticas.
lsum = []
lsresta = []
lsmulti = []
lsdivi = []
lspote = []
lslogarit = []


# Define la clase 'Client' que hereda de 'Thread' para manejar conexiones de clientes en subprocesos.
class Client(Thread):

    # Método constructor de la clase 'Client'.
    def __init__(self, conn, addr):
        # Inicializa la clase padre 'Thread'.
        Thread.__init__(self)

        # Almacena la conexión y la dirección del cliente.
        self.conn = conn
        self.addr = addr

    # Método 'run' que se ejecuta cuando el subproceso se inicia.
    def run(self):
        # Recibe datos del cliente, decodificándolos de UTF-8.
        recibido = self.conn.recv(BUFFER_SIZE).decode("UTF-8")
        print(recibido)

        # Si el mensaje recibido es '<', significa que un servidor de operación matemática se ha conectado.
        if recibido == '<':
            print('Se ha conectado un servidor de operación matemática')

            # Recibe la información del servidor de operación matemática.
            infoserver = self.conn.recv(BUFFER_SIZE).decode("UTF-8")

            # Inicializa listas para almacenar los datos recibidos.
            ls = []
            lisnum = []
            lis = []
            ls = infoserver

            # Itera sobre los datos recibidos para separar los componentes de la información.
            for i in ls:
                if i == "@":
                    lis.append(lisnum)
                    lisnum = []
                if i != "@":
                    lisnum.append(i)
            print(lis)

            # Identifica el tipo de operación matemática y almacena la IP y el puerto del servidor correspondiente.
            opera = "".join(lis[0])
            if opera == '+':
                print('Operación matemática: Suma')
                lsum.append("".join(lis[1]))
                lsum.append("".join(lis[2]))
            if opera == '-':
                print('Operación matemática: Resta')
                lsresta.append("".join(lis[1]))
                lsresta.append("".join(lis[2]))
            if opera == '*':
                print('Operación matemática: Multiplicación')
                lsmulti.append("".join(lis[1]))
                lsmulti.append("".join(lis[2]))
            if opera == '/':
                print('Operación matemática: División')
                lsdivi.append("".join(lis[1]))
                lsdivi.append("".join(lis[2]))
            if opera == '^':
                print('Operación matemática: Potenciación')
                lspote.append("".join(lis[1]))
                lspote.append("".join(lis[2]))
            if opera == 'l':
                print('Operación matemática: Logaritmación')
                lslogarit.append("".join(lis[1]))
                lslogarit.append("".join(lis[2]))

        # Gestiona solicitudes de clientes para operaciones matemáticas.
        if recibido == '1':
            print("Se ha conectado un cliente solicitando la operación Suma")
            if len(lsum) > 1:
                direccion = 'si@' + lsum[0] + '@' + lsum[1] + '@SUMA@'
                self.conn.send(direccion.encode("UTF-8"))
            else:
                self.conn.send('o'.encode("UTF-8"))

        if recibido == '2':
            print("Se ha conectado un cliente solicitando la operación Resta")
            if len(lsresta) > 1:
                direccion = 'si@' + lsresta[0] + '@' + lsresta[1] + '@RESTA@'
                self.conn.send(direccion.encode("UTF-8"))
            else:
                self.conn.send('o'.encode("UTF-8"))

        if recibido == '3':
            print("Se ha conectado un cliente solicitando la operación Multiplicación")
            if len(lsmulti) > 1:
                direccion = 'si@' + lsmulti[0] + '@' + lsmulti[1] + '@MULTIPLICACION@'
                self.conn.send(direccion.encode("UTF-8"))
            else:
                self.conn.send('o'.encode("UTF-8"))

        if recibido == '4':
            print("Se ha conectado un cliente solicitando la operación División")
            if len(lsdivi) > 1:
                direccion = 'si@' + lsdivi[0] + '@' + lsdivi[1] + '@DIVISION@'
                self.conn.send(direccion.encode("UTF-8"))
            else:
                self.conn.send('o'.encode("UTF-8"))

        if recibido == '5':
            print("Se ha conectado un cliente solicitando la operación Potenciación")
            if len(lspote) > 1:
                direccion = 'si@' + lspote[0] + '@' + lspote[1] + '@POTENCIACION@'
                self.conn.send(direccion.encode("UTF-8"))
            else:
                self.conn.send('o'.encode("UTF-8"))

        if recibido == '6':
            print("Se ha conectado un cliente solicitando la operación Logaritmación")
            if len(lslogarit) > 1:
                direccion = 'si@' + lslogarit[0] + '@' + lslogarit[1] + '@LOGARITMACION@'
                self.conn.send(direccion.encode("UTF-8"))
            else:
                self.conn.send('o'.encode("UTF-8"))


# Define la función principal del servidor.
def main():
    # Crea un socket para escuchar conexiones entrantes.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Asocia el socket a la dirección IP y el puerto especificados.
    s.bind((TCP_IP, TCP_PORT))

    # Permite reutilizar la dirección del socket.
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # El socket comienza a escuchar conexiones entrantes, con una cola de hasta 5 conexiones.
    s.listen(5)
    print("Servidor intermedio multihilo esperando peticiones...")

    try:
        # Bucle infinito para aceptar conexiones de clientes.
        while True:
            conn, addr = s.accept()

            # Crea un objeto 'Client' para manejar la conexión del cliente en un subproceso.
            c = Client(conn, addr)

            # Inicia el subproceso.
            c.start()
    except KeyboardInterrupt:
        # Maneja la interrupción del teclado (Ctrl+C) para detener el servidor.
        print("Servidor detenido.")
    finally:
        # Cierra el socket del servidor.
        s.close()


# Punto de entrada del script. Si es el programa principal, ejecuta la función 'main'.
if __name__ == "__main__":
    main()
