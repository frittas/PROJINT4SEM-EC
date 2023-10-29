from bot.bot import getResponse
import asyncio
from websockets.server import serve


async def server(websocket):
    async for message in websocket:
        # await websocket.send(f'A mensagem recebida foi: {message}')
        print (message)
        response = getResponse(message)
        await websocket.send(f'Resposta do Bot: {response}')


async def main():
    async with serve(server, "localhost", 5000):
        await asyncio.Future()  # run forever

asyncio.run(main())

