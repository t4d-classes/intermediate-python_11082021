""" server process module """

from multiprocessing.sharedctypes import Synchronized  # type: ignore

import socket

from .client_connection_thread import ClientConnectionThread


def rate_server(host: str, port: int, client_count: Synchronized) -> None:
    """rate server"""

    with socket.socket(
            socket.AF_INET, socket.SOCK_STREAM) as socket_server:

        socket_server.bind((host, port))
        socket_server.listen()

        while True:

            conn, _ = socket_server.accept()

            with client_count.get_lock():
                client_count.value += 1

            client_con_thread = ClientConnectionThread(conn, client_count)
            client_con_thread.start()
