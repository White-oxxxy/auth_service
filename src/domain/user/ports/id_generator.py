from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from domain.user.value_objects.user_id import UserIdValue


@dataclass
class UserIdGenerator(ABC):
    @abstractmethod
    def generate(self) -> UserIdValue: ...