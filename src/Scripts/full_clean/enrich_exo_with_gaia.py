import pandas as pd

stars = pd.read_csv("data/full/stars_gaia_clean.csv")
quasars = pd.read_csv("data/full/quasars_gaia_clean.csv")
exo = pd.read_csv("data/full/exoplanets_gaia_enriched.csv")

# align column names if needed
if "sy_plx" in exo.columns:
    exo = exo.rename(columns={"sy_plx": "parallax"})

features = ["ra", "dec", "parallax", "pmra", "pmdec", "phot_g_mean_mag", "bp_rp"]

stars = stars[features].assign(label="star")
quasars = quasars[features].assign(label="quasar")
exo = exo[features].assign(label="exo_host")

# balance classes
n = min(len(stars), len(quasars), len(exo))
stars = stars.sample(n=n, random_state=42)
quasars = quasars.sample(n=n, random_state=42)
exo = exo.sample(n=n, random_state=42)

df = pd.concat([stars, quasars, exo], ignore_index=True)
X = df[features].values
y = df["label"].values
