from pyramid.config import Configurator
from pyramid.request import Request
from sqlalchemy import engine_from_config
from .models import Base

def main(global_config, **settings):
    config = Configurator(settings=settings)
    engine = engine_from_config(settings, 'sqlalchemy.')
    Base.metadata.bind = engine
    config.include('pyramid_mako')
    
    config.add_route('query_table', '/db/Chinook/{table_name}/{field_name}/{field_value}.html')
    config.scan('.views')
    return config.make_wsgi_app()