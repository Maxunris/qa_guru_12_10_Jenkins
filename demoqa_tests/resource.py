from pathlib import Path


def path_photo(file_name):
    return str(
        Path(__file__).parent.parent.joinpath(f'tests/resources/{file_name}').absolute()
    )