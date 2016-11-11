# start server with Shift+F10
# drop this out if one day it is deployed
# TODO: add tests

import sqlalchemy as sa
import configparser
# These are WSGI things
# http://pythonpaste.org/deploy/module-paste.deploy.interfaces.html
from pyramid.paster import get_app, setup_logging
# https://docs.python.org/3.5/library/wsgiref.html
from wsgiref.simple_server import make_server, WSGIRequestHandler

pathtoini = "development.ini"
doalchemyecho = True
serverport = 6543
serverip = '127.0.0.1'

if __name__ == "__main__":
    # create / update schema (this is instead of initialize_db script)
    print('*'*10)
    print('Starting SQL Alchemy')
    print('*'*10)
    cnf = configparser.ConfigParser()
    cnf.read(pathtoini)
    connstr = cnf.get("app:main", "sqlalchemy.url")
    engine = sa.create_engine(connstr, echo=doalchemyecho, pool_recycle=3600)

    # TODO: find an elegant way to initialize all the Base inheritors
    from thready.models.allmodels import Base
    Base.metadata.create_all(engine)

    # start server
    # TODO: interactive break / better logging / WSGI undestanding and validation
    print('*' * 10)
    print('Starting server at %s : %d'%(serverip, serverport))
    print('*' * 10)
    setup_logging(pathtoini)
    # This would magically call main from thready.__init__.py
    # (one have to run "VENV/Scripts pip install -e ." to make this magic work.
    application = get_app(pathtoini, 'main') # https://github.com/Pylons/pyramid/blob/master/pyramid/router.py
    # There is a way to hack into WSGI protocol - testing purposes
    # http://www.programcreek.com/python/example/53274/wsgiref.simple_server.WSGIRequestHandler
    server = make_server(serverip, serverport, application)
    server.serve_forever()
    # pserve is a bit more complicated thing:
    # https://github.com/Pylons/pyramid/blob/master/pyramid/scripts/pserve.py




