import csv
import numpy as np
import pandas as pd

table = pd.read_csv("logFile.csv", sep="~")
table = table.drop(["RemoteAddr", "Time", "Connection", "DNT", "Host", "UpgradeInsecureRequest", "Accept", "AcceptEncoding"], axis=1)
table.to_csv("trimmedLog.csv", sep="~")
