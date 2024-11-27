import logging


# setup logging
logging.basicConfig(format="%(levelname)-6s- %(asctime)s -  %(message)s", level=logging.ERROR)

logger = logging.getLogger('webhook-bot')
logger.setLevel(logging.INFO)
