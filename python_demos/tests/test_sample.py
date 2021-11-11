""" Test Sample Module """

from unittest import TestCase, main

from python_demos.some_pkg.some_mod import do_it


class TestSample(TestCase):
    """ Test Sample Class """

    def test_sample(self) -> None:
        """ Sample Test """

        # arrange

        # setup input variables, stuff like that

        # act

        result = do_it()

        # assert

        self.assertEqual(result, True)

    def test_sample2(self) -> None:
        """ Sample Test """

        # arrange

        # setup input variables, stuff like that

        # act

        result = do_it()

        # assert

        self.assertEqual(result, True)


if __name__ == "__main__":
    main()
