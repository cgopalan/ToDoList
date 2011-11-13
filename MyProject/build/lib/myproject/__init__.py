from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from sqlalchemy import engine_from_config

from myproject.models import initialize_sql

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
    config = Configurator(settings=settings, session_factory=session_factory)
    config.add_static_view('static', 'myproject:static', cache_max_age=3600)
    config.add_route('list', '/')
    config.add_route('new', '/new')
    config.add_route('close', '/close/{id}')
    config.add_view('myproject.views.list_view',
                    route_name='list',
                    renderer='list.mako')
    config.add_view('myproject.views.new_view',
                    route_name='new',
                    renderer='new.mako')
    config.add_view('myproject.views.close_view',
                    route_name='close',
                    renderer='list.mako')
    return config.make_wsgi_app()

