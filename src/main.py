import json, logging
from multiprocessing import Queue

# updatable settings
class ConfigLoader:
    def __init__(self, config_path):
        self.config_path = config_path
        self.load_config()

    def load_config(self):
        with open(self.config_path, "r") as file:
            self.config = json.load(file)

        # debug/logger
        self.debug = self.config['config']['debug']
        self.format = self.config['config']['log_format']
        self.log_path = self.config['config']['log_path']

    def reload_config(self):
        self.load_config()

        pass
        
        return True

config_path = ''
config = ConfigLoader(config_path)

# logger
logger = logging.getLogger(__name__)
formatter = logging.Formatter(config.format, datefmt="%m-%d %H:%M:%S")
file_handler = logging.FileHandler(config.log_path, encoding='utf-8')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.DEBUG if config.debug is True else logging.INFO)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

# queue logging system
class QueueHandler(logging.Handler):
    def __init__(self, log_queue):
        super().__init__()
        self.log_queue = log_queue

    def emit(self, record):
        self.log_queue.put(record)

log_queue = Queue()
queue_handler = QueueHandler(log_queue)
queue_handler.setFormatter(formatter)
logger.addHandler(queue_handler)

if __name__ == '__main__':
    pass