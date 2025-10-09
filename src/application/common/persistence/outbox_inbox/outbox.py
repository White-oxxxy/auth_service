from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from domain.common.entity import BaseAggregate
from application.common.event import BaseIntegrationEvent
from application.common.persistence.outbox_inbox.message import Message


@dataclass
class Outbox(ABC):
    @abstractmethod
    async def add(
        self,
        event: BaseIntegrationEvent,
        source: BaseAggregate = None,
    ) -> None: ...

    @abstractmethod
    async def get_next_pending(self) -> BaseIntegrationEvent | None: ...

    @abstractmethod
    async def mark_as_sent(self) -> None: ...

    @abstractmethod
    async def mark_as_failed(self) -> None: ...

    @abstractmethod
    async def get_all_deliveries(self) -> list[Message]: ...