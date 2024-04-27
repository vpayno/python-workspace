"""Unmocked MongoDB Tests"""

import importlib.util
from typing import Any

import pytest

# MONGO_VER: str = "3.6.23"
MONGO_VER: str = "4.0.10"

found_tcm = importlib.util.find_spec("testcontainers")
if found_tcm is not None:
    from pymongo import MongoClient
    from testcontainers.core import waiting_utils  # type: ignore[import-untyped]
    from testcontainers.mongodb import MongoDbContainer  # type: ignore[import-untyped]

    mongodb = MongoDbContainer(f"mongo:{MONGO_VER}")

    @pytest.fixture(scope="module", autouse=True)
    def setup(request: Any) -> None:
        def cleanup() -> None:
            mongodb.stop()

        print("Starting container...")
        mongodb.start()
        print("Started container.")

        print("Waiting on log...")
        waiting_utils.wait_for_logs(mongodb, "waiting for connections on port 27017")
        print("Waited on log.")

        request.addfinalizer(cleanup)

    @pytest.mark.skipif(True, reason="can't get mongodb containers to work")
    @pytest.mark.skipif(found_tcm is None, reason="testcontainer module not installed")
    def test_mongo_testcontainer_demo() -> None:
        """This function demonstrates how to use testcontainer to start a mongodb container and how to connect to it."""
        mongodb_url: str = mongodb.get_connection_url()
        print(f"Got connection url: {mongodb_url}")

        mongodb_client = mongodb.get_connection_client()
        print(f"Got connection client: {mongodb_client}")

        client: MongoClient = MongoClient(mongodb_url)
        print(f"Got mongodb client: {client}")

        assert client.is_primary
        print(f"{client.list_databases()}")
