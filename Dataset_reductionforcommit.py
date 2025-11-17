import pandas as pd

# Comets
comets = pd.read_csv("data/comets.csv")
comets.head(1000).to_csv("data/comets_sample.csv", index=False)

# Asteroids
asteroids = pd.read_csv("data/asteroids.csv")
asteroids.head(1000).to_csv("data/asteroids_sample.csv", index=False)

# Stars
stars = pd.read_csv("data/stars_gaia.csv")
stars.head(1000).to_csv("data/stars_gaia_sample.csv", index=False)

# Exoplanets
exo = pd.read_csv("data/exoplanets.csv")
exo.head(1000).to_csv("data/exoplanets_sample.csv", index=False)

# Black hole hosts
bh = pd.read_csv("data/blackholes_gaia.csv")
bh.head(1000).to_csv("data/blackholes_gaia_sample.csv", index=False)

print("Sample files created successfully!")
