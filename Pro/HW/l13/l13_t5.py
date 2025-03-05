import asyncio
from aiohttp import web
from aiohttp.web import Request, Response
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(), logging.FileHandler('site_requests.log')]
)


async def hello(request: Request) -> Response:
    """
    Обработчик для главной страницы
    :param request:
    :return:
    """
    return web.Response(text="Hello, World!")


async def slow(request: Request) -> Response:
    """
    Обработчик для /slow с задержкой
    :param request:
    :return:
    """
    await asyncio.sleep(5)
    return web.Response(text="Operation completed")

app = web.Application()
app.router.add_get('/', hello)
app.router.add_get('/slow', slow)


if __name__ == '__main__':
    web.run_app(app, host='localhost', port=8080)
