from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class SessionManger(object):

    _engine = None
    _session = None

    @staticmethod
    def session():
        SessionManger.engine()
        if not SessionManger._session:
            Session = sessionmaker()
            Session.configure(bind=SessionManger._engine)
            SessionManger._session = Session()
        return SessionManger._session

    @staticmethod
    def engine():
        if not SessionManger._engine:
            SessionManger._engine = create_engine('sqlite:///foo.db', echo=True)
        return SessionManger._engine

    @staticmethod
    def commit():
        SessionManger.session().commit()
        SessionManger._session = None
