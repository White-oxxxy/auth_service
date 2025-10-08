from dataclasses import dataclass

from domain.common.event import BaseDomainEvent
from domain.user.enums import UserRole
from domain.user.value_objects import (
    UserIdValue,
    UserFullNameValue,
    UserEmailValue,
)


@dataclass(frozen=True)
class UserCreatedEvent(BaseDomainEvent):
    user_id: UserIdValue
    full_name: UserFullNameValue
    email: UserEmailValue
    role: UserRole


@dataclass(frozen=True)
class UserEmailChangedEvent(BaseDomainEvent):
    user_id: UserIdValue
    new_email: UserEmailValue