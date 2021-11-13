""" rate client module """
import logging
import socket
from pathlib import Path

logger = logging.getLogger(__name__)

clientCommandsLogger = logging.getLogger("client_commands")
clientCommandsLogger.setLevel(logging.INFO)

clientCommandsFileHandler = logging.FileHandler(
    Path("logs", "client_commands.log")
)
clientCommandsFileHandler.setLevel(logging.INFO)


clientCommandsLogger.addHandler(clientCommandsFileHandler)


def client_connect(host: str, port: int) -> None:
    """ client_connect """

    try:

        with socket.socket(
                socket.AF_INET, socket.SOCK_STREAM) as socket_client:

            socket_client.connect((host, port))

            welcome_message = socket_client.recv(2048)

            print(welcome_message.decode('UTF-8'))

            while True:

                command = input("> ")

                clientCommandsLogger.info("Command: %s", command)

                if command == "exit":
                    break
                else:
                    socket_client.sendall(command.encode('UTF-8'))
                    print(socket_client.recv(2048).decode('UTF-8'))

    except ConnectionRefusedError:
        logger.exception("Unable to connect to the server %s:%d", host, port)
    except ConnectionResetError:
        logger.exception("Server connection was closed.")
