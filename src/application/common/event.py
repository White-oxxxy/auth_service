from datetime import (
    datetime,
    timezone,
)
from msgspec import (
    Struct,
    field,
)
from uuid_utils.compat import (
    UUID,
    uuid7,
)


class BaseIntegrationEvent(
    Struct,
    frozen=True,
):
    event_id: UUID = field(default_factory=uuid7)
    accurate_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))