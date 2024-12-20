from dataclasses import dataclass

from example_dataclass import Connector, NodeConfig, Location, Config
from setconfig import load_config


@dataclass(frozen=True, slots=True)
class ConnectorV2(Connector):
    ssl: bool


@dataclass(frozen=True, slots=True)
class Extra:
    stage: str


@dataclass(frozen=True, slots=True)
class ConfigV2(Config):
    connector: ConnectorV2
    extra: Extra


if __name__ == '__main__':
    config = load_config('config.yaml', 'config.extra.yaml', into=ConfigV2)
    print(config.extra)  # Extra(stage='dev')
    print(config)
