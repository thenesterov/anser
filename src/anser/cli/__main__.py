import os
from pathlib import Path
from typing import Any

import click

from anser.core.config import build_config
from anser.core.init import InitAnser


@click.group()
def cli() -> None:
    return None


@cli.command(name='init')
@click.argument('path', required=False)
def init(path: str | None = None) -> None:
    path_ = Path(os.path.abspath(path or os.getcwd()))
    init_anser = InitAnser(path_)
    init_anser.execute()


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
    config_ = build_config(config_path)
    return None


@cli.command(name='migrate')
@click.argument('action')
def migrate(action: Any) -> None:
    return None
