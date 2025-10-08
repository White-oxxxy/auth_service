from dataclasses import dataclass

from domain.common.exception import DomainException


@dataclass(eq=False)
class BusinessRuleValidationException(DomainException):
    rule: "BaseBusinessRule"

    @property
    def message(self) -> str:
        message: str = self.rule.get_message()

        return message


@dataclass(frozen=True)
class BaseBusinessRule:
    __message = "Business rule is broken!"

    def get_message(self) -> str:
        return self.__message

    def is_broken(self) -> bool:
        ...