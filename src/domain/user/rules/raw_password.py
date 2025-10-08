from dataclasses import dataclass

from domain.common.rule import BaseBusinessRule
from domain.user.value_objects import UserRawPasswordValue
from domain.user.rules.constants import UserBusinessRulesConsts


@dataclass(frozen=True)
class UserRawPasswordLengthMustBeGreaterThanMinimumLength(BaseBusinessRule):
    __message = "User raw password must be greater than {minimum_length}"

    current_raw_password: UserRawPasswordValue
    minimum_length: int = UserBusinessRulesConsts.MIN_PASSWORD_LEN.value

    def is_broken(self) -> bool:
        return len(self.current_raw_password.value) <= self.minimum_length

    def get_message(self) -> str:
        return self.__message.format(minimum_length=self.minimum_length)


@dataclass(frozen=True)
class UserRawPasswordLengthMustBeLessOrEqualThanMaximumLength(BaseBusinessRule):
    __message = "User raw password must be less or equal than {maximum_length}"

    current_raw_password: UserRawPasswordValue
    maximum_length: int = UserBusinessRulesConsts.MAX_PASSWORD_LEN.value

    def is_broken(self) -> bool:
        return len(self.current_raw_password.value) > self.maximum_length

    def get_message(self) -> str:
        return self.__message.format(maximum_length=self.maximum_length)