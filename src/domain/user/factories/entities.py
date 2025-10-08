from dataclasses import dataclass
from uuid_utils import UUID

from domain.common.factory import IBaseEntityFactory
from domain.common.mixins import check_rule
from domain.user.entities import UserAggregate
from domain.user.enums import UserRole
from domain.user.value_objects import (
    UserEmailValue,
    UserFullNameValue,
    UserHashPasswordValue,
    UserRawPasswordValue,
    UserIdValue,
)
from domain.user.ports.password_hasher import PasswordHasher
from domain.user.ports.id_generator import UserIdGenerator
from domain.user.factories.value_odjects import UserValueFactory
from domain.user.events import UserCreatedEvent
from domain.user.rules import (
    UserEmailLengthMustBeLessOrEqualThanMaximumLength,
    UserEmailLengthMustBeGreaterThanMinimumLength,
    UserNameLengthMustBeLessOrEqualThanMaximumLength,
    UserNameLengthMustBeGreaterThanMinimumLength,
    UserSurnameLengthMustBeGreaterThanMinimumLength,
    UserSurnameLengthMustBeLessOrEqualThanMaximumLength,
    UserLastnameLengthMustBeGreaterThanMinimumLength,
    UserLastnameLengthMustBeLessOrEqualThanMaximumLength,
    UserRawPasswordLengthMustBeLessOrEqualThanMaximumLength,
    UserRawPasswordLengthMustBeGreaterThanMinimumLength,
)


@dataclass
class UserEntityFactory(IBaseEntityFactory):
    _user_value_factory: UserValueFactory
    _id_generator: UserIdGenerator
    _password_hasher: PasswordHasher

    async def create_user(
        self,
        name: str,
        surname: str,
        lastname: str,
        email: str,
        role: str | None,
        raw_password: str | None,
        hashed_password: bytes | None,
        user_id: UUID | None = None,
    ) -> UserAggregate:
        if not user_id:
            fullname_value: UserFullNameValue = self._user_value_factory.create_fullname_value(
                name=name,
                surname=surname,
                lastname=lastname,
            )
            check_rule(
                UserNameLengthMustBeGreaterThanMinimumLength(
                    current_name=fullname_value.name,
                )
            )
            check_rule(
                UserNameLengthMustBeLessOrEqualThanMaximumLength(
                    current_name=fullname_value.name,
                )
            )
            check_rule(
                UserSurnameLengthMustBeGreaterThanMinimumLength(
                    current_surname=fullname_value.surname,
                )
            )
            check_rule(
                UserSurnameLengthMustBeLessOrEqualThanMaximumLength(
                    current_surname=fullname_value.surname,
                )
            )
            check_rule(
                UserLastnameLengthMustBeGreaterThanMinimumLength(
                    current_lastname=fullname_value.last_name,
                )
            )
            check_rule(
                UserLastnameLengthMustBeLessOrEqualThanMaximumLength(
                    current_lastname=fullname_value.last_name,
                )
            )

            email_value: UserEmailValue = self._user_value_factory.create_email_value(email=email)
            check_rule(
                UserEmailLengthMustBeGreaterThanMinimumLength(
                    current_email=email_value,
                )
            )
            check_rule(
                UserEmailLengthMustBeLessOrEqualThanMaximumLength(
                    current_email=email_value,
                )
            )

            raw_password_value: UserRawPasswordValue = self._user_value_factory.create_raw_password_value(
                raw_password=raw_password,
            )
            check_rule(
                UserRawPasswordLengthMustBeGreaterThanMinimumLength(
                    current_raw_password=raw_password_value,
                )
            )
            check_rule(
                UserRawPasswordLengthMustBeLessOrEqualThanMaximumLength(
                    current_raw_password=raw_password_value,
                )
            )

            hashed_password_value: UserHashPasswordValue = await self._password_hasher.hash(
                raw_password=raw_password_value
            )

            user_id_value: UserIdValue = self._id_generator.generate()

            role_value = UserRole.USER

        else:
            fullname_value: UserFullNameValue = self._user_value_factory.create_fullname_value(
                name=name,
                surname=surname,
                lastname=lastname,
            )
            email_value: UserEmailValue = self._user_value_factory.create_email_value(email=email)
            hashed_password_value: UserHashPasswordValue = self._user_value_factory.create_hashed_password_value(
                hashed_password=hashed_password,
            )
            user_id_value: UserIdValue = self._user_value_factory.create_id_value(user_id=user_id)
            role_value: UserRole = self._user_value_factory.create_role_value(role=role)

        user = UserAggregate(
            id=user_id_value,
            full_name=fullname_value,
            email=email_value,
            hashed_password=hashed_password_value,
            role=role_value,
        )

        if not user_id:
            user.record_event(
                UserCreatedEvent(
                    user_id=user.id,
                    full_name=user.full_name,
                    email=user.email,
                    role=user.role,
                )
            )

        return user