import asyncio
import aiohttp


async def download_image(url: str, files: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                with open(files, 'wb') as f:
                    f.write(await response.read())
                print(f"Изображение сохранено как {files}")
            else:
                print(f"Ошибка при загрузке изображения с {url}")


async def main():
    image_paths = [
        'https://34travel.me/media/upload/images/2019/june/national-geographic/6.jpg',
        'https://34travel.me/media/upload/images/2019/june/national-geographic/1.jpg',
        'https://34travel.me/media/upload/images/2019/june/national-geographic/8.jpg'
    ]

    tasks = []
    for i, url in enumerate(image_paths):
        filename = f"image{i + 1}.jpg"
        tasks.append(download_image(url, filename))

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
