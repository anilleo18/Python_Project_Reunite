import logging
import inspect


def getcustomLogger(level):
    logger_name = inspect.stack()[1][3]

    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    fileHandler = logging.FileHandler('test.log', mode='w')
    fileHandler.setLevel(level)
    formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s : %(message)s', datefmt='%m/%d/%Y  %I:%M:%S %P')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger
