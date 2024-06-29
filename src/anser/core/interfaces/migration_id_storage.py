from abc import abstractmethod
from typing import Protocol
from uuid import UUID


class MigrationIdStorage(Protocol):
    @abstractmethod
    def create(self) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def get_migration_id(self) -> UUID | None:
        raise NotImplementedError
    
    @abstractmethod
    def set_migration_id(self, current_uuid: UUID) -> None:
        raise NotImplementedError
