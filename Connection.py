import cyberpi, time, event, mbot2, socket

class Client():
    
    def __init__(self, SERVER_IP, SERVER_PORT=8000):
        self.SERVER_IP = SERVER_IP
        self.SERVER_PORT = SERVER_PORT
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.client_socket.connect((self.SERVER_IP, self.SERVER_PORT))
            return True
        except Exception as e:
            cyberpi.console.print("Error al conectar al servidor: ")
            cyberpi.console.println(str(e))
            return False
        
    def send_msg(self, msg):
        self.client_socket.send(msg.encode("utf-8"))
        
    def recv_msg(self):
        response = self.client_socket.recv(1024)
        return response.decode("utf-8")
        
    def close_client(self):
        try:
            self.client_socket.close()
            return True
        except Exception as e:
            cyberpi.console.print("Error al conectar al servidor: ")
            cyberpi.console.println(str(e))
            return False

    def reconnect(self, max_retries=3):
        retries = 0
        while retries < max_retries:
            if self.connect():
                return True
            retries += 1
            time.sleep(1)  # Esperar antes de intentar nuevamente
        return False

    def send_binary(self, data):
        self.client_socket.send(data)

    def recv_binary(self, buffer_size):
        data = self.client_socket.recv(buffer_size)
        return data

    def handle_error(self, error_message):
        # Puedes implementar lógica para manejar errores aquí, como registrarlos en un archivo de registro.
        pass

    def set_timeout(self, timeout):
        self.client_socket.settimeout(timeout)

    def set_socket_option(self, option, value):
        self.client_socket.setsockopt(socket.SOL_SOCKET, option, value)

    def request_disconnect(self):
        self.client_socket.send(b'Disconnect')  # Envía una señal al servidor para solicitar una desconexión
