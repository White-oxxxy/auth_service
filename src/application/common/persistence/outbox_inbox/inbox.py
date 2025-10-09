from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from application.common.event import BaseIntegrationEvent


@dataclass
class Inbox(ABC):
    @abstractmethod
    async def add(self, event: BaseIntegrationEvent): ...

    @abstractmethod
    async def get_next_pending(self) -> BaseIntegrationEvent | None: ...

    @abstractmethod
    async def mark_as_processed(self) -> None: ...

    @abstractmethod
    async def mark_as_failed(self) -> None: ...