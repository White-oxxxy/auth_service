from dataclasses import dataclass

from application.common.event import BaseIntegrationEvent
from application.common.ports.event_bus import EventBus
from application.common.persistence.outbox_inbox.outbox import Outbox
from domain.common.entity import BaseAggregate


@dataclass
class EventBusImpl(EventBus):
    _outbox: Outbox

    async def publish(
        self,
        event: BaseIntegrationEvent,
        source: BaseAggregate,
    ) -> None:
        await self._outbox.add(
            event=event,
            source=source,
        )