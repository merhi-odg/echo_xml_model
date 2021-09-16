# modelop.schema.0: input_schema.avsc
# modelop.schema.1: output_schema.avsc

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level="INFO")


# modelop.init
def begin():
    pass

# modelop.score
def action(data):
    logger.info("type of data: %s", type(data))
    
    yield data
