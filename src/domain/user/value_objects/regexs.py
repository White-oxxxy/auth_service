import re

from domain.common.enum import BaseEnum


class UserValueObjectsRegex(
    BaseEnum,
    str,
):
    EMAIL_REGEX = re.compile(
        r"^(?:[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+"
        r"(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*"
        r"|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-"
        r"\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")"
        r"@"
        r"(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+"
        r"[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?"
        r"|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}"
        r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|"
        r"[a-zA-Z0-9-]*[a-zA-Z0-9]:"
        r"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]"
        r"|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)])$"
    )

    NAME_REGEX = re.compile(r'^[A-ZА-Я][a-zа-я]+(?:-[A-ZА-Я][a-zа-я]+)?$')

    @property
    def compiled(self) -> re.Pattern:
        return re.compile(self.value)


class UserValueObjectsRegexsProvider:
    NAME = UserValueObjectsRegex.NAME_REGEX.compiled
    EMAIL = UserValueObjectsRegex.EMAIL_REGEX.compiled