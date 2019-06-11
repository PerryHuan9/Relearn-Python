import websockets
import asyncio


async def handle(websocket, path):
    receive = await websocket.recv()
    print(receive)
    await websocket.send('埋骨何须桑梓地，人间何处不青山')

start_server = websockets.serve(handle, 'localhost', 8888)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()











