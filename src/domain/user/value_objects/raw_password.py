from dataclasses import dataclass

from domain.common.value_object.values import BaseSimpleValueObject
from domain.common.value_object.exceptions import EmptyValueException


@dataclass(frozen=True)
class UserRawPasswordValue(BaseSimpleValueObject[str]):
    def validate(self) -> None:
        super().validate()

        self._check_type(expected_type=str)

        if len(self.value) == 0:
            raise EmptyValueException()