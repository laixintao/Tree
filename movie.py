#_*_ coding: utf-8 _*_
__author__ = 'laixintao'


from sqlalchemy import Column,String,create_engine,Integer,Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movie'

    id = Column(Integer,primary_key=True)
    sent_ch = Column(String(200))
    sent_en = Column(String(200))
    pic = Column(String(200))
    url = Column(String(300))
    movie = Column(String(100))
    ispublic = Column(Boolean)

    def __repr__(self):
        return "<Movie(%s,%s,%s)>" % (
            self.movie,self.sent_ch,self.sent_en
        )


engine = create_engine("sqlite:///movie.db")
DBSession = sessionmaker(bind=engine)

def create_table():
    Base.metadata.create_all(engine)