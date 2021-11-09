""" comprehensions demo """

from itertools import islice
from pathlib import Path
from random import randint
import csv


def list_comprehension() -> None:
    """ list comprehension """

    even_nums = [x for x in range(10) if x % 2 == 0]
    print(even_nums)


def dictionary_comprehension() -> None:
    """ dictionary comprehension """

    food_groups = None

    with open(Path("data", "food.csv"), encoding="UTF-8") as food_file:
        food_groups = {
            food[0]: food[2]
            for food in csv.reader(islice(food_file, 1, None))
        }

    print(food_groups)


def set_comprehension() -> None:
    """ set comprehension """

    nums = [randint(0, 9) for _ in range(5)]

    unique_nums = {num for num in nums}

    print(unique_nums)
    print(type(unique_nums))


def generator_comprehension() -> None:

    nums = (x for x in range(10))

    print(type(nums))
    print(list(nums))


def main() -> None:

    # list_comprehension()
    # dictionary_comprehension()
    # set_comprehension()
    generator_comprehension()


if __name__ == "__main__":
    main()
