import time
import threading

counter1 = 2
counter2 = 4

counter1_lock = threading.Lock()
counter2_lock = threading.Lock()


def task1() -> None:

    global counter1
    global counter2

    with counter1_lock:
        time.sleep(1)
        with counter2_lock:
            x = counter1
            y = counter2
            x = x - 1
            y = y - 1
            counter1 = x
            counter2 = y


def task2() -> None:

    global counter1
    global counter2

    with counter2_lock:
        time.sleep(1)
        with counter1_lock:
            x = counter1
            y = counter2
            x = x - 1
            y = y - 1
            counter1 = x
            counter2 = y


print(f"start counter1: {counter1}")
print(f"start counter2: {counter2}")

thread1 = threading.Thread(target=task1)
thread1.start()

thread2 = threading.Thread(target=task2)
thread2.start()

thread1.join()
thread2.join()

print(f"end counter1: {counter1}")
print(f"end counter2: {counter2}")
