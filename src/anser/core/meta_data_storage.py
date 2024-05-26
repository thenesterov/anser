from abc import abstractmethod
from typing import Protocol
from uuid import UUID


class AnserMetaDataStorage(Protocol):
    @abstractmethod
    def create(self) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def get_current_uuid(self) -> UUID | None:
        raise NotImplementedError
    
    @abstractmethod
    def set_current_uuid(self, current_uuid: UUID) -> None:
        raise NotImplementedError
