from typing import Any, Optional

class PynamoDBException(Exception):
    msg = ...  # type: Any
    cause = ...  # type: Any
    def __init__(self, msg: Optional[Any] = ..., cause: Optional[Any] = ...) -> None: ...

class PynamoDBConnectionError(PynamoDBException):
    msg = ...  # type: str

class DeleteError(PynamoDBConnectionError):
    msg = ...  # type: str

class QueryError(PynamoDBConnectionError):
    msg = ...  # type: str

class ScanError(PynamoDBConnectionError):
    msg = ...  # type: str

class PutError(PynamoDBConnectionError):
    msg = ...  # type: str

class UpdateError(PynamoDBConnectionError):
    msg = ...  # type: str

class GetError(PynamoDBConnectionError):
    msg = ...  # type: str

class TableError(PynamoDBConnectionError):
    msg = ...  # type: str

class DoesNotExist(PynamoDBException):
    msg = ...  # type: str

class TableDoesNotExist(PynamoDBException):
    def __init__(self, table_name) -> None: ...

class VerboseClientError(Exception):
    MSG_TEMPLATE = ...  # type: Any
    def __init__(self, error_response, operation_name, verbose_properties: Optional[Any] = ...) -> None: ...
