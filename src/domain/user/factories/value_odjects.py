from uuid_utils import UUID

from domain.common.factory import IBaseValuesFactory
from domain.user.enums import UserRole
from domain.user.value_objects import (
    UserEmailValue,
    UserSurnameValue,
    UserLastnameValue,
    UserNameValue,
    UserFullNameValue,
    UserHashPasswordValue,
    UserRawPasswordValue,
    UserIdValue,
)


class UserValueFactory(IBaseValuesFactory):
    @staticmethod
    def create_id_value(user_id: UUID) -> UserIdValue:
        value = UserIdValue(value=user_id)

        return value

    @staticmethod
    def create_email_value(email: str) -> UserEmailValue:
        value = UserEmailValue(value=email)

        return value

    @staticmethod
    def create_role_value(role: str) -> UserRole:
        value = UserRole(role)

        return value

    @staticmethod
    def create_raw_password_value(raw_password: str) -> UserRawPasswordValue:
        value = UserRawPasswordValue(value=raw_password)

        return value

    @staticmethod
    def create_hashed_password_value(hashed_password: bytes) -> UserHashPasswordValue:
        value = UserHashPasswordValue(value=hashed_password)

        return value

    @staticmethod
    def create_name_value(name: str) -> UserNameValue:
        value = UserNameValue(value=name)

        return value

    @staticmethod
    def create_surname_value(surname: str) -> UserSurnameValue:
        value = UserSurnameValue(value=surname)

        return value

    @staticmethod
    def create_lastname_value(lastname: str) -> UserLastnameValue:
        value = UserLastnameValue(value=lastname)

        return value

    def create_fullname_value(
        self,
        name: str,
        surname: str,
        lastname: str,
    ) -> UserFullNameValue:
        name_value: UserNameValue = self.create_name_value(name=name)
        surname_value: UserSurnameValue = self.create_surname_value(surname=surname)
        lastname_value: UserLastnameValue = self.create_lastname_value(lastname=lastname)

        value = UserFullNameValue(
            name=name_value,
            surname=surname_value,
            last_name=lastname_value,
        )

        return value