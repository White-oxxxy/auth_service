from abc import ABC
from dataclasses import dataclass

from domain.common.repository import BaseRepository
from domain.user.entities import UserAggregate


@dataclass
class UserRepository(
    BaseRepository[UserAggregate],
    ABC,
): ...
