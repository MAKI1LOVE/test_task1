import aiohttp

http_session: aiohttp.ClientSession = None


async def init_http_session():
    global http_session
    http_session = aiohttp.ClientSession()


def get_http_session():
    return http_session


async def http_session_close():
    await http_session.close()
