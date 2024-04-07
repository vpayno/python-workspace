"""
server module initialization

set up for module execution
"""

import learn_asgi.client
from learn_asgi.server import main as server

__all__ = ["server", "client"]
