from dataclasses import dataclass

from domain.common.service import BaseService
from domain.user.ports.password_hasher import PasswordHasher
from domain.user.entities import UserAggregate
from domain.user.value_objects import (
    UserRawPasswordValue,
    UserHashPasswordValue,
)
from domain.user.value_objects.exceptions import CannotChangePasswordToUsedOne
from domain.user.rules import (
    UserRawPasswordLengthMustBeGreaterThanMinimumLength,
    UserRawPasswordLengthMustBeLessOrEqualThanMaximumLength,
)
from utils.data_structures import OrderedLifoSet


@dataclass
class ChangePasswordService(BaseService):
    _password_hasher: PasswordHasher

    async def execute(
        self,
        user: UserAggregate,
        new_raw_password: UserRawPasswordValue,
    ) -> None:
        user.check_rule(
            UserRawPasswordLengthMustBeGreaterThanMinimumLength(
                current_raw_password=new_raw_password,
            )
        )
        user.check_rule(
            UserRawPasswordLengthMustBeLessOrEqualThanMaximumLength(
                current_raw_password=new_raw_password,
            )
        )

        if await self._password_hasher.validate(
            raw_password=new_raw_password,
            hash_password=user.hashed_password,
        ):
            raise CannotChangePasswordToUsedOne()

        hashed_password_history: OrderedLifoSet[UserHashPasswordValue] = user.get_password_history()

        for hashed_password in hashed_password_history:
            if await self._password_hasher.validate(
                raw_password=new_raw_password,
                hash_password=hashed_password,
            ):
                raise CannotChangePasswordToUsedOne()

        new_hashed_password: UserHashPasswordValue = await self._password_hasher.hash(
            raw_password=new_raw_password,
        )

        user.change_password(
            new_password=new_hashed_password,
        )