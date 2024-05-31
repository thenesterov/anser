from dataclasses import dataclass
from pathlib import Path

import tomli


@dataclass(frozen=True)
class AnserMigrationsConfig:
    path: Path


@dataclass(frozen=True)
class AnserConfig:
    url: str
    migrations: AnserMigrationsConfig


def build_config(path: Path) -> AnserConfig:
    with open(path, 'rb') as file:
        toml_config = tomli.load(file)['anser']
    
    toml_migrations = toml_config['migrations']
    migrations = AnserMigrationsConfig(
        path=Path(toml_migrations['path'])
    )
    return AnserConfig(
        url=toml_config['url'],
        migrations=migrations,
    )
