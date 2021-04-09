import fire
from src.producer import run_infinite_generator
from src.consumer import run_listener


def consumer(bootstrap_server, topic):
    run_listener(bootstrap_server, topic)


def producer(bootstrap_server, topic):
    run_infinite_generator(bootstrap_server, topic)


if __name__ == '__main__':
    fire.Fire()
