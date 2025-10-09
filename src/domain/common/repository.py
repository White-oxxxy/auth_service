from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from typing import (
    Generic,
    TypeVar,
)

from domain.common.entity import BaseEntity
from domain.user.value_objects import UserIdValue

Entity = TypeVar("Entity", bound=BaseEntity)


@dataclass
class BaseRepository(
    Generic[Entity],
    ABC,
):
    @abstractmethod
    async def add(self, entity: Entity) -> None: ...

    @abstractmethod
    async def get_by_id(self, user_id: UserIdValue) -> Entity | None: ...

    @abstractmethod
    async def update(self, entity: Entity) -> None: ...

    @abstractmethod
    async def remove(self, entity: Entity) -> None: ...
