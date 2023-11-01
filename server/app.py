from bot import *
import asyncio
from websockets.server import serve, WebSocketServerProtocol
import json
import urllib.parse


async def server(websocket, path: str):

    print('Cliente Conectado', path)
    unquoted = urllib.parse.unquote(path.split('=')[1])
    params = json.loads(unquoted)
    corpus = params["corpus"]
    tolerance = float(params["tolerance"])
    websocket.bot = Bot('Jarbas', True, corpus, 'mongodb://localhost:27017', tolerance)
    async for message in websocket:
        print((f'Mensagem do Client: {message}'))
        response = websocket.bot.getResponse(message)

        await websocket.send(f'{response}')


async def main():
    async with serve(server, "localhost", 5000):
        await asyncio.Future()
asyncio.run(main())
