import pandas as pd

keep = [
    # IDs/basic
    "rowid","pl_name","hostname","pl_letter",
    # planet features
    "discoverymethod","disc_year","pl_orbper","pl_orbsmax","pl_rade","pl_radj","pl_masse","pl_massj",
    # star/system features
    "st_spectype","st_teff","st_rad","st_mass","sy_dist","sy_plx","ra","dec"
]

df = pd.read_csv("data/exoplanets_sample.csv", usecols=lambda c: c in keep)
df.to_csv("data/exoplanets_trimmed.csv", index=False)
print(df.head(), df.columns)
