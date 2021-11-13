""" rate client module """
import logging
import sys
import socket
from pathlib import Path

from python_demos.rates_app.client_connect import client_connect


def main() -> None:
    """ main """

    logging.basicConfig(
        level=logging.WARNING,
        filename=Path(
            "logs",
            "rates_app_client.log"),
        format='%(asctime)s,%(levelname)s,%(name)s,%(message)s')

    logging.debug("Program started")

    try:
        client_connect('127.0.0.1', 5050)

    except KeyboardInterrupt:
        logging.debug("Program exiting via Ctrl-C")

    except Exception as exc:  # pylint: disable=broad-except
        logging.critical("Unexpected error:\n%s", exc, exc_info=True)

    logging.debug("Program exiting")


if __name__ == "__main__":
    main()
