import asyncio
import websockets.asyncio.client
from collections.abc import AsyncGenerator

async def main():
    uri = "ws://localhost:8765"
    client: AsyncGenerator = await websockets.asyncio.client.connect(uri)
    try:
        # TODO start
        # 1. Use async for loop to receive numbers from server
        # 2. Send number + 1 back to server in 1 second for 10 times
        # Hint: client is a AsyncGenerator, you can use async for loop to iterate over it
        ...
        # end

    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Connection closed: {e}")

if __name__ == "__main__":
    asyncio.run(main())
