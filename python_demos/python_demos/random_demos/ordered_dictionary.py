""" ordered dictionary """


from collections import OrderedDict


def main() -> None:
    """ main """

    fruits = OrderedDict({
        "apple": 10,
        "orange": 15,
        "banana": 4
    })

    print(fruits.keys())

    fruits.move_to_end("apple")

    print(fruits.keys())

    fruits["lemon"] = 34
    print(fruits.keys())

    print(fruits.popitem())
    print(fruits.keys())

    print(fruits.popitem(False))
    print(fruits.keys())


if __name__ == "__main__":
    main()
