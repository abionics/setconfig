from setconfig import load_config

if __name__ == '__main__':
    config = load_config('config.yaml')
    print(config.nodes[0].host)  # 1.1.1.1
    print(config)
