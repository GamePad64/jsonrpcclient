import aiohttp
import asyncio
from jsonrpcclient.aiohttp_client import AioHTTPClient

async def main(loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        client = AiohttpClient(session, 'http://localhost:5000/')
        response = await client.request('ping')
        print(response)

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
