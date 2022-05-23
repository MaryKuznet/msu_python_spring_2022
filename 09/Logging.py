import sys

import logging
import logging.config


log_config = {
    "version": 1,
    "formatters": {
        "simple": {
            "format": "%(levelname)s\t%(message)s",
        },
        "dated": {
            "format": "%(asctime)s\t%(levelname)s\t%(message)s",
        },
    },
    "handlers": {
        "stream_file": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "simple",
        },
        "custom_file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "cache.log",
            "formatter": "dated",
        },
    },
    "loggers": {
        "for_file": {
            "level": "INFO",
            "handlers": ["custom_file"],
        },
        "for_stream": {
            "level": "INFO",
            "handlers": ["stream_file"],
        },
    },
}


class LRUCache:

    def __init__(self, limit=42):
        # Храним ключ-значение
        self.cache = {}
        # Храним порядок
        self.priority = []
        # Храним максимальное количество значений
        self.limit = limit

        logging.config.dictConfig(log_config)
        if '-s' in sys.argv:
            self.logger = logging.getLogger("for_stream")
        else:
            self.logger = logging.getLogger("for_file")

    def get(self, key):
        if key not in self.cache:
            self.logger.warning("Request for a non-existent hatch")
            return None
        self.logger.info("Get value")
        self.priority.remove(key)
        self.priority.append(key)
        return self.cache[key]

    def set(self, key, value):
        self.logger.info("Add key-value")
        if key in self.cache:
            self.priority.remove(key)
            self.logger.info("Changing the value for an existing key")
        self.cache[key] = value
        self.priority.append(key)
        if len(self.priority) > self.limit:
            self.cache.pop(self.priority[0])
            self.priority.pop(0)
            self.logger.info("Limit exceeded, one item removed")


if __name__ == "__main__":
    cache = LRUCache(2)

    cache.set("k1", "val1")
    cache.set("k2", "val2")

    cache.get("k2")
    cache.get("k1")
    cache.get("k3")

    cache.set("k3", "val3")

    cache.get("k2")

    cache.set("k3", "new_val")
