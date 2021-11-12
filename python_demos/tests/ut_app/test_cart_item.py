

from unittest import TestCase

from python_demos.ut_app.cart_item import (
    CartItem, PriceLessThanZeroError, NameEmptyError)


class TestCartItemErrors(TestCase):

    def test_cart_item_price_err(self) -> None:

        with self.assertRaises(PriceLessThanZeroError):
            CartItem("apples", -1, 5)
