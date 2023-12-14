from examples.example_dataclass import Config
from setconfig import load_config

if __name__ == '__main__':
    config = load_config('example.yaml', into=Config, override={'timeout': 10})
    print(config.timeout)
    print(config)
