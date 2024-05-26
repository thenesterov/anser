from pathlib import Path


class AnserException(Exception):
    pass


class DirectoryExistsException(AnserException):
    def __init__(self, path: Path) -> None:
        super().__init__(
            f'Directory exists {repr(path)}'
        )


class FileExistsException(AnserException):
    def __init__(self, path: Path) -> None:
        super().__init__(
            f'File exists {repr(path)}'
        )
