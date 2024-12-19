from dataclasses import dataclass

from example_dataclass import NodeConfig, Location
from setconfig import load_config


@dataclass(frozen=True, slots=True)
class Connector:
    title: str
    parallel: bool
    ssl: bool


@dataclass(frozen=True, slots=True)
class Extra:
    stage: str


@dataclass(frozen=True, slots=True)
class Config:
    timeout: float
    connector: Connector
    nodes: list[NodeConfig]
    matrix: list[list[Location]]
    extra: Extra


if __name__ == '__main__':
    config = load_config('example.yaml', 'example.modified.yaml', into=Config)
    print(config.extra)  # Extra(stage='dev')
    print(config)
