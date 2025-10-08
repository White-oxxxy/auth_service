from dataclasses import dataclass

from domain.common.value_object.exceptions import ValueObjectException


@dataclass(eq=False)
class CannotChangePasswordToUsedOne(ValueObjectException):
    @property
    def message(self) -> str:
        message = "Cannot change password to used one!"

        return message