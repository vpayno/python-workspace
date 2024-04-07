"""ASGI Module Server Demo"""

import hashlib
from typing import AsyncGenerator

import uvicorn
from rich import traceback
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import PlainTextResponse
from starlette.routing import Route

traceback.install(show_locals=True)


type stream_t = AsyncGenerator[bytes, None]  # type: ignore[valid-type]


async def online_sha256(stream: stream_t) -> bytes:
    hasher: hashlib._Hash = hashlib.sha256()

    async for chunk in stream:
        print(f"got chunk: {chunk!r}")
        hasher.update(chunk)

    return hasher.digest()


async def compute_sha256(request: Request) -> PlainTextResponse:
    bytes_hash = await online_sha256(request.stream())

    return PlainTextResponse(bytes_hash)


routes = [Route(path="/", endpoint=compute_sha256, methods=["POST"])]


def main() -> None:
    """Main Function"""

    app = Starlette(debug=True, routes=routes)

    uvicorn.run(app, port=5678, log_level="info")


if __name__ == "__main__":  # pragma: no cover
    main()
