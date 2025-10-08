from abc import ABC
from dataclasses import dataclass


@dataclass
class IBaseValuesFactory(ABC):
    ...


@dataclass
class IBaseEntityFactory(ABC):
    ...