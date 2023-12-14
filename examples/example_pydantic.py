from pydantic import BaseModel, field_validator

from setconfig import load_config


class Connector(BaseModel):
    title: str
    parallel: bool


class NodeConfig(BaseModel):
    host: str
    port: int

    @field_validator('port')
    def check_port(cls, port: int) -> int:
        assert 0 < port < 65535
        return port


class Location(BaseModel):
    x: int
    y: int


class Config(BaseModel):
    timeout: float
    connector: Connector
    nodes: list[NodeConfig]
    matrix: list[list[Location]]


if __name__ == '__main__':
    config = load_config('example.yaml', into=Config)
    print(config.nodes[0].host)  # 1.1.1.1
    print(config)
