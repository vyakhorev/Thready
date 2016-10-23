import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()  #Magic

class abst_key(object):
    rec_id = sa.Column(sa.Integer, primary_key=True)

    def __repr__(self):
        return self.string_key()

    def __my_key(self):
        return (self.__tablename__, self.rec_id)

    def string_key(self):
        s_r = ""
        for s in self.__my_key():
            s_r += str(s)
        return s_r

    def __eq__(x, y):
        return x.__my_key() == y.__my_key()

    def __hash__(self):
        return hash(self.__my_key())

class cUser(BASE, abst_key):
    __tablename__ = 'users'
    user_name = sa.Unicode(255)
    password = sa.Unicode(255)

class cBlockThread(BASE, abst_key):
    __tablename__ = 'threads'
    blocks = sa.orm.relationship("cBlock", back_populates="thread")

class cBlock(BASE, abst_key):
    __tablename__ = 'blocks'
    discriminator = sa.Column(sa.Unicode(50))
    __mapper_args__ = {'polymorphic_identity': 'Block', 'polymorphic_on': discriminator}
    thread_rec_id = sa.Column(sa.Integer, sa.ForeignKey("threads.rec_id"))
    thread = sa.orm.relationship("cBlockThread", back_populates="blocks")




