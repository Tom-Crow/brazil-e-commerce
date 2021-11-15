import os

import dotenv
from sqlalchemy import create_engine


def create_sql_alchemy_db_engine(db_name: str = "brazil"):
    """
    Requires correctly configured .env file
    """
    dotenv.load_dotenv()

    db_user = os.environ[f"POSTGRES_USER"]
    db_password = os.environ[f"POSTGRES_PASSWORD"]
    db_port = os.environ[f"POSTGRES_PORT"]

    return create_engine(
        f'postgresql://{db_user}:{db_password}@localhost:{db_port}/{db_name}'
    )
