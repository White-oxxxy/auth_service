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
class BaseCommand(ABC): ...


@dataclass
class BaseCommandHandler(ABC):
    @abstractmethod
    async def execute(self, command: BaseCommand) -> None: ...