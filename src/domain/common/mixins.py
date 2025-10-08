from dataclasses import dataclass

from domain.common.rule import (
    BaseBusinessRule,
    BusinessRuleValidationException,
)


@dataclass
class BusinessRuleValidationMixin:
    def check_rule(self, rule: BaseBusinessRule) -> None:
        self.__validate_rule(rule=rule)

    @staticmethod
    def __validate_rule(rule: BaseBusinessRule) -> None:
        if rule.is_broken():
            raise BusinessRuleValidationException(rule=rule)


def check_rule(rule: BaseBusinessRule):
    if rule.is_broken():
        raise BusinessRuleValidationException(rule=rule)