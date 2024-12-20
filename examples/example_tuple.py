from dataclasses import dataclass

from setconfig import load_config


@dataclass(frozen=True, slots=True)
class Server:
    domains: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class Location:
    coords: tuple


@dataclass(frozen=True, slots=True)
class Config:
    shape: tuple[int, int]
    server: Server
    locations: list[Location]


if __name__ == '__main__':
    config = load_config('config_tuple.yaml', into=Config)
    print(config.locations[0].coords)  # (38.897778, -77.036389)
    print(config)
