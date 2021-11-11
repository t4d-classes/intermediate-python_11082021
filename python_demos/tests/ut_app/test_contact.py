""" Test Sample Module """

from unittest import TestCase
from unittest.mock import Mock, create_autospec, patch

from python_demos.ut_app.contact import PersonA, PersonB, Address


class TestContact(TestCase):
    """ Test Contact Class """

    @patch("python_demos.ut_app.contact.Address")
    def test_person_a_mailing(self, Address) -> None:

        # these three lines are the same
        # addr = Address.return_value
        # addr = person.address
        addr = Address()
        addr.mailing.return_value = "123 Oak Ln.\nParis, TX 12345"

        with patch("python_demos.ut_app.contact.Address") as Address2:

            person = PersonA(
                "Bob",
                "Smith",
                "123 Oak Ln.",
                "Paris",
                "TX",
                "12345")

            Address.assert_called_once_with(
                "123 Oak Ln.", "Paris", "TX", "12345")

            actual_result = person.mailing()
            expected_result = "Bob Smith\n123 Oak Ln.\nParis, TX 12345"

            addr.mailing.assert_called_once()
            self.assertEqual(actual_result, expected_result)

    def test_person_b_mailing(self) -> None:

        addr = Mock()
        addr.mailing = Mock(return_value="123 Oak Ln.\nParis, TX 12345")

        person = PersonB("Bob", "Smith", addr)

        actual_result = person.mailing()
        expected_result = "Bob Smith\n123 Oak Ln.\nParis, TX 12345"

        addr.mailing.assert_called_once()
        self.assertEqual(actual_result, expected_result)

    def test_person_b_mailing_alt(self) -> None:

        MockAddress = create_autospec(Address)

        addr = MockAddress("123 Oak Ln.", "Paris", "TX", "12345")
        addr.mailing.return_value = "123 Oak Ln.\nParis, TX 12345"

        person = PersonB("Bob", "Smith", addr)

        actual_result = person.mailing()
        expected_result = "Bob Smith\n123 Oak Ln.\nParis, TX 12345"

        addr.mailing.assert_called_once()
        self.assertEqual(actual_result, expected_result)
