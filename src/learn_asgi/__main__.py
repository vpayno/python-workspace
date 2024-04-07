"""
learn_asgi module execution

Entrypoint when running module: python -m learn_asgi
"""

from learn_asgi import server

if __name__ == "__main__":  # pragma: no cover
    server()
