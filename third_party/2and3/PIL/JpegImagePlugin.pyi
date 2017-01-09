# Stubs for PIL.JpegImagePlugin (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from . import ImageFile

i8 = ...  # type: Any
o8 = ...  # type: Any
i16 = ...  # type: Any
i32 = ...  # type: Any

def Skip(self, marker): ...
def APP(self, marker): ...
def COM(self, marker): ...
def SOF(self, marker): ...
def DQT(self, marker): ...

MARKER = ...  # type: Any

class JpegImageFile(ImageFile.ImageFile):
    format = ...  # type: str
    format_description = ...  # type: str
    mode = ...  # type: Any
    size = ...  # type: Any
    tile = ...  # type: Any
    decoderconfig = ...  # type: Any
    def draft(self, mode, size): ...
    im = ...  # type: Any
    def load_djpeg(self): ...

RAWMODE = ...  # type: Any
zigzag_index = ...  # type: Any
samplings = ...  # type: Any

def convert_dict_qtables(qtables): ...
def get_sampling(im): ...
def jpeg_factory(fp: Optional[Any] = ..., filename: Optional[Any] = ...): ...
