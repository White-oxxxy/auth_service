from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from typing import (
    Any,
    TypeVar,
    Generic,
)

from domain.common.value_object.exceptions import (
    IncorrectValueTypeException,
    EmptyValueException,
)


VT = TypeVar("VT", bound=Any)


@dataclass(frozen=True)
class BaseValueObject(
    ABC,
):
    def __post_init__(self):
        return self.validate()

    @abstractmethod
    def validate(self) -> None: ...

    @property
    def vo_name(self) -> str:
        name: str = self.__class__.__name__

        return name


@dataclass(frozen=True)
class BaseSimpleValueObject(
    Generic[VT],
    BaseValueObject,
    ABC,
):
    value: VT

    def validate(self) -> None:
        if self.value is None:

            raise EmptyValueException()

    def _check_type(self, expected_type: type[Any]) -> None:
        if not isinstance(self.value, expected_type):

            raise IncorrectValueTypeException(
                expected_type=expected_type,
                actual_value=self.value
            )


@dataclass(frozen=True)
class BaseCompositeValueObject(
    BaseValueObject,
    ABC,
): ...