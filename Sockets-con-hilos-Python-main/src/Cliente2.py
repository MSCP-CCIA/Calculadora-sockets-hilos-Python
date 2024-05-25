import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024


def main():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))

        print("Operaciones:")
        print("1. Suma | 2. Resta | 3. Multiplicación | 4. División | 5. Potenciación | 6. Logaritmación")
        print("Digite la operación sin puntos: ")
        operacion = input()
        s.send(operacion.encode("UTF-8"))
        recibido = s.recv(BUFFER_SIZE).decode("UTF-8")
        ls = recibido

        if len(ls) > 1:
            lis = recibido.split('@')
            cod = lis[0]
            IP = lis[1]
            PORT = lis[2]
            OPERAC = lis[3]

            if cod == 'si':
                print(f"Digite dos números para realizar {OPERAC}:")
                print("Número 1:")
                numero1 = input()
                print("Número 2:")
                numero2 = input()
                num = numero1 + '@' + numero2

                s.close()
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(IP), int(PORT)))
                s.send(num.encode("UTF-8"))
                resultado = s.recv(BUFFER_SIZE).decode("UTF-8")
                print(f"El resultado de la operación {OPERAC} es: {resultado}")
                s.close()
            else:
                print("Respuesta no reconocida del servidor.")
        else:
            if recibido == 'o':
                print("El servidor al que intenta acceder se encuentra Apagado (OFF). Intente más tarde por favor...")

        # Preguntar al usuario si desea realizar otra operación
        print("¿Desea realizar otra operación? (sí/no):")
        continuar = input().strip().lower()
        if continuar != 'si':
            break


if __name__ == "__main__":
    main()
