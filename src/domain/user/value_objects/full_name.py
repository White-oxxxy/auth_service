from dataclasses import dataclass

from domain.common.value_object import (
    BaseSimpleValueObject,
    BaseCompositeValueObject,
)
from domain.common.value_object.exceptions import (
    EmptyValueException,
    IncorrectFormatException,
)
from domain.user.value_objects.regexs import UserValueObjectsRegexsProvider


@dataclass(frozen=True)
class UserFullNameValue(BaseCompositeValueObject):
    name: "UserNameValue"
    surname: "UserSurnameValue"
    last_name: "UserLastnameValue"

    def validate(self) -> None:
        self.name.validate()
        self.surname.validate()
        self.last_name.validate()


@dataclass(frozen=True)
class UserNameValue(BaseSimpleValueObject[str]):
    _regex = UserValueObjectsRegexsProvider.NAME

    def validate(self) -> None:
        super().validate()

        self._check_type(expected_type=str)

        if len(self.value) == 0:
            raise EmptyValueException()

        if not self.__validate_name(name=self.value):
            raise IncorrectFormatException()

    def __validate_name(self, name: str) -> bool:
        return bool(self._regex.match(name))


@dataclass(frozen=True)
class UserSurnameValue(BaseSimpleValueObject[str]):
    _regex = UserValueObjectsRegexsProvider.NAME

    def validate(self) -> None:
        super().validate()

        self._check_type(expected_type=str)

        if len(self.value) == 0:
            raise EmptyValueException()

        if not self.__validate_name(name=self.value):
            raise IncorrectFormatException()

    def __validate_name(self, name: str) -> bool:
        return bool(self._regex.match(name))


@dataclass(frozen=True)
class UserLastnameValue(BaseSimpleValueObject[str]):
    _regex = UserValueObjectsRegexsProvider.NAME

    def validate(self) -> None:
        super().validate()

        self._check_type(expected_type=str)

        if len(self.value) == 0:
            raise EmptyValueException()

        if not self.__validate_name(name=self.value):
            raise IncorrectFormatException()

    def __validate_name(self, name: str) -> bool:
        return bool(self._regex.match(name))