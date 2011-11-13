import transaction

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Unicode
from sqlalchemy import Boolean

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), unique=True)
    closed = Column(Boolean)

    def __init__(self, name, closed):
        self.name = name
        self.closed = closed

def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    try:
        transaction.begin()
        session = DBSession()
        #task = Task('Start learning Pyramid', 0)
        #session.add(task)
        task = Task('Do quick tutorial', 0)
        session.add(task)
        task = Task('Have some beer!', 0)
        session.add(task)
        transaction.commit()
    except IntegrityError:
        transaction.abort()
