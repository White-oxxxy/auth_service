from dataclasses import dataclass
from uuid_utils import UUID

from application.common.persistence.reader.reader_models import BaseReaderModel

from domain.user.enums import UserRole


@dataclass(
    frozen=True,
    slots=True,
)
class UserReaderModel(BaseReaderModel):
    id: UUID
    username: str
    role: UserRole
    is_active: bool