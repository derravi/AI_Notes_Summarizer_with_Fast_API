from sqlalchemy import Column, Integer, Text, DateTime
from datetime import datetime
from .database import Base


class Summury(Base):
    __tablename__ = "summury"

    id = Column(Integer, primary_key=True, index=True)
    original_text = Column(Text)
    summary_text = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)