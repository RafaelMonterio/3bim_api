# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Formato: mysql+pymysql://usuario:senha@host/nome_do_banco
DATABASE_URL = 'mysql+pymysql://root:@localhost/loja'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
<<<<<<< HEAD
Base = declarative_base() 

=======
Base = declarative_base()
>>>>>>> 14d06886dc54d91a5e1442d089da045973f50cfe
# Função de dependência: abre uma sessão por requisição e garante o fechamento
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()