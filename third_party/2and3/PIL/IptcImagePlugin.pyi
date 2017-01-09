# Stubs for PIL.IptcImagePlugin (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from . import ImageFile

i8 = ...  # type: Any
i16 = ...  # type: Any
i32 = ...  # type: Any
o8 = ...  # type: Any
COMPRESSION = ...  # type: Any
PAD = ...  # type: Any

def i(c): ...
def dump(c): ...

class IptcImageFile(ImageFile.ImageFile):
    format = ...  # type: str
    format_description = ...  # type: str
    def getint(self, key): ...
    def field(self): ...
    im = ...  # type: Any
    def load(self): ...

def getiptcinfo(im): ...
