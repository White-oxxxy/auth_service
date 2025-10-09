from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

@dataclass
class TransactionalManager(ABC):
    @abstractmethod
    async def commit(self) -> None: ...

    @abstractmethod
    async def flush(self) -> None: ...