from fastapi import HTTPException
from typing import Optional

class AppBaseException(HTTPException):
    """Base exception for all application-specific errors."""

    def __init__(self, status_code: int, detail: str, code: Optional[str] = None, data: Optional[dict] = None):
        self.code = code
        self.data = data
        super().__init__(status_code=status_code, detail=detail)


class TodoNotFoundError(AppBaseException):
    def __init__(self, todo_id=None):
        message = "Todo not found" if todo_id is None else f"Todo with id {todo_id} not found"
        super().__init__(status_code=404, detail=message)

class TodoCreationError(AppBaseException):
    def __init__(self, error: str):
        super().__init__(status_code=500, detail=f"Failed to create todo: {error}")


class UserNotFoundError(AppBaseException):
    def __init__(self, user_id=None):
        message = "User not found" if user_id is None else f"User with id {user_id} not found"
        super().__init__(status_code=404, detail=message)

class PasswordMismatchError(AppBaseException):
    def __init__(self):
        super().__init__(status_code=400, detail="New passwords do not match")

class InvalidPasswordError(AppBaseException):
    def __init__(self):
        super().__init__(status_code=401, detail="Current password is incorrect")

class AuthenticationError(AppBaseException):
    def __init__(self, message: str = "Could not validate user"):
        super().__init__(status_code=401, detail=message)
