from abc import ABC
from dataclasses import (
    dataclass,
    field,
)
from datetime import datetime
from uuid_utils.compat import (
    UUID,
    uuid7,
)

@dataclass(frozen=True)
class BaseDomainEvent(ABC):
    uid: UUID = field(kw_only=True, default_factory=uuid7)
    timestamp: datetime = field(kw_only=True, default_factory=datetime.utcnow)