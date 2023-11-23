from bot import Bot
import asyncio
from websockets.server import serve
import json
import urllib.parse


async def onConnect(websocket, path: str):

    print('Cliente Conectado', path)

    # Extração dos parametros do Path
    unquoted = urllib.parse.unquote(path.split('=')[1])
    params = json.loads(unquoted)
    corpus = params["corpus"]
    botName = params["botName"]
    tolerance = float(params["tolerance"])
    train = bool(params["train"])

    # Instanciando o Bot
    websocket.bot = Bot(botName, train, corpus,
                        'mongodb://localhost:27017', tolerance)

    print((f'=========== Bot Inicializado: {botName} ================'))
    async for message in websocket:

        # obtendo a melhor resposta do BOT
        response = websocket.bot.getResponse(message)

        # enviando a resposta de volta para o cliente conectado
        await websocket.send(f'{response}')


async def main():
    # Definindo o servidor Websocket na porta 5000
    async with serve(onConnect, "localhost", 5000):
        print((f'=========== Websocket inicializado na porta 5000 ================'))
        await asyncio.Future()
asyncio.run(main())
