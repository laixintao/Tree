#_*_ coding: utf-8 _*_
__author__ = 'laixintao'


from sqlalchemy import Column,String,create_engine,Integer,Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

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
    ispublish = Column(Boolean,default=False)
    couldPublish = Column(Boolean,default=False)
    checked = Column(Boolean,default=False)

    def __repr__(self):
        return "<Movie(%s,%s,%s,%s)>" % (
            self.movie,self.url,self.sent_ch,self.sent_en
        )

    def print_info(self):
        print self.id
        print self.movie
        print self.url
        print self.sent_ch
        print self.sent_en
        print self.pic_localname
        print "ispublish?",self.ispublish," couldpublish?",self.couldPublish," checked?",self.checked

engine = create_engine("sqlite:///movie.db")
DBSession = sessionmaker(bind=engine)

def create_table():
    Base.metadata.create_all(engine)

def list_movie():
    session = DBSession()
    movies = session.query(Movie)
    for m in movies:
        print ""
        print "-"*30
        m.print_info()
    session.close()

def list_moive_could_public():
    session = DBSession()
    movies = session.query(Movie).filter(Movie.couldPublish==True)
    for m in movies:
        print ""
        print "-"*30
        m.print_info()
    session.close()
def list_moive_could_not_public():
    session = DBSession()
    movies = session.query(Movie).filter(Movie.couldPublish==False)
    for m in movies:
        print ""
        print "-"*30
        m.print_info()
    session.close()

def movie_check():
    session = DBSession()
    while True:
        movie = session.query(Movie).filter(Movie.checked==False).first()
        if movie != None:
            print ""
            print "-"*30
            movie.print_info()
            could_publish = int(raw_input("1 for True; 2 for False; 3 for next;"))
            if could_publish == 1:
                movie.couldPublish = True
                movie.checked = True
                session.add(movie)
            elif could_publish == 2:
                movie.couldPublish = False
                movie.checked = True
                session.add(movie)
            else:
                pass
            # session.commit()
        else:
            break
    session.commit()
    session.close()

def movie_without_pic():
    session = DBSession()
    tobe_download = []
    movies = session.query(Movie).filter(Movie.couldPublish==True)
    for m in movies:
        pic_path = m.pic_localname
        if not os.path.exists(pic_path):
            tmp = (m.pic_localname,m.pic_url)
            tobe_download.append(tmp)
    return tobe_download


if __name__ == "__main__":
    action = int(raw_input("What you want to do ?\n"
                           "1 for list all movies;\n"
                           "2 for list the movies could publish;\n"
                           "3 for list the uncheck movies and give a check;\n"
                           "4 for list movie without pic;\n"
                           "5 for list the movies could NOT publish;\n"))
    if action == 1:
        list_movie()
    elif action == 2:
        list_moive_could_public()
    elif action == 3:
        movie_check()
    elif action == 4:
        movie_without_pic()
    elif action == 5:
        list_moive_could_not_public()