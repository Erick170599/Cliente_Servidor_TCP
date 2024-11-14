import socket


def Iniciar_Servidor():

    try:
        # Crear el socket TCP
        servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Configurar el servidor para escuchar en localhost y puerto 5000
        servidor_socket.bind(('localhost', 5000))

        # Especificar número de clientes posibles a conectar
        servidor_socket.listen(5)
        print("Servidor escuchando...")

    except Exception as e:
        print(f'Error al inicializar el servidor: {e}')

    while True:
        try:
            # Esperar a que un cliente se conecte
            cliente_socket, direccion = servidor_socket.accept()
            print(f"Conexión aceptada de {direccion}")

        except Exception as e:
            print(f'Error al aceptar la conexión: {e}')

        while True:
            try:
                # Recibir el mensaje del cliente
                mensaje = cliente_socket.recv(1024).decode('utf-8')
                if mensaje == "DESCONEXION":
                    print("Mensaje de desconexión recibido. Cerrando la conexión.")
                    cliente_socket.send("Conexión cerrada".encode('utf-8'))
                    # Cerrar la conexión con el cliente
                    cliente_socket.close()
                    # Salir del bucle de espera de mensajes para aceptar un nuevo cliente
                    break

                # Responder con el mensaje en mayúsculas
                mensaje_respuesta = mensaje.upper()
                cliente_socket.send(mensaje_respuesta.encode('utf-8'))

            except Exception as e:
                print(f'Error al recibir o enviar mensaje: {e}')


if __name__ == "__main__":
    Iniciar_Servidor()
