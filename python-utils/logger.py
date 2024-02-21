import logging

def setup_logger(name, log_file):
    """Function to setup logging to a file with the module name in the log message format"""
    formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger

# Example usage:
logger = setup_logger('example_logger', 'example.log')
logger.info('This is an information message.')
logger.warning('This is a warning message.')