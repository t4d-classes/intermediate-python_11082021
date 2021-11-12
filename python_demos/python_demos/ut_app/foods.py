""" read file """

from collections import namedtuple
from pathlib import Path
import csv
import itertools

Food = namedtuple(
    'Food',
    ['common_name', 'scientific_name', 'group', 'sub_group'])


def load_foods(food_file_path: Path) -> list[Food]:

    with open(food_file_path, encoding="UTF-8") as food_file:
        foods = [
            Food._make(row)
            for row in itertools.islice(csv.reader(food_file), 1, None)]

    return foods