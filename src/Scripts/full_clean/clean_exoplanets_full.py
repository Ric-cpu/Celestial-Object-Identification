"""
Trim and clean the full exoplanet catalog from `data/full/exoplanets.csv`.

Steps
- Read the raw NASA export, skipping the leading comment lines.
- Keep a lean set of useful columns (orbital, stellar, coordinates/distances).
- Median-impute moderate numeric gaps and drop any remaining NaNs.
- Write the cleaned file to `data/full/exoplanets_clean.csv`.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


KEEP_COLS = [
    # IDs / metadata
    "rowid",
    "pl_name",
    "hostname",
    "pl_letter",
    "discoverymethod",
    "disc_year",
    # Planet orbit
    "pl_orbper",
    "pl_orbsmax",
    # Host star parameters
    "st_teff",
    "st_rad",
    "st_mass",
    # Coordinates / distance
    "ra",
    "dec",
    "sy_dist",
    "sy_plx",
]


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description="Clean the full exoplanet catalog")
    parser.add_argument(
        "--input",
        type=Path,
        default=repo_root / "data/full/exoplanets.csv",
        help="Path to the raw exoplanet CSV",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=repo_root / "data/full/exoplanets_clean.csv",
        help="Destination for the cleaned CSV",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    # Skip leading comment lines with `comment="#"`.
    df = pd.read_csv(args.input, comment="#")

    # Select the lean column set that is present in the full export.
    missing = [c for c in KEEP_COLS if c not in df.columns]
    if missing:
        raise SystemExit(f"Missing expected columns in {args.input}: {missing}")

    df = df[KEEP_COLS].copy()

    # Median-impute moderate numeric gaps.
    for col in ["pl_orbper", "pl_orbsmax", "st_teff", "st_rad", "st_mass", "sy_dist", "sy_plx"]:
        df[col] = df[col].astype(float)
        df[col] = df[col].fillna(df[col].median())

    # Drop any remaining rows with NaNs in the kept columns.
    df = df.dropna()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.output, index=False)

    print(f"Cleaned exoplanet catalog written to {args.output} (rows={len(df)}, cols={df.shape[1]})")


if __name__ == "__main__":
    main()
