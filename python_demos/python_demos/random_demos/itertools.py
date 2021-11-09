""" basics of itertools """

from collections import namedtuple
from itertools import chain, islice, groupby
from pathlib import Path
import csv


Food = namedtuple(
    "Food",
    ['common_name', 'scientific_name', 'group', 'sub_group'])


def main() -> None:

    # print(("ABC",))

    # print(list(chain("ABC", "DEF")))
    # print(list(chain(range(0, 11), range(90, 101))))

    food_file_path = Path("data", "food.csv")

    with open(food_file_path, encoding="UTF-8") as food_file:
        for food_group, foods in groupby(
                map(Food._make, csv.reader(islice(food_file, 1, None))),
                lambda f: f.group):

            print(f"Group: {food_group}")

            for food in foods:
                print(f"  {food.common_name}")


if __name__ == "__main__":
    main()
