from bot import getResponse
import asyncio
from websockets.server import serve


async def server(websocket):
    async for message in websocket:
        print((f'Mensagem do Client: {message}'))
        response = getResponse(message)
        
        await websocket.send(f'Resposta do Bot: {response}')


async def main():
    async with serve(server, "localhost", 5000):
        await asyncio.Future()
asyncio.run(main())
