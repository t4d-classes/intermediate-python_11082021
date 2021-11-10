import threading
import multiprocessing as mp
import time


items = ['some stuff']


def do_it(items) -> None:
    items.append("first stuff")
    # items = ['new list']
    print("did it: ", items, id(items), threading.get_ident())


if __name__ == "__main__":

    print("start main: ", threading.get_ident())

    # do_it(items)

    thread1 = mp.Process(target=do_it, args=(items,))
    thread1.start()

    thread1.join()

    items.append("second stuff")

    print("end main: ", items, id(items), threading.get_ident())
