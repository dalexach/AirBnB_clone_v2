#!/usr/bin/python3
"""DB Storage for AirBnb clone"""
import os
import sqlalchemy
from models.base_model import Base
from .model_registry import models_dict
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session


class DBStorage:
    """Class which controls MySQL Storage
    """
    __engine = None
    __session = None

    def __init__(self):
        self.config = {
            'env': os.getenv('HBNB_ENV'),
            'dialect': 'mysql',
            'driver': 'mysqldb',
            'user': os.getenv('HBNB_MYSQL_USER'),
            'pass': os.getenv('HBNB_MYSQL_PWD'),
            'host': os.getenv('HBNB_MYSQL_HOST'),
            'port': 3306,
            'db': os.getenv('HBNB_MYSQL_DB')
        }
        self.__engine = create_engine(
            '{}+{}://{}:{}@{}:{}/{}'.format(
                self.config['dialect'],
                self.config['driver'],
                self.config['user'],
                self.config['pass'],
                self.config['host'],
                self.config['port'],
                self.config['db']
            ), pool_pre_ping=True)

        self.__session = sessionmaker(self.__engine)()

        if self.config['env'] == 'test':
            Base.metadata.drop_all(bind=self.__engine)
            # Base.MetaData(self.__engine).reflect().drop_all()

    def __del__(self):
        self.__session.close()

    def all(self, cls=None):
        """ Get all data from the DB
        """
        resultset = {}

        if cls is None:
            for key, val in models_dict.items():
                query = self.__session.query(val)
                for obj in query:
                    keyname = "{}.{}".format(key, obj.id)
                    resultset[keyname] = obj

        else:
            query = self.__session.query(models_dict[cls])
            for obj in query:
                keyname = "{}.{}".format(cls, obj.id)
                resultset[keyname] = obj

        return resultset

    def new(self, obj):
        """Add new object to the session
        """
        self.__session.add(obj)

    def save(self):
        """Save session to the DB
        """
        try:
            self.__session.commit()
        except Exception:
            self.__session.rollback()

    def delete(self, obj=None):
        """Delete an object from the session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload the session
        """
        # Base.metadata.create_all(self.__engine)
        # self.__session = scoped_session(sessionmaker(
        #     bind=self.__engine,
        #     expire_on_commit=False
        # ))
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expore_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()

    def close(self):
        """
            Calls remove method
        """
        self.__session.close()
