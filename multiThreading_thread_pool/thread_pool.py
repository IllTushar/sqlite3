from concurrent.futures import ThreadPoolExecutor
import time


def square(number):
    time.sleep(1)
    return number


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=7) as executor:
        results = executor.map(square, numbers)

        for digit in results:
            print(digit)
