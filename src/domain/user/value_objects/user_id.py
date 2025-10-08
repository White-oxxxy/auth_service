from dataclasses import dataclass

from uuid_utils import UUID

from domain.common.value_object import BaseSimpleValueObject


@dataclass(frozen=True)
class UserIdValue(BaseSimpleValueObject[UUID]):
    def validate(self) -> None:
        super().validate()

        self._check_type(expected_type=UUID)