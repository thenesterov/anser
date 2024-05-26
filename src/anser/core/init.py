from pathlib import Path

from src.anser.core.exceptions import DirectoryExistsException, FileExistsException
from src.anser.core.schemas import CONFIG_SCHEMA, SETUP_FILE_SCHEMA, TEMPLATE_SCHEMA


def create_config(path: Path) -> None:
    config_path = path / 'anser.toml'
    if config_path.exists():
        raise FileExistsException(config_path)
    
    with config_path.open('x') as file:
        file.write(
            CONFIG_SCHEMA.format(
                path_to_migrations=path / 'migrations',
            ),
        )
    return None


def create_template_j2(path: Path) -> None:
    template_j2_path = path / 'template.j2'
    if template_j2_path.exists():
        raise FileExistsException(template_j2_path)
    
    with template_j2_path.open('x') as template:
        template.write(TEMPLATE_SCHEMA)
    return None


def create_setup_file(path: Path) -> None:
    setup_file_path = path / 'setup.py'
    if setup_file_path.exists():
        raise FileExistsException(setup_file_path)
    
    with setup_file_path.open('x') as template:
        template.write(SETUP_FILE_SCHEMA)
    return None


def create_migrations_directory(path: Path) -> None:
    migrations_path = path / 'migrations'
    if migrations_path.exists():
        raise DirectoryExistsException(migrations_path)
    
    migrations_init_path = migrations_path / '__init__.py'
    if migrations_path.exists():
        raise FileExistsException(migrations_path)
    
    migrations_path.mkdir()
    with open(migrations_init_path, 'x') as template:
        pass
    return None


def init_anser(path: Path) -> None:
    anser_path = path / 'anser'
    if anser_path.exists():
        raise DirectoryExistsException(anser_path)
    anser_path.mkdir()
    
    create_config(path)
    create_template_j2(anser_path)
    create_setup_file(anser_path)
    create_migrations_directory(anser_path)
