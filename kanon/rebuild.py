import csv
import sys
import pandas as pd

full = pd.read_csv(sys.argv[1], sep="~")
generalized = pd.read_csv(sys.argv[2], sep="~")

final = pd.DataFrame(columns=["Image", "Forwarded", "Agent"])
i = 0

for index, genRow in generalized.iterrows():
  while full.iloc[i + 1].AcceptLanguage == full.iloc[i].AcceptLanguage and\
    full.iloc[i + 1].Agent == full.iloc[i].Agent\
    and full.iloc[i + 1].Forwarded == full.iloc[i].Forwarded:
    final = final.append({"Image" : full.iloc[i].Image,\
      "Forwarded" : genRow.Forwarded,\
      "Agent" : genRow.Agent}, ignore_index=True)
    i = i + 1
  final = final.append({"Image" : full.iloc[i - 1].Image,\
    "Forwarded" : genRow.Forwarded,\
    "Agent" : genRow.Agent}, ignore_index=True)
  i = i + 1

final.to_csv("finalData.csv", sep="~")
