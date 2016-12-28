from CloudWatchUtil import CustomMetricSender
import numpy as np
import random
import logging
import boto3

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def send_random():
    random.seed()
    #a1 = random.randint(0,5)
    #a2 = random.randint(0,5)
    #a3 = random.randint(0,5)
    data = np.random.randn(5)
    sender = CustomMetricSender('ExperimentalCustom', 'TpltestTimings')
    res = sender.senddatalist(data)
    logging.info(data)

