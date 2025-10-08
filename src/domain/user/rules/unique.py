from dataclasses import dataclass

from domain.common.rule import BaseBusinessRule
from domain.common.value_object import BaseSimpleValueObject


@dataclass(frozen=True)
class CannotChangeValueToTheCurrentOne(BaseBusinessRule):
    __message = "Cannot change {current_value} to {new_value}! (already using)"

    current_value: BaseSimpleValueObject
    new_value: BaseSimpleValueObject

    def is_broken(self) -> bool:
        return self.new_value.value == self.current_value.value

    def get_message(self) -> str:
        return self.__message.format(
            current_value=self.current_value.value,
            new_value=self.new_value.value,
        )