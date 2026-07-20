import os
from urllib.parse import quote_plus

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT", "4000")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

required_variables = {
    "MYSQL_USER": MYSQL_USER,
    "MYSQL_PASSWORD": MYSQL_PASSWORD,
    "MYSQL_HOST": MYSQL_HOST,
    "MYSQL_DATABASE": MYSQL_DATABASE,
}

missing_variables = [
    name for name, value in required_variables.items() if not value
]

if missing_variables:
    raise ValueError(
        f"Missing database environment variables: "
        f"{', '.join(missing_variables)}"
    )

# Safely handle special characters such as @, #, / and : in the password.
encoded_user = quote_plus(MYSQL_USER)
encoded_password = quote_plus(MYSQL_PASSWORD)

DATABASE_URL = (
    f"mysql+pymysql://{encoded_user}:{encoded_password}"
    f"@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=300,
    connect_args={
        "ssl": {}
    }
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def test_database_connection():
    try:
        with engine.connect() as connection:
            database_name = connection.execute(
                text("SELECT DATABASE()")
            ).scalar()

            print("TiDB connection successful")
            print(f"Connected database: {database_name}")

    except Exception as error:
        print("TiDB connection failed")
        print(error)


if __name__ == "__main__":
    test_database_connection()