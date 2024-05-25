# Importa el módulo 'socket' para realizar operaciones de red, como la creación de sockets TCP/IP.
import socket

# Importa el módulo 'concurrent.futures' para realizar operaciones concurrentes y ejecutar tareas en paralelo.
import concurrent.futures

# Importa el módulo 'csv' para trabajar con archivos CSV y escribir los resultados de la prueba en un archivo CSV.
import csv

# Importa el módulo 'time' para medir el tiempo de ejecución de las operaciones.
import time

# Dirección IP del servidor al que se conectarán los clientes.
TCP_IP = '127.0.0.1'

# Puerto del servidor al que se conectarán los clientes.
TCP_PORT = 5000

# Tamaño del búfer utilizado para recibir datos del servidor.
BUFFER_SIZE = 1024


# Función para realizar una operación con el servidor.
def perform_operation(operation_code, num1, num2):
    # Registra el tiempo de inicio de la operación.
    start_time = time.time()

    # Crea un socket TCP/IP.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Establece la conexión con el servidor.
        s.connect((TCP_IP, TCP_PORT))

        # Envía el código de operación al servidor.
        s.send(operation_code.encode("UTF-8"))

        # Recibe la respuesta inicial del servidor y la decodifica.
        initial_response = s.recv(BUFFER_SIZE).decode("UTF-8")

        # Verifica la respuesta inicial del servidor.
        if len(initial_response) > 1:
            # Divide la respuesta en partes utilizando el carácter '@' como separador.
            parts = initial_response.split('@')

            # Verifica si el servidor está listo para realizar la operación.
            if parts[0] == 'si':
                # Obtiene la dirección IP, puerto y tipo de operación del servidor.
                ip = parts[1]
                port = int(parts[2])
                operation = parts[3]

                # Combina los números de la operación en una cadena separada por '@'.
                numbers = f"{num1}@{num2}"

                # Crea un nuevo socket para la operación específica.
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_operation:
                    # Establece la conexión con el servidor de la operación.
                    s_operation.connect((ip, port))

                    # Envía los números al servidor de la operación.
                    s_operation.send(numbers.encode("UTF-8"))

                    # Recibe el resultado de la operación del servidor de la operación.
                    result = s_operation.recv(BUFFER_SIZE).decode("UTF-8")

                    # Registra el tiempo de finalización de la operación.
                    end_time = time.time()

                    # Calcula la duración de la operación.
                    duration = end_time - start_time

                    # Devuelve el resultado de la operación y la duración.
                    return f"Resultado de {operation}: {result}", duration
            else:
                # Devuelve un mensaje de error si la respuesta del servidor no es reconocida.
                return "Respuesta no reconocida del servidor.", None
        else:
            # Devuelve un mensaje de error si la respuesta del servidor no es válida.
            if initial_response == 'o':
                return "El servidor está apagado. Intente más tarde.", None
            return "Respuesta del servidor no válida.", None


# Función para ejecutar la prueba de estrés con un número específico de clientes.
def run_stress_test(num_clients):
    # Lista para almacenar los resultados de la prueba.
    results = []

    # Crea un ThreadPoolExecutor para manejar múltiples hilos de ejecución.
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_clients) as executor:
        # Crea una lista de tareas (futuros) para realizar la operación en paralelo.
        futures = [executor.submit(perform_operation, "1", "2", "3") for _ in range(num_clients)]

        # Itera sobre los futuros a medida que se completan.
        for future in concurrent.futures.as_completed(futures):
            # Obtiene el resultado y la duración de cada tarea.
            result, duration = future.result()

            # Agrega el resultado y la duración a la lista de resultados.
            results.append((result, duration))

            # Imprime el resultado en la consola.
            print(result)

    # Devuelve la lista de resultados.
    return results


# Función para escribir los resultados de la prueba en un archivo CSV.
def write_results_to_csv(results, filename="stress_test_results.csv"):
    # Abre el archivo CSV en modo de escritura.
    with open(filename, mode='w', newline='') as file:
        # Crea un escritor CSV.
        writer = csv.writer(file)

        # Escribe la fila de encabezado en el archivo CSV.
        writer.writerow(["Result", "Duration"])

        # Itera sobre los resultados y escribe cada resultado en una fila del archivo CSV.
        for result, duration in results:
            writer.writerow([result, duration])


# Punto de entrada del script.
if __name__ == "__main__":
    # Número de clientes que se utilizarán en la prueba de estrés.
    num_clients = 100  # Cambia este valor según el número de clientes que deseas simular
    results = run_stress_test(num_clients)
    write_results_to_csv(results)
    print(f"Resultados guardados en stress_test_results.csv")

