import os
from pathlib import Path
import pytest
import sqlalchemy
from testcontainers.community.postgres import PostgresContainer


@pytest.fixture(scope="session")
def postgres_engine():
    project_root = Path(__file__).resolve().parents[4]
    init_script_path = (project_root / "init.sql").as_posix()

    if not os.path.exists(init_script_path):
        raise FileNotFoundError(f"Could not find init.sql at: {init_script_path}")

    db_user = os.getenv("POSTGRES_USER", "postgres")
    db_password = os.getenv("POSTGRES_PASSWORD", "postgres")
    db_name = os.getenv("POSTGRES_DB", "postgres")

    postgres = PostgresContainer(
        "postgres:16-alpine",
        username=db_user,
        password=db_password,
        dbname=db_name,
    )

    postgres.with_volume_mapping(
        init_script_path,
        "/docker-entrypoint-initdb.d/init.sql",
        "ro"
    )

    with postgres:
        engine = sqlalchemy.create_engine(postgres.get_connection_url())
        yield engine
        engine.dispose()

def test_initial_data_loaded(postgres_engine):
    with postgres_engine.connect() as conn:
        result = conn.execute(sqlalchemy.text("SELECT COUNT(*) FROM users")).scalar()
        assert result > 0


