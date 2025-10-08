from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from domain.user.value_objects.raw_password import UserRawPasswordValue
from domain.user.value_objects.hash_password import UserHashPasswordValue


@dataclass
class PasswordHasher(ABC):
    @abstractmethod
    async def hash(self, raw_password: UserRawPasswordValue) -> UserHashPasswordValue: ...

    @abstractmethod
    async def validate(
        self,
        raw_password: UserRawPasswordValue,
        hash_password: UserHashPasswordValue,
    ) -> bool: ...