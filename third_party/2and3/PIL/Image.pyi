# Stubs for PIL.Image (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, IO, Optional, Text, Tuple, Union
from PIL import PixelAccess as PixelAccess, _imaging as core

logger = ...  # type: Any

class DecompressionBombWarning(RuntimeWarning): ...

class _imaging_not_installed:
    def __getattr__(self, id): ...

MAX_IMAGE_PIXELS = ...  # type: Any
builtins = ...  # type: Any
USE_CFFI_ACCESS = ...  # type: Any
HAS_CFFI = ...  # type: bool

def isImageType(t): ...

NONE = ...  # type: int
FLIP_LEFT_RIGHT = ...  # type: int
FLIP_TOP_BOTTOM = ...  # type: int
ROTATE_90 = ...  # type: int
ROTATE_180 = ...  # type: int
ROTATE_270 = ...  # type: int
TRANSPOSE = ...  # type: int
AFFINE = ...  # type: int
EXTENT = ...  # type: int
PERSPECTIVE = ...  # type: int
QUAD = ...  # type: int
MESH = ...  # type: int
NEAREST = ...  # type: int
LANCZOS = ...  # type: int
ANTIALIAS = ...  # type: int
BILINEAR = ...  # type: int
LINEAR = ...  # type: int
BICUBIC = ...  # type: int
CUBIC = ...  # type: int
ORDERED = ...  # type: int
RASTERIZE = ...  # type: int
FLOYDSTEINBERG = ...  # type: int
WEB = ...  # type: int
ADAPTIVE = ...  # type: int
MEDIANCUT = ...  # type: int
MAXCOVERAGE = ...  # type: int
FASTOCTREE = ...  # type: int
NORMAL = ...  # type: int
SEQUENCE = ...  # type: int
CONTAINER = ...  # type: int
DEFAULT_STRATEGY = ...  # type: Any
FILTERED = ...  # type: Any
HUFFMAN_ONLY = ...  # type: Any
RLE = ...  # type: Any
FIXED = ...  # type: Any
ID = ...  # type: Any
OPEN = ...  # type: Any
MIME = ...  # type: Any
SAVE = ...  # type: Any
SAVE_ALL = ...  # type: Any
EXTENSION = ...  # type: Any
MODES = ...  # type: Any

def getmodebase(mode): ...
def getmodetype(mode): ...
def getmodebandnames(mode): ...
def getmodebands(mode): ...
def preinit(): ...
def init(): ...
def coerce_e(value): ...

class _E:
    data = ...  # type: Any
    def __init__(self, data) -> None: ...
    def __add__(self, other): ...
    def __mul__(self, other): ...

class Image:
    format = ...  # type: Any
    format_description = ...  # type: Any
    im = ...  # type: Any
    mode = ...  # type: str
    size = ...  # type: Tuple[int, int]
    palette = ...  # type: Any
    info = ...  # type: Any
    category = ...  # type: Any
    readonly = ...  # type: int
    pyaccess = ...  # type: Any
    def __init__(self) -> None: ...
    @property
    def width(self): ...
    @property
    def height(self): ...
    def __enter__(self): ...
    def __exit__(self, *args): ...
    def close(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __getattr__(self, name): ...
    def tobytes(self, encoder_name: str = ..., *args): ...
    def tostring(self, *args, **kw): ...
    def tobitmap(self, name: str = ...): ...
    def frombytes(self, data, decoder_name: str = ..., *args): ...
    def fromstring(self, *args, **kw): ...
    def load(self) -> PixelAccess.PixelAccess: ...
    def verify(self): ...
    def convert(self, mode: Optional[Text] = ..., matrix: Optional[Any] = ..., dither: Optional[Any] = ..., palette: Any = ..., colors: int = ...) -> Image: ...
    def quantize(self, colors: int = ..., method: Optional[Any] = ..., kmeans: int = ..., palette: Optional[Any] = ...): ...
    def copy(self): ...
    def crop(self, box: Optional[Tuple[int, int, int, int]] = ...) -> Image: ...
    def draft(self, mode, size): ...
    def filter(self, filter): ...
    def getbands(self): ...
    def getbbox(self): ...
    def getcolors(self, maxcolors: int = ...): ...
    def getdata(self, band: Optional[Any] = ...): ...
    def getextrema(self): ...
    def getim(self): ...
    def getpalette(self): ...
    def getpixel(self, xy): ...
    def getprojection(self): ...
    def histogram(self, mask: Optional[Any] = ..., extrema: Optional[Any] = ...): ...
    def offset(self, xoffset, yoffset: Optional[Any] = ...): ...
    def paste(self, im, box: Optional[Any] = ..., mask: Optional[Any] = ...): ...
    def point(self, lut, mode: Optional[Any] = ...): ...
    def putalpha(self, alpha): ...
    def putdata(self, data, scale: float = ..., offset: float = ...): ...
    def putpalette(self, data, rawmode: str = ...): ...
    def putpixel(self, xy, value): ...
    def resize(self, size: Tuple[int, int], resample: Any = ...) -> Image: ...
    def rotate(self, angle, resample: Any = ..., expand: int = ...): ...
    encoderinfo = ...  # type: Any
    encoderconfig = ...  # type: Any
    def save(self, fp: Union[Text, IO[bytes]], format: Optional[Any] = ..., **params) -> None: ...
    def seek(self, frame): ...
    def show(self, title: Optional[Any] = ..., command: Optional[Any] = ...): ...
    def split(self): ...
    def tell(self): ...
    def thumbnail(self, size, resample: Any = ...): ...
    def transform(self, size, method, data: Optional[Any] = ..., resample: Any = ..., fill: int = ...): ...
    def transpose(self, method) -> Image: ...
    def effect_spread(self, distance): ...
    def toqimage(self): ...
    def toqpixmap(self): ...

class _ImageCrop(Image):
    mode = ...  # type: Any
    size = ...  # type: Any
    im = ...  # type: Any
    def __init__(self, im, box) -> None: ...
    def load(self): ...

class ImagePointHandler: ...
class ImageTransformHandler: ...

def new(mode: str, size: Tuple[int, int], color: int = ...) -> Image: ...
def frombytes(mode, size, data, decoder_name: str = ..., *args): ...
def fromstring(*args, **kw): ...
def frombuffer(mode, size, data, decoder_name: str = ..., *args): ...
def fromarray(obj, mode: Optional[Any] = ...): ...
def fromqimage(im): ...
def fromqpixmap(im): ...
def open(fp: Union[Text, IO[bytes]], mode: str = ...) -> Image: ...
def alpha_composite(im1, im2): ...
def blend(im1, im2, alpha): ...
def composite(image1, image2, mask): ...
def eval(image, *args): ...
def merge(mode, bands): ...
def register_open(id, factory, accept: Optional[Any] = ...): ...
def register_mime(id, mimetype): ...
def register_save(id, driver): ...
def register_save_all(id, driver): ...
def register_extension(id, extension): ...
def effect_mandelbrot(size, extent, quality): ...
def effect_noise(size, sigma): ...
