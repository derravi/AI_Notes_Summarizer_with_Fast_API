#It is an DataBase Tool

from sqlalchemy import Column,Integer,String,Text
from Data_Base.database import Base

class Summury(Base):
    __tablename__ = "summaries"

    id = Column(Integer,primary_key=True,index=True)
    original_text = Column(Text)
    summary_text = Column(Text)