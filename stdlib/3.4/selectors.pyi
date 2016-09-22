# Stubs for selector
# See https://docs.python.org/3/library/selectors.html

from typing import Any, List, NamedTuple, Mapping, Tuple, Optional, Union
from abc import ABCMeta, abstractmethod
import socket


# Type aliases added mainly to preserve some context
#
# See https://github.com/python/typeshed/issues/482
# for details regarding how FileObject is typed.
FileObject = Union[int, socket.socket]
FileDescriptor = int
EventMask = int


EVENT_READ = ...  # type: EventMask
EVENT_WRITE = ...  # type: EventMask


SelectorKey = NamedTuple('SelectorKey', [
    ('fileobj', FileObject),
    ('fd', FileDescriptor),
    ('events', EventMask),
    ('data', Any)
])


class BaseSelector(metaclass=ABCMeta):
    @abstractmethod
    def register(self, fileobj: FileObject, events: EventMask, data: Any = None) -> SelectorKey: ...

    @abstractmethod
    def unregister(self, fileobj: FileObject) -> SelectorKey: ...

    def modify(self, fileobj: FileObject, events: EventMask, data: Any = None) -> SelectorKey: ...

    @abstractmethod
    def select(self, timeout: Optional[int] = None) -> List[Tuple[SelectorKey, EventMask]]: ...

    def close(self) -> None: ...

    def get_key(self, fileobj: FileObject) -> SelectorKey: ...

    @abstractmethod
    def get_map(self) -> Mapping[FileObject, SelectorKey]: ...

    def __enter__(self) -> BaseSelector: ...

    def __exit__(self, *args: Any) -> None: ...

class SelectSelector(BaseSelector):
    def register(self, fileobj: FileObject, events: EventMask, data: Any = None) -> SelectorKey: ...
    def unregister(self, fileobj: FileObject) -> SelectorKey: ...
    def select(self, timeout: Optional[int] = None) -> List[Tuple[SelectorKey, EventMask]]: ...
    def get_map(self) -> Mapping[FileObject, SelectorKey]: ...

class PollSelector(BaseSelector):
    def register(self, fileobj: FileObject, events: EventMask, data: Any = None) -> SelectorKey: ...
    def unregister(self, fileobj: FileObject) -> SelectorKey: ...
    def select(self, timeout: Optional[int] = None) -> List[Tuple[SelectorKey, EventMask]]: ...
    def get_map(self) -> Mapping[FileObject, SelectorKey]: ...

class EpollSelector(BaseSelector):
    def fileno(self) -> int: ...
    def register(self, fileobj: FileObject, events: EventMask, data: Any = None) -> SelectorKey: ...
    def unregister(self, fileobj: FileObject) -> SelectorKey: ...
    def select(self, timeout: Optional[int] = None) -> List[Tuple[SelectorKey, EventMask]]: ...
    def get_map(self) -> Mapping[FileObject, SelectorKey]: ...

class DevpollSelector(BaseSelector):
    def fileno(self) -> int: ...
    def register(self, fileobj: FileObject, events: EventMask, data: Any = None) -> SelectorKey: ...
    def unregister(self, fileobj: FileObject) -> SelectorKey: ...
    def select(self, timeout: Optional[int] = None) -> List[Tuple[SelectorKey, EventMask]]: ...
    def get_map(self) -> Mapping[FileObject, SelectorKey]: ...

class KqueueSelector(BaseSelector):
    def fileno(self) -> int: ...
    def register(self, fileobj: FileObject, events: EventMask, data: Any = None) -> SelectorKey: ...
    def unregister(self, fileobj: FileObject) -> SelectorKey: ...
    def select(self, timeout: Optional[int] = None) -> List[Tuple[SelectorKey, EventMask]]: ...
    def get_map(self) -> Mapping[FileObject, SelectorKey]: ...

class DefaultSelector(BaseSelector):
    def register(self, fileobj: FileObject, events: EventMask, data: Any = None) -> SelectorKey: ...
    def unregister(self, fileobj: FileObject) -> SelectorKey: ...
    def select(self, timeout: Optional[int] = None) -> List[Tuple[SelectorKey, EventMask]]: ...
    def get_map(self) -> Mapping[FileObject, SelectorKey]: ...