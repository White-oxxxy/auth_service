from abc import ABC
from dataclasses import dataclass

from application.common.persistence.reader.interface import BaseReader
from application.user.persistence.reader.reader_models import UserReaderModel

@dataclass
class UserReader(
    BaseReader[UserReaderModel],
    ABC,
): ...