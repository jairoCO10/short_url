from sqlalchemy import Column, String
from app.database import Connection

class URL(Connection.Base):
    __tablename__ = "urls"
    short_url = Column(String, primary_key=True, index=True)
    original_url = Column(String, index=True)
    ip =Column()

