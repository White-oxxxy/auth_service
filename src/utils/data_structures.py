from collections import OrderedDict
from typing import (
    Any,
    Generic,
    Iterable,
    Iterator,
    TypeVar,
)

T = TypeVar("T", bound=Any)


class OrderedLifoSet(OrderedDict[T, None], Generic[T]):
    def __init__(
        self,
        limit: int = 5,
        iterable: Iterable[T] | None = None,
    ) -> None:
        super().__init__()
        self._limit = limit

        if iterable:
            for item in iterable:
                self.add(item)

    def __iter__(self) -> Iterator[T]:
        return reversed(self.keys())

    def add(self, item: T) -> None:
        if item in self:
            del self[item]
        self[item] = None

        if len(self) > self._limit:
            self.popitem(last=False)
