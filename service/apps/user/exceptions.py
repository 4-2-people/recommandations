from core.exceptions import AppException


class UserAlreadyExists(AppException):
    detail = 'User already exists'


class UserNotFoundError(AppException):
    detail = 'User with specified credentials does not exist'


class UserCredentialsError(AppException):
    detail = 'Wrong username or password'
