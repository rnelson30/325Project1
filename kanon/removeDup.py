import csv
import numpy as np
import pandas as pd

df = pd.read_csv("trimmedLog.csv", sep="~").drop("Image", axis=1)
df = df.loc[(df.Forwarded != df.Forwarded.shift()) | (df.Agent != df.Agent.shift()) | (df.AcceptLanguage != df.AcceptLanguage.shift())]
df.to_csv("trimmedNoDup.csv", sep="~")
