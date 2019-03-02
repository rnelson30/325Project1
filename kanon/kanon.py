import csv
import sys
import numpy as np
import pandas as pd

df = pd.read_csv(sys.argv[1], sep="~")

print 'anonymity with Forwarded: ' + str(df.groupby(['Forwarded'], as_index=False).size().min())
print 'anonymity with Agent: ' + str(df.groupby(['Agent'], as_index=False).size().min())
#print 'anonymity with AcceptLanguage: ' + str(df.groupby(['AcceptLanguage'], as_index=False).size().min())
print 'anonymity with all: ' + str(df.groupby(['Forwarded', 'Agent'], as_index=False).size().min())
#print 'anonymity with all: ' + str(df.groupby(['Forwarded', 'Agent', 'AcceptLanguage'], as_index=False).size())
