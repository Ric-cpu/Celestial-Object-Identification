import pandas as pd
from pathlib import Path

root = Path("data")
df = pd.read_csv(root / "small_bodies.csv")


#Anything with a comet-style prefix goes into comet set
comet_mask = df["full_name"].str.contains(r"\b[CDPXI]/|\bI\s", case=False, na=False)

comets = df[comet_mask].copy()
asteroids = df[~comet_mask].copy()

comets.to_csv(root / "comets.csv", index=False)
asteroids.to_csv(root / "asteroids.csv", index=False)

print(f"comets:{len(comets)}, asteroids:{len(asteroids)}")