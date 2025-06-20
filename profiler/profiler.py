"""
Time the queries in the queries directory.
"""

import pathlib

import db_query_profiler
import duckdb

HERE = pathlib.Path(__file__).parent


def main() -> None:
    """
    Time the queries in the queries directory.
    """

    db_connection = duckdb.connect(
        database=str(HERE.parent / "billiam_database" / "billiam.duckdb"),
        read_only=True,
    )
    db_query_profiler.time_queries(
        conn=db_connection,
        repeat=1_000,
        directory=HERE / "queries"
    )


if __name__ == "__main__":
    main()
