import numpy as np

import pandas as pd

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

def ind_titler(i):
    return film_df.iloc[i, 1]

def title_ind(t):
    return film_df[film_df["Title"] == t].index[0]
