""" Test Client Commands Module """

from unittest import TestCase

from python_demos.rates_app.client_commands import parse_command


class TestClientCommands(TestCase):
    """ Test Client Commands Class """

    def test_parse_command(self) -> None:
        """ Parse Command Test """

        client_command = "GET 2021-04-01 CAD"

        result = parse_command(client_command)

        # self.assertEqual(result, {
        #     "name": "GET",
        #     "date": "2021-04-01",
        #     "symbols": "CAD"
        # })

        self.assertDictEqual(result, {
            "name": "GET",
            "date": "2021-04-01",
            "symbols": "CAD"
        })

    def test_parse_command_invalid_format(self) -> None:
        """ Parse Command Test """

        client_command = "JUNK"

        result = parse_command(client_command)

        # self.assertEqual(result, None)

        self.assertIsNone(result)
