from pyramid.view import view_config
from pyramid.response import Response
from task.models import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///chinook.db')
Session = sessionmaker(bind=engine)

@view_config(route_name='query_table', renderer='task:templates/index.mako')
def query_table(request):
    try:
        table_name = request.matchdict['table_name']
        field_name = request.matchdict['field_name']
        field_value = request.matchdict['field_value']
        session = Session()

        # Filter and get the table
        model_class = next((cls for cls in Base.registry._class_registry.values() if getattr(cls, '__tablename__', None) == table_name), None)
        if not model_class:
            return Response(status=400, body='Invalid table name')

        # Create a dynamic filter
        filter_criteria = {field_name: field_value}

        # Query the table
        results = session.query(model_class).filter_by(**filter_criteria).all()
            
        session.close()

        return {'results': results}
    except Exception as e:
        return Response(status=400, body=str(e))