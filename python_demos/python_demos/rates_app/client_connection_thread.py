""" client connection thread """

from typing import Any
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.sharedctypes import Synchronized  # type: ignore
from datetime import datetime, date

import socket
import threading
import re
import requests

from .client_commands import parse_command


CURRENCY_SYMBOLS_REGEX = re.compile(r"[,:;|]")


class ClientConnectionThread(threading.Thread):
    """ client connection thread """

    def __init__(
            self,
            conn: socket.socket,
            client_count: Synchronized) -> None:

        threading.Thread.__init__(self)
        self.conn = conn
        self.client_count = client_count

    def run(self) -> None:

        # pylint: disable=broad-except

        try:

            self.conn.sendall(b"Connected to the Rate Server")

            while True:
                data = self.conn.recv(2048)

                if not data:
                    break

                client_command_str: str = data.decode("UTF-8")

                client_command_dict = parse_command(client_command_str)

                if not client_command_dict:
                    self.conn.sendall(b"Invalid Command Format")
                else:
                    self.process_client_command(client_command_dict)

        except BaseException:
            pass

        finally:
            with self.client_count.get_lock():
                self.client_count.value -= 1

    def process_client_command(self, client_command: dict[str, Any]) -> None:
        """ process client command """

        if client_command["name"] == "GET":

            closing_date = datetime.strptime(
                client_command["date"], "%Y-%m-%d")

            currency_symbols = CURRENCY_SYMBOLS_REGEX.split(
                client_command["symbols"])

            rate_responses: list[str] = []

            with ThreadPoolExecutor() as executor:
                rate_responses = list(executor.map(
                    lambda p: self.get_rate_from_api(*p),
                    [(closing_date, currency_symbol)
                        for currency_symbol in currency_symbols]
                ))

            self.conn.sendall(
                "\n".join(rate_responses).encode("UTF-8"))

        else:
            self.conn.sendall(b"Invalid Command Name")

    @staticmethod
    def get_rate_from_api(closing_date: date, currency_symbol: str) -> str:
        """ get rate from api """

        url = "".join([
            "http://localhost:5000/api/",
            closing_date.strftime("%Y-%m-%d"),
            "?base=USD&symbols=",
            currency_symbol,
        ])

        response = requests.get(url)
        rate_data = response.json()

        return f"{currency_symbol} {rate_data['rates'][currency_symbol]}"
