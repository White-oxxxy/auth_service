from dataclasses import dataclass
from typing import ClassVar


@dataclass(eq=False)
class AppException(Exception):
    status_code: ClassVar[int] = 500

    @property
    def message(self) -> str:
        message = "App error!"

        return message


@dataclass(eq=False)
class DomainException(AppException):
    @property
    def message(self) -> str:
        message = "Domain error!"

        return message