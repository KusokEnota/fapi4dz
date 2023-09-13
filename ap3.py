import threading
import requests
import time

urls = ['https://img.goodfon.ru/original/1920x1080/e/55/warhammer-40000-horus-heresy-6339.jpg',
        'https://img.goodfon.ru/wallpaper/nbig/0/ec/dospekh-shlem-mech-fantastika-mertvets-tma-deathbringer-king.jpg',
        'https://img.goodfon.ru/wallpaper/nbig/2/6a/graf-vampir-plashch.jpg', ]


def download(url):
    response = requests.get(url)
    filename = 'threding_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.jpg'

    with open('E:\prj' + filename, "wb") as f:
        f.write(response.content)

    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


threads = []
start_time = time.time()
for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()