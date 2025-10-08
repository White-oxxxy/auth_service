from dataclasses import dataclass
from typing import (
    Any,
    Iterable,
)

from domain.common.exception import DomainException


@dataclass(eq=False)
class ValueObjectException(DomainException):
    @property
    def message(self) -> str:
        message = "Value Object exception!"

        return message


@dataclass(eq=False)
class IncorrectValueTypeException(
    ValueObjectException
):
    expected_type: type[Any]
    actual_value: Any

    @property
    def message(self) -> str:
        message = f"Incorrect value type! Excepted type is {self.expected_type}, current type is {type(self.actual_value)}!"

        return message


@dataclass(eq=False)
class EmptyValueException(ValueObjectException):
    @property
    def message(self) -> str:
        message = "Value cannot be empty!"

        return message


@dataclass(eq=False)
class InvalidValueException(ValueObjectException):
    actual_value: Any
    allowed_values: Iterable[Any]

    @property
    def message(self) -> str:
        message = f"Invalid value for ValueObject: {self.actual_value}. Allowed values: {list(self.allowed_values)}."

        return message


@dataclass(eq=False)
class IncorrectFormatException(ValueObjectException):
    @property
    def message(self) -> str:
        message = f"Incorrect name format! Must start with upper symbol and only russian!!"

        return message