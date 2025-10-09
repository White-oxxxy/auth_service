from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from typing import (
    Generic,
    TypeVar,
)
from uuid_utils import UUID

from application.common.persistence.reader.reader_models import BaseReaderModel


ReaderModel = TypeVar("ReaderModel", bound=BaseReaderModel)


@dataclass
class BaseReader(
    Generic[ReaderModel],
    ABC,
):
    @abstractmethod
    async def find_by_id(self, required_id: UUID) -> ReaderModel | None: ...