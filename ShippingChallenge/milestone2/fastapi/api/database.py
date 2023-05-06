from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# "sqlite:///./sql_app.db"
url_met_pymysql = "mysql+pymysql://root:wachtwoord@127.0.0.1/milestone"
# test_url = "mariadb+mariadbconnector://root:wachtwoord@127.0.0.1:1234/milestone"
url_met_mariadb = "mariadb+mariadbconnector://root:wachtwoord@mariadb/milestone"

#engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
engine = create_engine(url_met_mariadb)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()