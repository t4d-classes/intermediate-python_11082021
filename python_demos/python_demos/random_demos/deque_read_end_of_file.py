""" get last lines of a file """

from collections import deque
from pathlib import Path


def main() -> None:

    fruits_file_path = Path("data", "fruits.txt")

    with open(fruits_file_path, encoding="UTF-8") as fruits_file:
        print(deque(map(lambda x: x.strip(), fruits_file), 5))


if __name__ == "__main__":
    main()
