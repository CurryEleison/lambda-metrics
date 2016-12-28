import boto3
import numpy as np
import logging
import pandas as pd
import datetime
from AwsElbLogUtil import LogDataFrame
from CloudWatchUtil import CustomMetricSender

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



def send_random(event, context):
    data = np.random.randn(5)
    logging.info(data)


def send_metrics_tpltest(event, context):
    objlist = []
    
    client = boto3.resource('s3')
    for record in event['Records']:
        objlist.append(
                client.ObjectSummary(
                    record['s3']['bucket']['name'], 
                    record['s3']['object']['key']
                    )
                )
        # bucket = record['s3']['bucket']['name']
        # keds.append(record['s3']['object']['key'])
        #download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
        #s3_client.download_file(bucket, key, download_path)
    dfmaker = LogDataFrame(client)
    for s3objsummary in objlist:
        logging.info(s3objsummary.key)
    df = dfmaker.make_dataframe(objlist, lambda l: hasattr(l, 'path') and l.path.startswith('/tpltest'))
    # urltimetaken = df[['path', 'servertime']].groupby('path').sum().sort_values('servertime', ascending=False) #.agg({'servertime', 'sum'})
    # print urltimetaken.head(10)
    df['roundedtime'] = df['utctime'].apply(lambda dt: datetime.datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute))                                                                                        
    df = df.assign(mintime = df.servertime).assign(maxtime = df.servertime).assign(sumtime = df.servertime).assign(reccount = df.method)                                                                        
    summary = df.groupby('roundedtime').agg(                                                                
            {                                                                                           
                'maxtime': 'max',                                                                       
                'mintime': 'min',                                                                       
                'sumtime': 'sum',                                                                       
                'reccount': 'count'                                                                     
                }                                                                                       
            )  
    sender = CustomMetricSender('ExperimentalCustom', 'TpltestTimings')
    for index, item in summary.iterrows():
        logging.info("At {4} Min: {0}, Max: {1}, Sum: {2}, Count: {3}".format(item['mintime'], item['maxtime'], item['sumtime'], item['reccount'], index))
        resp = sender.senddataaggregate(datatime = index, datalength = item['reccount'],
                datasum = item['sumtime'], datamin = item['mintime'], datamax = item['maxtime'])
        logging.info(resp)

