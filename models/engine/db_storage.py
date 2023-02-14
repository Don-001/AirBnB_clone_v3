# models/engine/db_storage.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("sqlite:///hbnb.db")

    def all(self):
        return self.__session.query(Base).all()

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def remove(self):
        self.__session.close()

    def close(self):
        self.remove()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
        
    def get(self, cls, id):
    """Retrieve an object from the database by its ID"""
    if cls and id:
        return self.__session.query(cls).get(id)
    return None

    def count(self, cls=None):
    """Count the number of objects in the database"""
    if cls:
        return self.__session.query(cls).count()
    else:
        return sum(self.__session.query(cls).count() for cls in self.__classes.values())

