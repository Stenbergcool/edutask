import pytest
from unittest.mock import patch
from pymongo.errors import WriteError
from src.util.dao import DAO


validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["title"],
        "properties": {
            "title": {
                "bsonType": "string",
                "description": "the title of a task must be determined"
            },
        }
    }
}


@pytest.fixture
@patch('src.util.dao.getValidator', autospec=True)
def sut(mockedValidator):
    mockedValidator.return_value = validator
    sut = DAO("test")
    return sut

@pytest.mark.integration
def test_create_valid_data(sut):
    result = sut.create({"title": "testOne", "description": "TestOne"})
    assert isinstance(result, object)
    sut.drop()

@pytest.mark.integration
def test_create_not_valid_data(sut):
    with pytest.raises(WriteError):
        result = sut.create({"title": 142, "description": "TestOne"})
