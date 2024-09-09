from rcon import Client

class RCONManager:
    def __init__(self, host, port, password):
        self.host = host
        self.port = port
        self.password = password

    def run_command(self, command):
        try:
            with Client(self.host, self.port, passwd=self.password) as client:
                return client.run(command)
        except Exception as e:
            return f"Failed to run command: {str(e)}"
