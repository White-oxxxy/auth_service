from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from domain.user.value_objects import UserIdValue


@dataclass
class AccessRevoker(ABC):
    @abstractmethod
    async def remove_all_user_access(self, user_id: UserIdValue) -> None: ...