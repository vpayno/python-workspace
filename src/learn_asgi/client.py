"""ASGI Module Client Demo"""

import asyncio
import hashlib
import time
from typing import Any, Awaitable, Iterable, Self

import httpx
from rich import traceback

traceback.install(show_locals=True)


class AwaitRateLimited:
    def __init__(self, awaitables: Iterable[Awaitable], rate: float):
        self.awaitables = iter(awaitables)
        self.max_sleep_duration = 1 / rate
        self.last_iter_at: float | None = None

    def __aiter__(self) -> Self:
        return self

    async def wait_if_needed(self) -> None:
        if self.last_iter_at is None:
            return

        now = time.perf_counter()
        elapsed = now - self.last_iter_at

        await asyncio.sleep(max(0.0, self.max_sleep_duration - elapsed))

    async def __anext__(self) -> Any:
        await self.wait_if_needed()

        self.last_iter_at = time.perf_counter()

        try:
            awaitable = next(self.awaitables)
        except StopIteration:
            raise StopAsyncIteration
        return await awaitable


async def fake_file_data():
    yield b"Hello "
    await asyncio.sleep(0.1)
    yield b"world!"
    yield b""  # EOF


async def use_api(x: int):
    await asyncio.sleep(0.1)
    return 2 * x


async def await_rate_limited(awaitables, rate: float):
    max_sleep_duration = 1 / rate

    for aw in awaitables:
        start = time.perf_counter()
        yield await aw
        elapsed = time.perf_counter() - start
        await asyncio.sleep(max(0.0, max_sleep_duration - elapsed))


async def main():
    """Main Function"""

    print("\n")
    print("Example 1 server/client")
    print("\n")

    async with httpx.AsyncClient() as client:
        response = await client.post(
            url="http://localhost:5678/",
            data=fake_file_data(),
        )
        data = response.read()

        print(f"Got resonse: {data.hex()}")
        print(f"   Expected: {hashlib.sha256(b'Hello world!').hexdigest()}")

    print("\n")
    print("Example 2 await for loop without rate-limiting")
    print("\n")

    awaitables = (use_api(x) for x in range(10))
    start = time.perf_counter()

    for awaitable in awaitables:
        result = await awaitable
        elapsed = time.perf_counter() - start
        print(f"[{elapsed:.2f}s] Got result: {result}")

    print("\n")
    print("Example 3 await for loop with rate-limiting")
    print("\n")

    awaitables = (use_api(x) for x in range(10))
    start = time.perf_counter()

    async for result in await_rate_limited(awaitables, rate=5.0):
        elapsed = time.perf_counter() - start
        print(f"[{elapsed:.2f}s] Got result: {result}")

    print("\n")
    print("Example 4 await for loop iterable with rate-limiting")
    print("\n")

    awaitables = (use_api(x) for x in range(10))
    start = time.perf_counter()

    async for result in AwaitRateLimited(awaitables, rate=5.0):
        elapsed = time.perf_counter() - start
        print(f"[{elapsed:.2f}s] Got result: {result}")


if __name__ == "__main__":  # pragma: no cover
    asyncio.run(main())
