from bot import *
import asyncio
from websockets.server import serve, WebSocketServerProtocol
import json
import urllib.parse


async def onConnect(websocket, path: str):

    print('Cliente Conectado', path)
    unquoted = urllib.parse.unquote(path.split('=')[1])
    params = json.loads(unquoted)
    corpus = params["corpus"]
    botName = params["botName"]
    tolerance = float(params["tolerance"])
    websocket.bot = Bot(botName, True, corpus, 'mongodb://localhost:27017', tolerance)
    print((f'=========== Bot Inicializado: {botName} ================'))
    async for message in websocket:
        response = websocket.bot.getResponse(message)

        await websocket.send(f'{response}')


async def main():
    async with serve(onConnect, "localhost", 5000):
        print((f'=========== Websocket inicializado na porta 5000 ================'))
        await asyncio.Future()
asyncio.run(main())
