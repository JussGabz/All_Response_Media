import logging

import json_log_formatter


def get_logger(name):
    formatter = json_log_formatter.JSONFormatter()

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)

    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    return logger
