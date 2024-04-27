import psycopg
from testcontainers.postgres import PostgresContainer


def test_with_postgresql_demo() -> None:
    with PostgresContainer("postgres:16", driver=None) as postgres:
        psql_url = postgres.get_connection_url()

        with psycopg.connect(psql_url) as connection:
            with connection.cursor() as cursor:
                (version,) = cursor.execute("SELECT version()").fetchone()

        print(version)
