import threading
from bs4 import BeautifulSoup
import requests


def fetch_all_content(urls):
    response = requests.get(urls)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'text length -> {len(soup.text)} urls -> {urls}')


if __name__ == '__main__':
    urls = ['https://en.wikipedia.org/wiki/Elon_Musk', 'https://en.wikipedia.org/wiki/Donald_Trump',
            'https://en.wikipedia.org/wiki/Python_(programming_language)'
            ]
    thread = []
    for url in urls:
        t1 = threading.Thread(target=fetch_all_content, args=(url,))
        t1.start()
        thread.append(t1)

    for thread_join in thread:
        thread_join.join()

    print(f"Fetch all {len(thread)}")
