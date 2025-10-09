from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass


@dataclass(
    frozen=True,
    kw_only=True,
    slots=True,
)
class BaseQuery(ABC): ...


@dataclass(
    frozen=True,
    kw_only=True,
    slots=True,
)
class BaseQueryResult(ABC): ...


@dataclass
class BaseQueryHandler(ABC):
    @abstractmethod
    async def execute(self, query: BaseQuery) -> BaseQueryResult: ...