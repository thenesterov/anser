from anser.core.config import AnserConfig
from anser.core.meta_data_storage import AnserMetaDataStorage


class AnserMigration:
    def __init__(
        self,
        config: AnserConfig,
        meta_data_storage: AnserMetaDataStorage,
    ) -> None:
        self._config = config
        self._meta_data_storage = meta_data_storage
    
    def execute(self) -> None:
        current_uuid = self._meta_data_storage.get_current_uuid()
        path_to_migrations = self._config.migrations.path
