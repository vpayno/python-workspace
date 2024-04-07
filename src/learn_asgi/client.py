"""ASGI Module Client Demo"""

import asyncio
import hashlib

import httpx
from rich import traceback

traceback.install(show_locals=True)


async def fake_file_data():
    yield b"Hello "
    await asyncio.sleep(0.1)
    yield b"world!"
    yield b""  # EOF


async def main():
    """Main Function"""

    async with httpx.AsyncClient() as client:
        response = await client.post(
            url="http://localhost:5678/",
            data=fake_file_data(),
        )
        data = response.read()

        print(f"Got resonse: {data.hex()}")
        print(f"   Expected: {hashlib.sha256(b'Hello world!').hexdigest()}")


if __name__ == "__main__":  # pragma: no cover
    asyncio.run(main())
