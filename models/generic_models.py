from sqlalchemy import Sequence, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from orm.utils import SessionManger

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String)
    name = Column(String)
    email = Column(String)
    country = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(username='%s', name='%s', email='%s', country='%s', password='%s')>" % (
            self.username, self.name, self.email, self.country, self.password)


engine = SessionManger.engine()
Base.metadata.create_all(engine)
