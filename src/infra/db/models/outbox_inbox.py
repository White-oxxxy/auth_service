from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from sqlalchemy.sql.sqltypes import (
    Enum,
    JSON,
)
from uuid_utils import UUID

from infra.db.models.base import TimedBaseModel
from application.common.persistence.outbox_inbox.message import MessageStatus


class OutboxMessageModel(TimedBaseModel):
    __tablename__ = "outbox"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    event_type: Mapped[str] = mapped_column(nullable=False)
    event_data: Mapped[JSON] = mapped_column(nullable=False)
    aggregate_id: Mapped[UUID] = mapped_column(nullable=False)
    aggregate_type: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(
        Enum(
            MessageStatus,
            name="messagestatus",
        ),
        default=MessageStatus.PENDING,
        nullable=False
    )


class InboxMessageModel(TimedBaseModel):
    __tablename__ = "inbox"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    event_type: Mapped[str] = mapped_column(nullable=False)
    event_data: Mapped[JSON] = mapped_column(nullable=False)
    aggregate_id: Mapped[UUID] = mapped_column(nullable=False)
    aggregate_type: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(
        Enum(
            MessageStatus,
            name="messagestatus",
        ),
        default=MessageStatus.PENDING,
        nullable=False
    )