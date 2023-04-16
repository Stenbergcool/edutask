import pytest
from src.controllers.usercontroller import UserController
import unittest.mock as mock

"""Email does not exists, email valid and email unique"""
def test_valid_email_does_not_exist_unique():
    mockeddao = mock.MagicMock()
    mockeddao.find.return_value = None
    user_contoller = UserController(mockeddao)
    result = user_contoller.get_user_by_email("hello@gmail.com")
    assert result == None

"""Email does not exists, email valid and email not unique"""
def test_valid_email_does_not_exit_not_unique():
    mockeddao = mock.MagicMock()
    mockeddao.find.return_value = None
    user_contoller = UserController(mockeddao)
    result = user_contoller.get_user_by_email("hello@gmail.com")
    assert result == None

"""Email does not exists, email not valid and email unique"""
def test_not_valid_email_does_not_exit():
    with pytest.raises(ValueError, match=r"Error: invalid email address"):
        mockeddao = mock.MagicMock()
        mockeddao.find.return_value = None
        user_contoller = UserController(mockeddao)
        user_contoller.get_user_by_email("hello")

"""Email does not exists, email not valid and email not unique"""
def test_not_valid_email_does_not_exit_not_unique():
    with pytest.raises(ValueError, match=r"Error: invalid email address"):
        mockeddao = mock.MagicMock()
        mockeddao.find.return_value = None
        user_contoller = UserController(mockeddao)
        user_contoller.get_user_by_email("hello")