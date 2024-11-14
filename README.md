# Proyecto de Comunicación TCP (Cliente/Servidor)

Este proyecto implementa una comunicación básica cliente-servidor usando el protocolo TCP en Python. El servidor escucha conexiones en el puerto 5000 y responde a los mensajes enviados por los clientes. El cliente puede enviar mensajes y recibir respuestas en mayúsculas, o enviar el mensaje especial `DESCONEXION` para cerrar la conexión.

## Archivos del Proyecto

- **Servidor_TCP.py**: Implementa el servidor TCP que escucha en el puerto 5000, acepta conexiones de clientes y responde a los mensajes recibidos.
- **Cliente_TCP.py**: Implementa el cliente TCP que se conecta al servidor, envía mensajes y recibe respuestas.

## Descripción

El servidor espera conexiones entrantes de los clientes y responde con el mensaje recibido en mayúsculas. Si el cliente envía el mensaje `DESCONEXION`, el servidor cierra la conexión con ese cliente.

### Flujo de la Comunicación

1. El servidor escucha en el puerto 5000 por conexiones TCP.
2. El cliente se conecta al servidor y puede enviar mensajes.
3. El servidor responde con el mensaje en mayúsculas.
4. Si el cliente envía el mensaje `DESCONEXION`, el servidor cierra la conexión con ese cliente.

## Requisitos

- Python 3.x

No hay dependencias externas necesarias para este proyecto, ya que solo se utiliza la librería estándar de Python `socket`.

## Uso

### 1. Ejecutar el Servidor

Para iniciar el servidor, simplemente ejecuta el archivo `Servidor_TCP.py` en una terminal:

```bash
python Servidor_TCP.py
```
El servidor comenzará a escuchar en `localhost`en el puerto 5000.

### 2. Ejecutar el Cliente

Para conectar el cliente al servidor, ejecuta el archivo `SCliente_TCP.py`. Asegúrate de que el servidor esté en ejecución antes de iniciar el cliente.

```bash
python Cliente_TCP.py
```
El cliente se conectará al servidor y podrá enviar mensajes.

### 3. Enviar Mensajes

Una vez que el cliente esté conectado, puedes enviarle mensajes al servidor. El servidor responderá con el mensaje en mayúsculas.

### 4. Desconexión

Si deseas desconectar al cliente, simplemente ingresa el mensaje `DESCONEXION`. El servidor cerrará la conexión con el cliente y el cliente se desconectará.

## Ejemplo de Interacción

### Terminal del servidor:

```bash
Servidor escuchando...
Conexión aceptada de ('127.0.0.1', 12345)
```

### Terminal del cliente:

```bash
Conectado al servidor en localhost:5000
Ingresa un mensaje (o 'DESCONEXION' para salir): hola servidor
Servidor: HOLA SERVIDOR
Ingresa un mensaje (o 'DESCONEXION' para salir): DESCONEXION
Servidor: Conexión cerrada
```

### Terminal del servidor (después de desconexión):

```bash
Servidor escuchando...
Conexión aceptada de ('127.0.0.1', 59319)
Mensaje de desconexión recibido. Cerrando la conexión.
```
