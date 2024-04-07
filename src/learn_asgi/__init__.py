"""
server module initialization

set up for module execution
"""

from learn_asgi.client import main as client
from learn_asgi.server import main as server

__all__ = ["server", "client"]
