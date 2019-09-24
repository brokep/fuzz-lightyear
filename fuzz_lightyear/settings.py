import random
from functools import lru_cache

from hypothesis import core


class Settings:
    def __init__(self) -> None:
        self.seed = random.getrandbits(128)    # type: int

    @property
    def seed(self) -> int:
        return self._seed

    @seed.setter
    def seed(self, value: int) -> None:
        self._seed = value
        core.global_force_seed = value      # type: ignore
        random.seed(value)


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
