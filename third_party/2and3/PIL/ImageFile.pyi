# Stubs for PIL.ImageFile (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from . import Image

logger = ...  # type: Any
MAXBLOCK = ...  # type: int
SAFEBLOCK = ...  # type: Any
LOAD_TRUNCATED_IMAGES = ...  # type: bool
ERRORS = ...  # type: Any

def raise_ioerror(error): ...

class ImageFile(Image.Image):
    tile = ...  # type: Any
    readonly = ...  # type: int
    decoderconfig = ...  # type: Any
    decodermaxblock = ...  # type: Any
    fp = ...  # type: Any
    filename = ...  # type: Any
    def __init__(self, fp: Optional[Any] = ..., filename: Optional[Any] = ...) -> None: ...
    def draft(self, mode, size): ...
    def verify(self): ...
    map = ...  # type: Any
    im = ...  # type: Any
    size = ...  # type: Any
    def load(self): ...
    def load_prepare(self): ...
    def load_end(self): ...

class StubImageFile(ImageFile):
    __class__ = ...  # type: Any
    __dict__ = ...  # type: Any
    def load(self): ...

class Parser:
    incremental = ...  # type: Any
    image = ...  # type: Any
    data = ...  # type: Any
    decoder = ...  # type: Any
    offset = ...  # type: int
    finished = ...  # type: int
    def reset(self): ...
    decode = ...  # type: Any
    def feed(self, data): ...
    def close(self): ...
