"""
learn_asgi module execution
"""

from learn_asgi import client, server

if __name__ == "__client__":  # pragma: no cover
    client.main()

if __name__ == "__main__":  # pragma: no cover
    server()
