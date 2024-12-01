from sqlalchemy.orm import sessionmaker
from app.db.setup import engine


Session = sessionmaker(bind=engine)
