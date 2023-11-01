from bot import *
import asyncio
from websockets.server import serve


socketBot = Bot('Jarbas', True, 'vet', 'mongodb://localhost:27017', 0.65)


async def server(websocket):
    async for message in websocket:
        print((f'Mensagem do Client: {message}'))
        response = socketBot.getResponse(message)

        await websocket.send(f'{response}')


async def main():
    async with serve(server, "localhost", 5000):
        await asyncio.Future()
asyncio.run(main())
