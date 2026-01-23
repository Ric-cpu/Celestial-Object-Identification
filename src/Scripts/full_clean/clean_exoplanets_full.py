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


REQUIRED_COLS = [
    "rowid", "pl_name", "hostname", "pl_letter", "gaia_id",
    "discoverymethod", "disc_year",
    "pl_orbper", "pl_orbsmax",
    "st_teff", "st_rad", "st_mass",
    "ra", "dec", "sy_dist", "sy_plx",
]

OPTIONAL_RENAMES = {
    "sy_pmra": "pmra",
    "sy_pmdec": "pmdec",
    "sy_gaiamag": "phot_g_mean_mag",  # <-- this is the one you actually have
    "sy_gmag": "phot_g_mean_mag",     # optional fallback
}




def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[3]
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
    #renaming gaiaID to gaia_id for consistency
    if "gaiaID" in df.columns:
        df = df.rename(columns={"gaiaID": "gaia_id"})
    # Select the lean column set that is present in the full export.
       # Select the lean column set that is present in the full export.
    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    if missing:
        raise SystemExit(f"Missing expected columns in {args.input}: {missing}")

    # Start with required columns, then add optional Gaia-like columns if available.
    keep_cols = REQUIRED_COLS.copy()
    for raw_col, out_col in OPTIONAL_RENAMES.items():
        if raw_col in df.columns:
            df[out_col] = pd.to_numeric(df[raw_col], errors="coerce")
            if out_col not in keep_cols:
                keep_cols.append(out_col)
    print("raw optional cols present:", [c for c in OPTIONAL_RENAMES if c in df.columns])
    print("keep_cols:", keep_cols)
    print("output:", args.output)


    # If bp_rp is missing but BP/RP mags exist, derive it.
    if "bp_rp" not in df.columns and {"sy_bpmag", "sy_rpmag"}.issubset(df.columns):
        bp = pd.to_numeric(df["sy_bpmag"], errors="coerce")
        rp = pd.to_numeric(df["sy_rpmag"], errors="coerce")
        df["bp_rp"] = bp - rp
        if "bp_rp" not in keep_cols:
            keep_cols.append("bp_rp")

    df = df[keep_cols].copy()

    # Median-impute moderate numeric gaps.
    numeric_cols = [
        "pl_orbper", "pl_orbsmax", "st_teff", "st_rad", "st_mass",
        "sy_dist", "sy_plx", "pmra", "pmdec", "phot_g_mean_mag", "bp_rp",
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
            df[col] = df[col].fillna(df[col].median())
  
    df = df.dropna()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.output, index=False)
    print(f"Wrote {args.output} with cols={df.shape[1]} rows={len(df)}")

if __name__ == "__main__":
    main()
