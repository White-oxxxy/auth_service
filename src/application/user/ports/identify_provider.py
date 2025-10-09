from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from domain.user.value_objects import UserIdValue


@dataclass
class IdentifyProvider(ABC):
    @abstractmethod
    async def get_current_user_id(self) -> UserIdValue: ...