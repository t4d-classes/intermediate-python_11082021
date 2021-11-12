""" Main Test Module """

from unittest import TestSuite, TextTestRunner

from tests.test_sample import TestSample
from tests.simple_rates_client.test_rates_api_server import TestRatesApiServer


def suite() -> TestSuite:
    """ Create Test Suite for Main Test Module """

    test_suite = TestSuite()
    test_suite.addTest(TestSample())
    test_suite.addTest(TestRatesApiServer())
    return test_suite


if __name__ == '__main__':
    runner = TextTestRunner()
    runner.run(suite())
