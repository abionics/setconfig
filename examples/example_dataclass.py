from dataclasses import dataclass

from setconfig import load_config


@dataclass(frozen=True, slots=True)
class Connector:
    title: str
    parallel: bool


@dataclass(frozen=True, slots=True)
class NodeConfig:
    host: str
    port: int

    def __post_init__(self):
        assert 0 < self.port < 65535


@dataclass(frozen=True, slots=True)
class Location:
    x: int
    y: int


@dataclass(frozen=True, slots=True)
class Config:
    timeout: float
    connector: Connector
    nodes: list[NodeConfig]
    matrix: list[list[Location]]


if __name__ == '__main__':
    config = load_config('config.yaml', into=Config)
    print(config.nodes[0].host)  # 1.1.1.1
    print(config)
