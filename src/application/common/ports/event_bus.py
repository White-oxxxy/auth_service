from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from application.common.event import BaseIntegrationEvent
from domain.common.entity import BaseAggregate


@dataclass
class EventBus(ABC):
    @abstractmethod
    async def publish(
        self,
        event: BaseIntegrationEvent,
        source: BaseAggregate,
    ) -> None: ...