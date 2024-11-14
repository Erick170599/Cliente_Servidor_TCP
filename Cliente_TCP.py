import socket


def Iniciar_Cliente():

    try:
        # Crear el socket TCP
        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Conectarse al servidor en localhost y puerto 5000
        cliente_socket.connect(('localhost', 5000))

    except Exception as e:
        print(f'Error al intentar conectarse al servidor: {e}')

    while True:
        try:
            # Solicitar al usuario un mensaje
            mensaje = input("Ingresa un mensaje (o 'DESCONEXION' para salir): ")

            # Enviar el mensaje al servidor
            cliente_socket.send(mensaje.encode('utf-8'))

            # Si el mensaje es "DESCONEXION", cerrar la conexión
            if mensaje == "DESCONEXION":
                respuesta = cliente_socket.recv(1024).decode('utf-8')
                print(f"Servidor: {respuesta}")
                cliente_socket.close()
                break

            # Recibir la respuesta del servidor
            respuesta = cliente_socket.recv(1024).decode('utf-8')
            print(f"Servidor: {respuesta}")

        except Exception as e:
            print(f'Error de comunicación con el servidor: {e}')


if __name__ == "__main__":
    Iniciar_Cliente()
