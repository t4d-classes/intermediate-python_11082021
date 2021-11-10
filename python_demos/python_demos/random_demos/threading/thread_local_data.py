
import time
import threading


mydata = threading.local()


def do_it2() -> None:

    time.sleep(0.5)
    print("do_it2: ", mydata.msg, ", thread id: ", threading.get_ident())


def do_it(msg: str) -> None:

    time.sleep(0.5)
    mydata.msg = msg

    print("do_it: ", mydata.msg, ", thread id: ", threading.get_ident())

    do_it2()


thread1 = threading.Thread(target=do_it, args=('thread1',))
thread1.start()

thread2 = threading.Thread(target=do_it, args=('thread2',))
thread2.start()

thread1.join()
thread2.join()
