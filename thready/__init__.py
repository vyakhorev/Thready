from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models.allmodels import DBSession, Base

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.include('.models')
    # how to add routes in a less explicit way?...
    config.add_route('main', '/')
    config.add_route('item_add', '/add')
    config.add_route('item_view', '/id={uid}')
    config.add_route('item_edit', '/id={uid}/edit')
    config.add_static_view('deform_static', 'deform:static/')
    config.scan()
    return config.make_wsgi_app()
