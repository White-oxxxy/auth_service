from dataclasses import (
    dataclass,
    field,
)

from domain.common.entity import BaseAggregate
from domain.user.enums import UserRole
from domain.user.value_objects import (
    UserIdValue,
    UserFullNameValue,
    UserHashPasswordValue,
    UserEmailValue,
)
from domain.user.events import UserEmailChangedEvent
from domain.user.rules import (
    UserEmailLengthMustBeLessOrEqualThanMaximumLength,
    UserEmailLengthMustBeGreaterThanMinimumLength,
    CannotChangeValueToTheCurrentOne,
)
from utils.data_structures import OrderedLifoSet


@dataclass(
    kw_only=True,
    slots=True,
)
class UserAggregate(BaseAggregate):
    id: UserIdValue
    full_name: UserFullNameValue
    email: UserEmailValue
    role: UserRole
    hashed_password: UserHashPasswordValue
    _hashed_password_history: OrderedLifoSet[UserHashPasswordValue] = field(default_factory=OrderedLifoSet)

    def change_password(self, new_password: UserHashPasswordValue) -> None:
        self._hashed_password_history.add(self.hashed_password)

        self.hashed_password = new_password

    def change_email(self, new_email: UserEmailValue) -> None:
        self.check_rule(
            CannotChangeValueToTheCurrentOne(
                current_value=self.email,
                new_value=new_email,
            )
        )
        self.check_rule(
            UserEmailLengthMustBeGreaterThanMinimumLength(
                current_email=new_email,
            )
        )
        self.check_rule(
            UserEmailLengthMustBeLessOrEqualThanMaximumLength(
                current_email=new_email,
            )
        )

        self.email = new_email

        self.record_event(
            UserEmailChangedEvent(
                user_id=self.id,
                new_email=new_email
            )
        )

    def change_role(self, new_role: UserRole) -> None:
        self.role = new_role

    def change_fullname(self, new_full_name: UserFullNameValue) -> None:
        self.full_name = new_full_name

    def get_password_history(self) -> OrderedLifoSet[UserHashPasswordValue]:
        return self._hashed_password_history