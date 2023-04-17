import pytest
import unittest.mock as mock
from src.controllers.usercontroller import UserController

"""Email exists, email valid and email not unique"""
def test_valid_email_exist_not_unique():
    mockedDao = mock.MagicMock()
    mockedDao.find.return_value = [{'Email': 'hello@gmail.com'}, {'Email': 'hello@gmail.com'}]
    user_controller = UserController(mockedDao)
    result = user_controller.get_user_by_email('hello@gmail.com')
    assert result == {'Email': 'hello@gmail.com'}

"""Email exists, email not valid and email unique"""
def test_not_valid_exist_unique():
    with pytest.raises(ValueError, match='Error: invalid email address'):
        mockedDao = mock.MagicMock()
        mockedDao.find.return_value = [{'Email': 'hello'}]
        user_controller = UserController(mockedDao)
        user_controller.get_user_by_email('hello')

"""Email exists, email valid and email unique"""
def test_valid_exist_unique():
    mockedDao = mock.MagicMock()
    mockedDao.find.return_value = [{'Email': 'hello@gmail.com'}]
    user_controller = UserController(mockedDao)
    result = user_controller.get_user_by_email('hello@gmail.com')
    assert result == {'Email': 'hello@gmail.com'}

"""Email exists, email not valid and email not unique"""
def test_not_valid_exist_not_unique():
    with pytest.raises(ValueError, match='Error: invalid email address'):
        mockedDao = mock.MagicMock()
        mockedDao.find.return_value = [{'Email': 'hello'}]
        user_controller = UserController(mockedDao)
        user_controller.get_user_by_email('hello')

"""Email does not exists, email valid and email unique"""
def test_valid_email_does_not_exist_unique():
    mockedDao = mock.MagicMock()
    mockedDao.find.return_value = None
    user_controller = UserController(mockedDao)
    result = user_controller.get_user_by_email("hello@gmail.com")
    assert result == None

"""Email does not exists, email valid and email not unique"""
def test_valid_email_does_not_exist_not_unique():
    mockedDao = mock.MagicMock()
    mockedDao.find.return_value = None
    user_controller = UserController(mockedDao)
    result = user_controller.get_user_by_email("hello@gmail.com")
    assert result == None

"""Email does not exists, email not valid and email unique"""
def test_not_valid_email_does_not_exist():
    with pytest.raises(ValueError, match=r"Error: invalid email address"):
        mockedDao = mock.MagicMock()
        mockedDao.find.return_value = None
        user_controller = UserController(mockedDao)
        user_controller.get_user_by_email("hello")

"""Email does not exists, email not valid and email not unique"""
def test_not_valid_email_does_not_exist_not_unique():
    with pytest.raises(ValueError, match=r"Error: invalid email address"):
        mockedDao = mock.MagicMock()
        mockedDao.find.return_value = None
        user_controller = UserController(mockedDao)
        user_controller.get_user_by_email("hello")