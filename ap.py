import asyncio
import aiohttp
import time

urls = ['https://img.goodfon.ru/original/1920x1080/e/55/warhammer-40000-horus-heresy-6339.jpg',
        'https://img.goodfon.ru/wallpaper/nbig/0/ec/dospekh-shlem-mech-fantastika-mertvets-tma-deathbringer-king.jpg',
        'https://img.goodfon.ru/wallpaper/nbig/2/6a/graf-vampir-plashch.jpg', ]


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            filename = 'asyncio_' + url.replace('https://', '').replace('.jpg', '').replace('.', '_').replace('/',
                                                                                                              '') + '.jpg'

            with open('E:\prj/' + filename, "wb") as f:
                total, size = (0, 4092)
                res = response.content.iter_chunked(size)
                async for chunk in res:
                    f.write(chunk)
                    total += size
                    print(f"Downloaded {url}: {total / 1024:.2f} kB in {time.time() - start_time:.2f} seconds")


async def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
        await asyncio.gather(*tasks)


start_time = time.time()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())