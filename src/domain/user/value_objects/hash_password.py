from dataclasses import dataclass

from domain.common.value_object.values import BaseSimpleValueObject
from domain.common.value_object.exceptions import EmptyValueException


@dataclass(frozen=True)
class UserHashPasswordValue(BaseSimpleValueObject[bytes]):
    def validate(self) -> None:
        super().validate()

        if len(self.value) == 0:
            raise EmptyValueException()

        self._check_type(expected_type=bytes)