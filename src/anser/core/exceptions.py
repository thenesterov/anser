from pathlib import Path


class AnserException(Exception):
    pass


class DirectoryExistsException(AnserException):
    def __init__(self, path: Path) -> None:
        super().__init__(
            'Directory exists %r' % path
        )


class FileExistsException(AnserException):
    def __init__(self, path: Path) -> None:
        super().__init__(
            'File exists %r' % path
        )
