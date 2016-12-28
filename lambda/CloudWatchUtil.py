import boto3
from datetime import tzinfo, datetime, timedelta
from AwsElbLogUtil import UTC



class CustomMetricSender:
    """CustomMetricSender"""

    def __init__(self, namespace, metricname, region = u'eu-west-1'):
        self.namespace = namespace
        self.metricname = metricname
        self.region = region

    def senddatalist(self, datalist, timestamp=None):
        utc = UTC()
        datatime = timestamp if timestamp != None else datetime.now(utc)
        datasum = sum(datalist)
        datamax = max(datalist)
        datamin = min(datalist)
        datalength = len(datalist)
        return self.senddataaggregate(datatime, datalength, datasum, datamin, datamax)

    def senddataaggregate(self, datatime, datalength, datasum, datamin, datamax):
        metricdata = [
                        {
                        'MetricName': self.metricname,
                        'Timestamp': datatime,
                        'StatisticValues': {
                            'SampleCount': int(datalength), 
                            'Sum': datasum, 
                            'Minimum': datamin,
                            'Maximum': datamax
                        },
                        'Unit': 'Seconds'
                        }
                ]

        client = boto3.client('cloudwatch', region_name = self.region)
        response = client.put_metric_data(
                Namespace = self.namespace,
                MetricData = metricdata
                )
        return response

