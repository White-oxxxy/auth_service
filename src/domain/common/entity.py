from abc import ABC
from dataclasses import (
    dataclass,
    field,
)

from domain.common.event import BaseDomainEvent
from domain.common.mixins import BusinessRuleValidationMixin


@dataclass(
    kw_only=True,
    slots=True,
)
class BaseEntity(ABC): ...


@dataclass(
    kw_only=True,
    slots=True,
)
class BaseAggregate(
    BusinessRuleValidationMixin,
    BaseEntity
):
    _events: list[BaseDomainEvent] = field(default_factory=list)

    def record_event(self, event: BaseDomainEvent) -> None:
        self._events.append(event)

    def get_events(self) -> list[BaseDomainEvent]:
        return self._events

    def clear_events(self) -> None:
        self._events.clear()

    def pull_events(self) -> list[BaseDomainEvent]:
        events = self.get_events().copy()

        self.clear_events()

        return events