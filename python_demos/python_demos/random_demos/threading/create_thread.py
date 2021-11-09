import threading
import multiprocessing as mp
import time


items = ['some stuff']


def do_it() -> None:
    items.append("first stuff")
    print("did it: ", items, id(items), threading.get_ident())


if __name__ == "__main__":

    print("start main: ", threading.get_ident())

    thread1 = threading.Thread(target=do_it)
    thread1.start()

    thread1.join()

    items.append("second stuff")

    print("end main: ", items, id(items), threading.get_ident())
