import threading
import time


def apple_1():
    print("苹果1")
    time.sleep(1)


def apple_2():
    print("苹果2")
    time.sleep(1)


def main():
    thread1 = threading.Thread(target=apple_1)
    thread2 = threading.Thread(target=apple_2)
    thread1.start()
    thread2.start()
    print("苹果3")
    print("有多少小丑", threading.active_count())
    print("这些小丑是谁呢", threading.enumerate())


if __name__ == "__main__":
    main()
