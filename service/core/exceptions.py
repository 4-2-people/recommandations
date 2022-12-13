from fastapi import HTTPException


class AppException(HTTPException):
    status_code = 400
    detail = 'Application error'

    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            status_code=self.status_code,
            detail=self.detail
        )
