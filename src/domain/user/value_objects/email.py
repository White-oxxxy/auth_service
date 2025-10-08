from dataclasses import dataclass

from domain.common.value_object.values import BaseSimpleValueObject
from domain.common.value_object.exceptions import (
    EmptyValueException,
    IncorrectFormatException,
)
from domain.user.value_objects.regexs import UserValueObjectsRegexsProvider


@dataclass(frozen=True)
class UserEmailValue(BaseSimpleValueObject[str]):
    _regex = UserValueObjectsRegexsProvider.EMAIL

    def validate(self) -> None:
        super().validate()

        self._check_type(expected_type=str)

        if len(self.value) == 0:
            raise EmptyValueException()

        if not self.__validate_name(email=self.value):
            raise IncorrectFormatException()

    def __validate_name(self, email: str) -> bool:
        return bool(self._regex.match(email))