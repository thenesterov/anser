import os
from pathlib import Path

import click

from anser.core.config import build_config
from anser.core.init import init_anser


@click.group()
def cli() -> None:
    return None


@cli.command(name='init')
@click.argument('path', required=False)
def init(path: str | None = None) -> None:
    init_anser(Path(os.path.abspath(path or os.getcwd())))
    return None


@cli.command(name='migration')
@click.option('--message', required=False)
@click.option('--config', required=False)
def migration(
    message: str | None = None,
    config: str | None = None,
) -> None:
    if config is None:
        config_path = Path(os.path.abspath(os.getcwd())) / 'anser.toml'
    else:
        config_path = Path(config)
    config = build_config(config_path)
    return None


@cli.command(name='migrate')
@click.argument('action')
def migrate(action) -> None:
    return None
