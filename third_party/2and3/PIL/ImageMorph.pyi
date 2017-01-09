# Stubs for PIL.ImageMorph (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

LUT_SIZE = ...  # type: Any

class LutBuilder:
    patterns = ...  # type: Any
    lut = ...  # type: Any
    def __init__(self, patterns: Optional[Any] = ..., op_name: Optional[Any] = ...) -> None: ...
    def add_patterns(self, patterns): ...
    def build_default_lut(self): ...
    def get_lut(self): ...
    def build_lut(self): ...

class MorphOp:
    lut = ...  # type: Any
    def __init__(self, lut: Optional[Any] = ..., op_name: Optional[Any] = ..., patterns: Optional[Any] = ...) -> None: ...
    def apply(self, image): ...
    def match(self, image): ...
    def get_on_pixels(self, image): ...
    def load_lut(self, filename): ...
    def save_lut(self, filename): ...
    def set_lut(self, lut): ...
