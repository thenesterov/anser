from hashlib import sha1
from typing import NewType


MigrationId = NewType('MigrationId', str)


def create_migration_id() -> MigrationId:
    migration_id = sha1().hexdigest()[:8]
    return MigrationId(migration_id)
