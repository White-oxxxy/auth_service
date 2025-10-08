from dataclasses import dataclass

from domain.common.rule import BaseBusinessRule
from domain.user.value_objects import (
    UserSurnameValue,
    UserLastnameValue,
    UserNameValue,
)
from domain.user.rules.constants import UserBusinessRulesConsts


@dataclass(frozen=True)
class UserNameLengthMustBeGreaterThanMinimumLength(BaseBusinessRule):
    __message = "User name must be greater than {minimum_length}"

    current_name: UserNameValue
    minimum_length: int = UserBusinessRulesConsts.MIN_NAME_LEN.value

    def is_broken(self) -> bool:
        return len(self.current_name.value) <= self.minimum_length

    def get_message(self) -> str:
        return self.__message.format(minimum_length=self.minimum_length)


@dataclass(frozen=True)
class UserNameLengthMustBeLessOrEqualThanMaximumLength(BaseBusinessRule):
    __message = "User name must be less or equal than {maximum_length}"

    current_name: UserNameValue
    maximum_length: int = UserBusinessRulesConsts.MAX_NAME_LEN.value

    def is_broken(self) -> bool:
        return len(self.current_name.value) > self.maximum_length

    def get_message(self) -> str:
        return self.__message.format(maximum_length=self.maximum_length)


@dataclass(frozen=True)
class UserSurnameLengthMustBeGreaterThanMinimumLength(BaseBusinessRule):
    __message = "User surname must be greater than {minimum_length}"

    current_surname: UserSurnameValue
    minimum_length: int = UserBusinessRulesConsts.MIN_SURNAME_LEN.value

    def is_broken(self) -> bool:
        return len(self.current_surname.value) <= self.minimum_length

    def get_message(self) -> str:
        return self.__message.format(minimum_length=self.minimum_length)


@dataclass(frozen=True)
class UserSurnameLengthMustBeLessOrEqualThanMaximumLength(BaseBusinessRule):
    __message = "User surname must be less or equal than {maximum_length}"

    current_surname: UserSurnameValue
    maximum_length: int = UserBusinessRulesConsts.MAX_SURNAME_LEN.value

    def is_broken(self) -> bool:
        return len(self.current_surname.value) > self.maximum_length

    def get_message(self) -> str:
        return self.__message.format(maximum_length=self.maximum_length)


@dataclass(frozen=True)
class UserLastnameLengthMustBeGreaterThanMinimumLength(BaseBusinessRule):
    __message = "User lastname must be greater than {minimum_length}"

    current_lastname: UserLastnameValue
    minimum_length: int = UserBusinessRulesConsts.MIN_LASTNAME_LEN.value

    def is_broken(self) -> bool:
        return len(self.current_lastname.value) <= self.minimum_length

    def get_message(self) -> str:
        return self.__message.format(minimum_length=self.minimum_length)


@dataclass(frozen=True)
class UserLastnameLengthMustBeLessOrEqualThanMaximumLength(BaseBusinessRule):
    __message = "User lastname must be less or equal than {maximum_length}"

    current_lastname: UserLastnameValue
    maximum_length: int = UserBusinessRulesConsts.MAX_LASTNAME_LEN.value

    def is_broken(self) -> bool:
        return len(self.current_lastname.value) > self.maximum_length

    def get_message(self) -> str:
        return self.__message.format(maximum_length=self.maximum_length)