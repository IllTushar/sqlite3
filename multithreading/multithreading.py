import threading
import time


def print_number():
    for i in range(5):
        time.sleep(2)
        print("Number", i)


def print_letter():
    for letter in 'abcde':
        time.sleep(2)
        print("Letter", letter)


if __name__ == '__main__':
    # Create thread
    t1 = threading.Thread(target=print_number)
    t2 = threading.Thread(target=print_letter)
    start = time.time()
    # thread start
    t1.start()
    t2.start()

    # join the thread make a main thread after excustion
    t1.join()
    t2.join()
    finish = time.time() - start
    print("Finish time", finish)

