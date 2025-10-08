from dataclasses import dataclass

from domain.common.rule import BaseBusinessRule
from domain.user.value_objects import UserEmailValue
from domain.user.rules.constants import UserBusinessRulesConsts


@dataclass(frozen=True)
class UserEmailLengthMustBeGreaterThanMinimumLength(BaseBusinessRule):
    __message = "User email must be greater than {minimum_length}"

    current_email: UserEmailValue
    minimum_length: int = UserBusinessRulesConsts.MIN_NAME_LEN.value

    def is_broken(self) -> bool:
        return len(self.current_email.value) <= self.minimum_length

    def get_message(self) -> str:
        return self.__message.format(minimum_length=self.minimum_length)


@dataclass(frozen=True)
class UserEmailLengthMustBeLessOrEqualThanMaximumLength(BaseBusinessRule):
    __message = "User email must be less or equal than {maximum_length}"

    current_email: UserEmailValue
    maximum_length: int = UserBusinessRulesConsts.MAX_NAME_LEN.value

    def is_broken(self) -> bool:
        return len(self.current_email.value) > self.maximum_length

    def get_message(self) -> str:
        return self.__message.format(maximum_length=self.maximum_length)