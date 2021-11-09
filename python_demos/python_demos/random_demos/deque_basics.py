""" deque basics """

from collections import deque


def main() -> None:
    """ main """

    fruits = deque(["apple", "orange", "banana"])
    print(fruits)

    fruits.append("lemon")
    print(fruits)

    fruits.appendleft("lime")
    print(fruits)

    last_value = fruits.pop()
    print(last_value)
    print(fruits)

    first_value = fruits.popleft()
    print(first_value)
    print(fruits)


if __name__ == "__main__":
    main()
