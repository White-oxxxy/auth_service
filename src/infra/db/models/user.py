from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from sqlalchemy.sql.sqltypes import (
    Enum,
    LargeBinary,
)
from uuid_utils import UUID

from domain.user.enums import UserRole
from infra.db.models.base import TimedBaseModel


class UserModel(TimedBaseModel):
    __tablename__ = "user"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        unique=True,
        nullable=False,
    )
    first_name: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[bytes] = mapped_column(
        LargeBinary,
        nullable=False,
    )
    role: Mapped[str] = mapped_column(
        Enum(
            UserRole,
            name="userrole",
        ),
        default=UserRole.USER,
        nullable=False,
    )
    is_active: Mapped[bool] = mapped_column(
        default=True,
        nullable=False,
    )