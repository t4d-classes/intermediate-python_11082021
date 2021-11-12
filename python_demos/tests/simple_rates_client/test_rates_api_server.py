

from unittest import TestCase
from unittest.mock import patch

from python_demos.simple_rates_client.rates_api_server import rates_api_server


class TestRatesApiServer(TestCase):

    @patch("python_demos.simple_rates_client.rates_api_server.start_rates_api")
    @patch("python_demos.simple_rates_client.rates_api_server.requests")
    @patch("python_demos.simple_rates_client.rates_api_server.mp")
    def test_start_rates_api(self, mp, requests, start_rates_api) -> None:

        rates_api_server_fn = rates_api_server.__wrapped__

        gen = rates_api_server_fn()

        next(gen)

        mp.Process.assert_called_once_with(target=start_rates_api)
        mp.Process.return_value.start.assert_called_once()
        requests.get.assert_called_once_with("http://127.0.0.1:5000/check")

        next(gen, None)

        mp.Process.return_value.terminate.assert_called_once()
        

    @patch("python_demos.simple_rates_client.rates_api_server.start_rates_api")
    @patch("python_demos.simple_rates_client.rates_api_server.requests")
    @patch("python_demos.simple_rates_client.rates_api_server.mp")
    def test_start_rates_api_conn_error(
            self, mp, requests, start_rates_api) -> None:

        requests.get.side_effect = [
            ConnectionError(),
            True
        ]

        rates_api_server_fn = rates_api_server.__wrapped__

        gen = rates_api_server_fn()

        next(gen)

        mp.Process.assert_called_once_with(target=start_rates_api)
        mp.Process.return_value.start.assert_called_once()
        requests.get.assert_called_with("http://127.0.0.1:5000/check")

        next(gen, None)

        mp.Process.return_value.terminate.assert_called_once()
