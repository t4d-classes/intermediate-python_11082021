""" map filter reduce demos """

from functools import reduce

# don't do it this way
# do_it = lambda x: x * 2


def double(x: int):
    return x * 2


def my_sum(acc, cur):

    print("acc: ", acc, " cur:", cur)
    return acc + cur


def my_map(fn, items):

    def my_transform(acc, cur):
        acc.append(fn(cur))
        return acc

    return reduce(my_transform, items, [])


def main() -> None:

    nums = [1, 2, 3, 4, 5, 6, 7]

    print(list(my_map(double, nums)))
    # print(list(map(double, nums)))

    # print(list(filter(lambda x: x % 2 == 0, nums)))

    # print(reduce(my_sum, nums, 0))


if __name__ == "__main__":
    main()
