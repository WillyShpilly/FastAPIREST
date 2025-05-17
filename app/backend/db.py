from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker  # New


engine = create_engine('sqlite:///ecommerce.db', echo=True)
SessionLocal = sessionmaker(bind=engine)  # New