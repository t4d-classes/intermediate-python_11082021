""" named tuple """

from collections import namedtuple


def main() -> None:
    """ main """

    # p1 = (2, 6, 4)
    # print(p1)
    # print(type(p1))

    Point = namedtuple("Point", ["x", "y", "z"])

    p = Point(2, 6, 4)
    print(p)
    print(type(p))

    x, y, z = p

    print(x, y, z)

    print(p.x, p.y, p.z)


if __name__ == "__main__":
    main()
