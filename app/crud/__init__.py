from sqlalchemy.orm import sessionmaker
from db.setup import engine


Session = sessionmaker(bind=engine)
