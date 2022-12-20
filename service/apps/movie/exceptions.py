from core.exceptions import AppException


class InvalidScoreError(AppException):
    detail = 'Score must be greater than 0 and less than or equal to 10'
