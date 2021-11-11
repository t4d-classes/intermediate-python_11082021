""" Test Patterns Module """

from unittest import TestCase
from unittest.mock import patch, Mock

from python_demos.ut_app.patterns import action_a, action_b, console_log


class TestPatterns(TestCase):
    """ Test Patterns Class """

    @patch("python_demos.ut_app.patterns.console_log")
    def test_action_a(self, console_log) -> None:

        action_a()
        console_log.assert_called_once_with("action a")

    def test_action_a_alt(self) -> None:

        with patch("python_demos.ut_app.patterns.console_log") as console_log:
            action_a()
            console_log.assert_called_once_with("action a")

    def test_action_b(self) -> None:

        # arrange
        mock_log = Mock()

        # act

        action_b(mock_log)

        # assert
        mock_log.assert_called_once_with("action b")
        

    @patch("python_demos.ut_app.patterns.print")
    def test_console_log(self, print) -> None:

        console_log("test")
        print.assert_called_once_with("test")
