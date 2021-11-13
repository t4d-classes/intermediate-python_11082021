""" Test Foods Module """

from unittest import TestCase
from unittest.mock import patch, mock_open
from pathlib import Path

from python_demos.ut_app.foods import load_foods


class TestFoods(TestCase):

    def setUp(self) -> None:
        self.mock_food_data = (
            "FOOD NAME,SCIENTIFIC NAME,GROUP,SUB GROUP\n"
            "Angelica,Angelica keiskei,Herbs and Spices,Herbs\n"
            "Savoy cabbage,Brassica oleracea var. sabauda,Vegetables,Cabbages\n"
            "Silver linden,Tilia argentea,Herbs and Spices,Herbs\n"
            "Kiwi,Actinidia chinensis,Fruits,Tropical fruits\n"
        )
        self.mock_food_open = mock_open(read_data=self.mock_food_data)

    def test_load_foods(self) -> None:
        
        with patch("python_demos.ut_app.foods.open",
            self.mock_food_open) as mock_foods_open:

            foods_file_path = Path("food.csv")

            # act
            foods = load_foods(foods_file_path)

            food = foods[0]
            self.assertEqual(food.common_name, "Angelica")
            self.assertEqual(food.scientific_name, "Angelica keiskei")
            self.assertEqual(food.group, "Herbs and Spices")
            self.assertEqual(food.sub_group, "Herbs")

            mock_foods_open.assert_called_once_with(
                foods_file_path, encoding="UTF-8")


    def tearDown(self) -> None:
        self.mock_food_open = None
        self.mock_food_data = None




