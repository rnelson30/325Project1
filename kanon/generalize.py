import csv
import sys
import numpy as np
import pandas as pd
import netaddr

#topTenLangs = {"zh", "en", "hi", "es", "ar", "ms", "ru", "bn", "pt", "fr"}
#mostCommon = {"si", "mt"}#"lo", "tn", "kr", "fo", "yo", "te", "se", "ks"}
#"hu", "et", "bn", "ay", "as", "vi", "om", "es", "ca", "af", "wo", "tg", \
#"ss", "sq", "sl", "ro", "pa", "or", "nn", "ms", "mn", "lu", "li", "kv"}
#"kl", "it", "gd", "eu", "dv", "da", "ty", "tw", "tt", "sv", "sh", "ru", \
#"ps", "no", "ng", "ne", "nd", "my", "mr", "mo", "lt", "ln", "kn", "kj", \
#"ki", "io", "ht", "fy", "fj", "ee", "cv", "ce", "br", "be", "ar", "am"}

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

#def anonAcceptLang(lang):
#  if len(lang) != 2:
#    lang = lang[:2]
#  if lang not in mostCommon:
#    lang = "other"
#  return lang

def generalize(row):
  row.Forwarded = netaddr.IPNetwork(row.Forwarded + "/2").cidr
  row.Agent = anonAgent(row.Agent)
  #row.AcceptLanguage = anonAcceptLang(row.AcceptLanguage)
  return row

df = pd.read_csv(sys.argv[1], sep="~")
df = df.apply(generalize, axis=1)
df = df.drop("AcceptLanguage", axis=1)

df.to_csv("generalized.csv", sep="~")
