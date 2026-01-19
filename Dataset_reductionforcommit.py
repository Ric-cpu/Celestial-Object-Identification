import pandas as pd

# Comets
comets = pd.read_csv("data/full/comets.csv")
comets.head(1000).to_csv("data/comets_sample.csv", index=False)

# Asteroids
asteroids = pd.read_csv("data/full/asteroids.csv")
asteroids.head(1000).to_csv("data/asteroids_sample.csv", index=False)

# Stars
stars = pd.read_csv("data/full/stars_gaia.csv")
stars.head(1000).to_csv("data/stars_gaia_sample.csv", index=False)

# Exoplanets
exo = pd.read_csv("data/full/exoplanets.csv")
exo.head(1000).to_csv("data/exoplanets_sample.csv", index=False)

# Quasars / AGN
quasars = pd.read_csv("data/full/quasars_gaia.csv")
quasars.head(1000).to_csv("data/quasars_gaia_sample.csv", index=False)

print("Sample files created successfully!")
