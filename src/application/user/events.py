from uuid_utils import UUID

from application.common.event import BaseIntegrationEvent


class UserCreatedIntegrationEvent(
    BaseIntegrationEvent,
    frozen=True,
):
    user_id: UUID
