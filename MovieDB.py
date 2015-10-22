#_*_ coding: utf-8 _*_
__author__ = 'laixintao'


from sqlalchemy import Column,String,create_engine,Integer,Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movie'

    id = Column(Integer,primary_key=True)
    post_title = Column(String(200))
    sent_ch = Column(String(200))
    sent_en = Column(String(200))
    pic_url = Column(String(200))
    pic_localname = Column(String(200))
    url = Column(String(300))
    movie = Column(String(100))
    ispublic = Column(Boolean,default=False)
    couldPublic = Column(Boolean,default=True)

    def __repr__(self):
        return "<Movie(%s,%s,%s,%s)>" % (
            self.movie,self.url,self.sent_ch,self.sent_en
        )

    def print_info(self):
        print self.movie
        print self.url
        print self.sent_ch
        print self.sent_en
        print self.pic_localname

engine = create_engine("sqlite:///movie.db")
DBSession = sessionmaker(bind=engine)

def create_table():
    Base.metadata.create_all(engine)

def list_movie():
    session = DBSession()
    movies = session.query(Movie)
    for m in movies:
        m.print_info()
    session.close()

if __name__ == "__main__":
    list_movie()
