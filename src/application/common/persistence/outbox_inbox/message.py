from dataclasses import dataclass
from datetime import (
    datetime,
    timezone,
)
from enum import Enum
from uuid_utils import UUID

from application.common.event import BaseIntegrationEvent


class MessageStatus(str, Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    PROCESSED = "PROCESSED"
    FAILED = "FAILED"


@dataclass
class Message:
    id: UUID
    event: BaseIntegrationEvent
    status: MessageStatus = MessageStatus.PENDING
    sender: str | None = None
    created_at: datetime = datetime.now(timezone.utc)
    updated_at: datetime = datetime.now(timezone.utc)

    def mark_as_processing(self):
        self.status = MessageStatus.PROCESSING
        self.updated_at = datetime.now()

    def mark_as_processed(self):
        self.status = MessageStatus.PROCESSED
        self.updated_at = datetime.now()

    def mark_as_failed(self):
        self.status = MessageStatus.FAILED
        self.updated_at = datetime.now()


