import pytest
from pyramid.testing import DummyRequest
from pyramid.registry import Registry
from task.views import query_table

@pytest.fixture
def dummy_request(dummy_registry):
    request = DummyRequest()
    request.registry = dummy_registry
    return request

@pytest.fixture
def dummy_registry():
    registry = Registry()
    return registry

def test_query_table_valid_input(dummy_request):
    dummy_request.matchdict = {'table_name': 'Customer', 'field_name': 'Country', 'field_value': 'Brazil'}

    response = query_table(dummy_request)

    assert response['results'] is not None
    assert len(response['results']) > 0

def test_query_table_invalid_table_name(dummy_request):
    dummy_request.matchdict = {'table_name': 'invalid_table', 'field_name': 'Country', 'field_value': 'Brazil'}

    response = query_table(dummy_request)

    assert response.status_code == 400
    assert response.body.decode() == 'Invalid table name'

def test_query_table_exception(dummy_request):
    dummy_request.matchdict = {'table_name': 'Employee', 'field_name': 'invalid_value', 'field_value': 'invalid_value'}

    response = query_table(dummy_request)

    assert response.status_code == 400
    assert response.body.decode() == 'Entity namespace for "Employee" has no property "invalid_value"'