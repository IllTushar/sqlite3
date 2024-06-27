import time
import multiprocessing


def process_1():
    for i in range(10):
        time.sleep(1)
        print(i)


def process_2():
    for i in range(10):
        time.sleep(1.5)
        print(i * i)


if __name__ == '__main__':
    # create process
    p1 = multiprocessing.Process(target=process_1)
    p2 = multiprocessing.Process(target=process_2)

    # Start
    p1.start()
    p2.start()

    p1.join()
    p2.join()
