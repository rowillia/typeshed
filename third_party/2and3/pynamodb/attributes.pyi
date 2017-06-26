from typing import Any, Callable, Dict, Generic, Iterable, List, Mapping, Optional, Text, Type, TypeVar, Union, Set

from datetime import datetime

_T = TypeVar('_T')
_KT = TypeVar('_KT')
_VT = TypeVar('_VT')
_MT = TypeVar('_MT', bound='MapAttribute')

class Attribute(Generic[_T]):
    attr_name: Optional[Text]
    attr_type: Text
    null: bool
    default: Any
    is_hash_key: bool
    is_range_key: bool
    def __init__(self, hash_key: bool = ..., range_key: bool = ..., null: Optional[bool] = ..., default: Optional[Union[_T, Callable[..., _T]]] = ..., attr_name: Optional[Text] = ...) -> None: ...
    def __set__(self, instance: Any, value: _T) -> None: ...
    def serialize(self, value: Any) -> Any: ...
    def deserialize(self, value: Any) -> Any: ...
    def get_value(self, value: Any) -> Any: ...

class SetMixin(object):
    def serialize(self, value): ...
    def deserialize(self, value): ...

class BinaryAttribute(Attribute[bytes]):
    def __get__(self, instance: Any, owner: Any) -> bytes: ...

class BinarySetAttribute(SetMixin, Attribute[Set[bytes]]):
    def __get__(self, instance: Any, owner: Any) -> Set[bytes]: ...

class UnicodeSetAttribute(SetMixin, Attribute[Set[Text]]):
    def element_serialize(self, value: Any) -> Any: ...
    def element_deserialize(self, value: Any) -> Any: ...
    def __get__(self, instance: Any, owner: Any) -> Set[Text]: ...

class UnicodeAttribute(Attribute[Text]):
    def __get__(self, instance: Any, owner: Any) -> Text: ...

class JSONAttribute(Attribute[Dict[Text, Any]]):
    def __get__(self, instance: Any, owner: Any) -> Dict[Text, Any]: ...

class LegacyBooleanAttribute(Attribute[bool]):
    def __get__(self, instance: Any, owner: Any) -> bool: ...

class BooleanAttribute(Attribute[bool]):
    def __get__(self, instance: Any, owner: Any) -> bool: ...

class NumberSetAttribute(SetMixin, Attribute[Set[float]]):
    def __get__(self, instance: Any, owner: Any) -> Set[float]: ...

class NumberAttribute(Attribute[float]):
    def __get__(self, instance: Any, owner: Any) -> float: ...

class UTCDateTimeAttribute(Attribute[datetime]):
    def __get__(self, instance: Any, owner: Any) -> datetime: ...

class NullAttribute(Attribute[None]):
    def __get__(self, instance: Any, owner: Any) -> None: ...

class MapAttributeMeta(type):
    def __init__(cls, name, bases, attrs) -> None: ...

class MapAttribute(Generic[_KT, _VT], Attribute[Mapping[_KT, _VT]], metaclass=MapAttributeMeta):
    attribute_values: Any
    def __init__(self, hash_key: bool = ..., range_key: bool = ..., null: Optional[bool] = ..., default: Optional[Union[Any, Callable[..., Any]]] = ..., attr_name: Optional[Text] = ..., **attrs) -> None: ...
    def __iter__(self) -> Iterable[_VT]: ...
    def __getattr__(self, attr: str) -> _VT: ...
    def __getitem__(self, item: _KT) -> _VT: ...
    def __set__(self, instance: Any, value: Union[MapAttribute[_KT, _VT], Mapping[_KT, _VT]]) -> None: ...
    def __get__(self: _MT, instance: Any, owner: Any) -> _MT: ...
    def is_type_safe(self, key: Any, value: Any) -> bool: ...
    def validate(self) -> bool: ...

class ListAttribute(Generic[_T], Attribute[List[_T]]):
    element_type: Any
    def __init__(self, hash_key: bool = ..., range_key: bool = ..., null: Optional[bool] = ..., default: Optional[Union[Any, Callable[..., Any]]] = ..., attr_name: Optional[Text] = ..., of: Optional[Type[_T]] = ...) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> List[_T]: ...

DESERIALIZE_CLASS_MAP: Dict[Text, Attribute]
SERIALIZE_CLASS_MAP: Dict[Type, Attribute]
SERIALIZE_KEY_MAP: Dict[Type, Text]
