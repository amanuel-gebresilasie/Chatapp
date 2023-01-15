import websockets
import asyncio
import ssl
import json


async def main():
    async with websockets.connect(
        ssl=ssl.SSLContext(ssl.PROTOCOL_TLS),
        uri="wss://chatapp-production-ebcf.up.railway.app/",
    ) as c:
        await c.send(json.dumps({"name": "NAME", "_date": "DATE", "msg": "message"}))
        print(await c.recv())
        asyncio.Future()


asyncio.run(main())
