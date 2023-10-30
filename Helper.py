import numpy as np

import pandas as pd

def counter(data):
  result = {}

  for i in data:
    for t in i.split(" "):
      if t in result.keys():
        result[t] += 1
      else:
        result[t] = 1

  return result

def filmer(data):

    title = []
    tahun = []

    replacer = {"Sci-Fi":"SciFi", "Film-Noir":"Filnoir", "|":" "}

    for t in data.iloc[:, 1]:
        split = t.split(" ")
        if len(split) == 1:
            title.append(split[0])
            tahun.append(np.nan)
        else:
            title.append(" ".join(split[:-1]))
            tahun.append(split[-1:][0][1:5])

    for i, t in replacer.items():
        data["Genre"] = data["Genre"].str.replace(i, t)

    data["Title"] = title
    data["Tahun"] = tahun

    data = data.fillna("2016")

    return data
