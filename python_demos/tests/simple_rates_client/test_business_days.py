""" Test Business Bays Module """

from unittest import TestCase, main
from unittest.mock import patch, Mock
from datetime import date, datetime

from python_demos.simple_rates_client.business_days import (
    business_days_list, EndBeforeStartException)


class TestBusinessDays(TestCase):
    """ Test Business Days Class """

    @patch("python_demos.simple_rates_client.business_days.holidays")
    def test_business_days(self, holidays) -> None:
        """ Business Days Test """

        holidays.UnitedStates.return_value = [
            date(2021, 4, 7), date(2021, 4, 8)]

        start_date = date(2021, 4, 1)
        end_date = date(2021, 4, 20)

        days = business_days_list(start_date, end_date)

        self.assertEqual(len(days), 12)

        expected_days = [
            date(2021, 4, 1),
            date(2021, 4, 2),
            date(2021, 4, 5),
            date(2021, 4, 6),
            date(2021, 4, 9),
            date(2021, 4, 12),
            date(2021, 4, 13),
            date(2021, 4, 14),
            date(2021, 4, 15),
            date(2021, 4, 16),
            date(2021, 4, 19),
            date(2021, 4, 20),
        ]

        self.assertListEqual(days, expected_days)

    @patch("python_demos.simple_rates_client.business_days.holidays")
    def test_business_days_invalid_args(self, holidays) -> None:
        """ Business Days Test """

        holidays.UnitedStates.return_value = [
            date(2021, 4, 7), date(2021, 4, 8)]

        start_date = date(2021, 4, 20)
        end_date = date(2021, 4, 1)

        with self.assertRaises(EndBeforeStartException):
            business_days_list(start_date, end_date)


if __name__ == "__main__":
    main()
