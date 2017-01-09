# Stubs for PIL.MpoImagePlugin (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from . import JpegImagePlugin

class MpoImageFile(JpegImagePlugin.JpegImageFile):
    format = ...  # type: str
    format_description = ...  # type: str
    def load_seek(self, pos): ...
    @property
    def n_frames(self): ...
    @property
    def is_animated(self): ...
    fp = ...  # type: Any
    offset = ...  # type: Any
    tile = ...  # type: Any
    def seek(self, frame): ...
    def tell(self): ...
