""" named tuple file load """

from collections import namedtuple
from pathlib import Path
from itertools import islice
import csv


def main() -> None:
    """ main """

    Food = namedtuple(
        "Food",
        ['common_name', 'scientific_name', 'group', 'sub_group'])

    food_file_path = Path("data", "food.csv")

    with open(food_file_path, encoding="UTF-8") as food_file:
        foods = [
            Food._make(row)
            for row in islice(csv.reader(food_file), 1, None)]

    # print(foods[:5])

    # common_name, scientific_name, group, sub_group = foods[10]

    # print(f"Common Name: {common_name}")
    # print(f"Scientific Name: {scientific_name}")
    # print(f"Group: {group}")
    # print(f"Sub Group: {sub_group}")

    print(f"Common Name: {foods[10].common_name}")
    print(f"Scientific Name: {foods[10].scientific_name}")
    print(f"Group: {foods[10].group}")
    print(f"Sub Group: {foods[10].sub_group}")


if __name__ == "__main__":
    main()
