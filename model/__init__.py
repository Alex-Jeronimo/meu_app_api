from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from model.base import BaseModelo
from model.atividade import Atividade


PASTA_BANCO = Path("database")
PASTA_BANCO.mkdir(exist_ok=True)

URL_BANCO = f"sqlite:///{PASTA_BANCO.as_posix()}/db.sqlite3"
motor = create_engine(URL_BANCO, echo=False)
Sessao = sessionmaker(bind=motor)

if not database_exists(motor.url):
    create_database(motor.url)

BaseModelo.metadata.create_all(motor)
