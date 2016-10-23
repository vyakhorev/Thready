import model.base as mb
#import model.blocks.contact
import model.blocks.note

import sqlalchemy as sa

import configparser

cnf = configparser.ConfigParser()
cnf.read('.\__secret\main.ini')
conn_string = cnf.get("DBConnection", "ConnString")

db_conn_str = conn_string
engine = sa.create_engine(db_conn_str, echo=False, encoding='utf-8', pool_recycle=3600)
mb.BASE.metadata.create_all(engine)