from CloudWatchUtil import CustomMetricSender
import numpy as np

def main():
    shortlist = np.random.randn(5)
    sender = CustomMetricSender('ExperimentalCustom', 'TpltestTimings')
    res = sender.senddata(shortlist)
    print shortlist
    print res





if __name__ == "__main__":
    main()
