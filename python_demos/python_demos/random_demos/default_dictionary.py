""" default dictionary demo """


from collections import defaultdict


def default_quantity() -> int:
    """ default quanity """
    return 0


def main() -> None:
    """ main """

    fruits = defaultdict(default_quantity)
    # fruits = {}

    fruits["apple"] = 23
    fruits["orange"] = 12

    print(fruits["apple"])
    print(fruits["banana"])
    # print(fruits.get("banana", 0))


if __name__ == "__main__":
    main()
