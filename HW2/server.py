import asyncio
import random

import websockets.asyncio.server as wsserver

async def send_number(websocket: wsserver.ServerConnection):
    for _ in range(10):
        n = random.randint(0, 255)
        await websocket.send(str(n))
        print(f"Sent number {n}")
        try:
            n_recv = await asyncio.wait_for(websocket.recv(), 1)
            if int(n_recv) != n + 1:
                print(f"Expected {n + 1}, but got {n_recv}")
                await websocket.close(code=1002, reason=f"Expected {n + 1}, but got {n_recv}")
                return
        except asyncio.TimeoutError:
            await websocket.close(code=1002, reason="You are too slow!")
        await asyncio.sleep(1)
    await websocket.close(reason="You passed!")

async def main():
    server = await wsserver.serve(send_number, "localhost", 8765)
    print("Number server listening on port 8765")
    return await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())