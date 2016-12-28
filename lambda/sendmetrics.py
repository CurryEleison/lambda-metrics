from CloudWatchUtil import CustomMetricSender
import numpy as np
from datetime import datetime
import dateutil.parser


def main():
    # shortlist = np.random.randn(5)
    sender = CustomMetricSender('ExperimentalCustom', 'TpltestTimings')
    currenttime = datetime.now()
    sender.senddataaggregate(datatime = dateutil.parser.parse("2016-12-28T13:42:00.00Z"), datamin =  0.054696, datamax = 0.058849, datasum = 0.113545, datalength = 2.0)
    # res = sender.senddatalist(shortlist)
    # print shortlist
    # print res





if __name__ == "__main__":
    main()
