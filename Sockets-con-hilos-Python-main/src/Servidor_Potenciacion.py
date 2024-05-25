# Importa el módulo 'math', aunque no se utiliza en este código.
import math

# Importa el módulo 'socket' para realizar operaciones de red, como la creación de conexiones TCP/IP.
import socket

# Importa la clase 'Thread' del módulo 'threading' para manejar subprocesos.
from threading import Thread

# Importa el módulo 'time' que proporciona funciones para manipular el tiempo.
import time

# Define la dirección IP del servidor.
TCP_IP = '127.0.0.1'

# Define el puerto del servidor.
TCP_PORT = 5005

# Define el tamaño del buffer que se usará para recibir datos.
BUFFER_SIZE = 1024


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
        print("Se ha conectado un cliente solicitando la operacion potenciacion")

        # Recibe datos del cliente, decodificándolos de UTF-8.
        data1 = self.conn.recv(BUFFER_SIZE).decode("UTF-8")
        print("Dato recibido: ", data1)

        # Inicializa listas para almacenar los números.
        numero2 = []
        ls = []
        ls = data1

        # Itera sobre los datos recibidos para separar los números.
        for i in ls:
            if i != "@":
                numero2.append(i)
            if i == "@":
                numero1 = numero2
                numero2 = []

        # Une los números separados en cadenas.
        num1 = "".join(numero1)
        num2 = "".join(numero2)

        # Realiza la potenciación de los números convertidos a enteros.
        suma = int(num1) ** int(num2)
        print("Dato enviado: ", suma)

        # Envía el resultado de la potenciación al cliente, codificándolo en UTF-8.
        self.conn.send(str(suma).encode("UTF-8"))


# Define la función principal del servidor.
def main():
    # Crea un socket para conectarse al servidor central.
    cliente_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecta el socket al servidor central en la IP y puerto especificados.
    cliente_server.connect(('127.0.0.1', 5000))

    # Envía un mensaje al servidor central para registrarse.
    cliente_server.send('<'.encode("UTF-8"))

    # Espera un segundo.
    time.sleep(1)

    # Crea una cadena con la dirección IP y el puerto del servidor de potenciación.
    direccion = '^' + '@' + TCP_IP + '@' + str(TCP_PORT) + '@'

    # Envía la dirección al servidor central.
    cliente_server.send(direccion.encode("UTF-8"))

    # Crea un nuevo socket para escuchar conexiones entrantes de clientes.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Asocia el socket a la dirección IP y el puerto especificados.
    s.bind((TCP_IP, TCP_PORT))

    # Permite reutilizar la dirección del socket.
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # El socket comienza a escuchar conexiones entrantes, con una cola de hasta 5 conexiones.
    s.listen(5)

    # Bucle infinito para aceptar conexiones de clientes.
    while True:
        # Acepta una conexión entrante.
        conn, addr = s.accept()

        # Crea un objeto 'Client' para manejar la conexión del cliente en un subproceso.
        c = Client(conn, addr)

        # Inicia el subproceso.
        c.start()

    # Cierra la conexión y el socket. (Nunca se alcanzará debido al bucle infinito).
    conn.close()
    s.close()


# Punto de entrada del script. Si es el programa principal, ejecuta la función 'main'.
if __name__ == "__main__":
    print("Servidor potenciacion escuchando...")
    main()

# Cierra la conexión y el socket al final del script. (No se alcanzará debido al bucle infinito en 'main').
conn.close()
s.close()

