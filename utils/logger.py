import logging

def setup_logger():
    logger = logging.getLogger("arkbot")
    file_handler = logging.FileHandler("arkbot.log")
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    return logger
