import csv
import sys
import numpy as np
import pandas as pd
import netaddr

def anonAgent(agent):
  if "Mac" in agent:
    return "Mac"
  elif "iPhone" in agent:
    return "iPhone"
  elif "iPod" in agent:
    return "iPod"
  elif "Windows Phone" in agent:
    return "Windows Phone"
  elif "Linux" in agent:
    return "Linux"
  elif "Android" in agent:
    return "Android"
  elif "Windows" in agent:
    return "Windows"
  else:
    return "Other"

def generalize(row):
  row.Forwarded = netaddr.IPNetwork(row.Forwarded + "/2").cidr
  row.Agent = anonAgent(row.Agent)
  return row

df = pd.read_csv(sys.argv[1], sep="~")
df = df.apply(generalize, axis=1)
df = df.drop("AcceptLanguage", axis=1)

df.to_csv("generalized.csv", sep="~")
