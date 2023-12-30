from main import logger

import traceback

def x():
    try:
        pass
    except Exception as e:
        line_number = (traceback.extract_tb(e.__traceback__))[-1][1]
        logger.error(f'{type(e).__name__} occured on line {line_number}: {e}')