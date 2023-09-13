from multiprocessing import Process
import requests
import time

urls = ['https://img.goodfon.ru/original/1920x1080/e/55/warhammer-40000-horus-heresy-6339.jpg',
        'https://img.goodfon.ru/wallpaper/nbig/0/ec/dospekh-shlem-mech-fantastika-mertvets-tma-deathbringer-king.jpg',
        'https://img.goodfon.ru/wallpaper/nbig/2/6a/graf-vampir-plashch.jpg', ]


def download(url):
    response = requests.get(url)
    filename = 'multiprocessing_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.jpg'
    with open('E:\prj' + filename, "wb") as f:
        f.write(response.content)
        print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


processes = []
start_time = time.time()

if __name__ == '__main__':
    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()