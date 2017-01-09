# Stubs for PIL.ContainerIO (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class ContainerIO:
    fh = ...  # type: Any
    pos = ...  # type: int
    offset = ...  # type: Any
    length = ...  # type: Any
    def __init__(self, file, offset, length) -> None: ...
    def isatty(self): ...
    def seek(self, offset, mode: int = ...): ...
    def tell(self): ...
    def read(self, n: int = ...): ...
    def readline(self): ...
    def readlines(self): ...
