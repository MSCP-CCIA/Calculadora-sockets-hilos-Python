# Importa el módulo 'socket' que permite realizar operaciones de red, como la creación de conexiones TCP/IP.
import socket

# Define la dirección IP del servidor con el que se establecerá la conexión.
TCP_IP = '127.0.0.1'

# Define el puerto del servidor al que se conectará el cliente.
TCP_PORT = 5000

# Define el tamaño del buffer que se usará para recibir datos del servidor.
BUFFER_SIZE = 1024


# Define la función principal que contendrá el bucle principal del programa.
def main():
    # Bucle infinito que permite al usuario realizar múltiples operaciones hasta que decida salir.
    while True:
        # Crea un nuevo socket TCP/IP (AF_INET es la familia de direcciones, SOCK_STREAM es el tipo de socket).
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Conecta el socket al servidor especificado por TCP_IP y TCP_PORT.
        s.connect((TCP_IP, TCP_PORT))

        # Imprime las opciones de operaciones matemáticas disponibles para el usuario.
        print("Operaciones:")
        print("1. Suma | 2. Resta | 3. Multiplicación | 4. División | 5. Potenciación | 6. Logaritmación")
        print("Digite la operación sin puntos: ")

        # Lee la operación seleccionada por el usuario desde la entrada estándar.
        operacion = input()

        # Envía la operación seleccionada al servidor, codificándola en UTF-8.
        s.send(operacion.encode("UTF-8"))

        # Recibe la respuesta del servidor, decodificándola de UTF-8.
        recibido = s.recv(BUFFER_SIZE).decode("UTF-8")

        # Asigna la respuesta recibida a la variable 'ls'.
        ls = recibido

        # Verifica si la longitud de 'ls' es mayor que 1, indicando que contiene datos válidos.
        if len(ls) > 1:
            # Divide la respuesta recibida en partes usando el carácter '@' como separador.
            lis = recibido.split('@')

            # Asigna las partes de la respuesta a variables individuales.
            cod = lis[0]
            IP = lis[1]
            PORT = lis[2]
            OPERAC = lis[3]

            # Verifica si el código recibido es 'si', indicando que el servidor está listo para realizar la operación.
            if cod == 'si':
                # Solicita al usuario ingresar dos números para realizar la operación.
                print(f"Digite dos números para realizar {OPERAC}:")
                print("Número 1:")
                numero1 = input()
                print("Número 2:")
                numero2 = input()

                # Combina los dos números ingresados en una sola cadena, separada por '@'.
                num = numero1 + '@' + numero2

                # Cierra el socket actual.
                s.close()

                # Crea un nuevo socket TCP/IP.
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                # Conecta el nuevo socket a la IP y puerto especificados en la respuesta del servidor.
                s.connect((str(IP), int(PORT)))

                # Envía los números al servidor, codificándolos en UTF-8.
                s.send(num.encode("UTF-8"))

                # Recibe el resultado de la operación del servidor, decodificándolo de UTF-8.
                resultado = s.recv(BUFFER_SIZE).decode("UTF-8")

                # Imprime el resultado de la operación.
                print(f"El resultado de la operación {OPERAC} es: {resultado}")

                # Cierra el socket.
                s.close()
            else:
                # Si el código no es 'si', imprime un mensaje indicando que la respuesta del servidor no fue reconocida.
                print("Respuesta no reconocida del servidor.")
        else:
            # Si la longitud de 'ls' es 1 y es 'o', indica que el servidor está apagado.
            if recibido == 'o':
                print("El servidor al que intenta acceder se encuentra Apagado (OFF). Intente más tarde por favor...")

        # Pregunta al usuario si desea realizar otra operación.
        print("¿Desea realizar otra operación? (sí/no):")

        # Lee la respuesta del usuario, eliminando espacios y convirtiéndola a minúsculas.
        continuar = input().strip().lower()

        # Si la respuesta no es 'sí', sale del bucle.
        if continuar != 'sí':
            break


# Si este script es el programa principal, ejecuta la función 'main'.
if __name__ == "__main__":
    main()
