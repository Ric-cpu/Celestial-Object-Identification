"""
Clean the full stars and blackholes Gaia catalogs.

Steps:
- Read the raw CSVs from data/full.
- Keep a shared Gaia feature set.
- Median-impute small numeric gaps.
- Optionally drop quasar_probability if you want to avoid leakage (kept here; comment to drop).
- Write cleaned CSVs to data/full/*_clean.csv.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


STAR_FEATURES = [
    "source_id",
    "ra",
    "dec",
    "parallax",
    "pmra",
    "pmdec",
    "phot_g_mean_mag",
    "bp_rp",
]

# Blackholes have a superset; align to these plus ruwe/quasar_probability if present
BH_EXTRA = ["ruwe", "quasar_probability"]


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description="Clean stars and blackholes Gaia catalogs")
    parser.add_argument(
        "--stars-input",
        type=Path,
        default=repo_root / "data/full/stars_gaia.csv",
        help="Path to raw stars Gaia CSV",
    )
    parser.add_argument(
        "--bh-input",
        type=Path,
        default=repo_root / "data/full/blackholes_gaia.csv",
        help="Path to raw blackholes Gaia CSV",
    )
    parser.add_argument(
        "--stars-output",
        type=Path,
        default=repo_root / "data/full/stars_gaia_clean.csv",
        help="Path to cleaned stars CSV",
    )
    parser.add_argument(
        "--bh-output",
        type=Path,
        default=repo_root / "data/full/blackholes_gaia_clean.csv",
        help="Path to cleaned blackholes CSV",
    )
    return parser.parse_args()


def clean_stars(df: pd.DataFrame) -> pd.DataFrame:
    df = df[STAR_FEATURES].copy()
    for col in ["parallax", "pmra", "pmdec", "phot_g_mean_mag", "bp_rp"]:
        df[col] = df[col].astype(float)
        df[col] = df[col].fillna(df[col].median())
    return df.dropna()


def clean_blackholes(df: pd.DataFrame) -> pd.DataFrame:
    keep = STAR_FEATURES + [c for c in BH_EXTRA if c in df.columns]
    df = df[keep].copy()
    num_cols = [c for c in df.columns if c != "source_id"]
    for col in num_cols:
        df[col] = df[col].astype(float)
        df[col] = df[col].fillna(df[col].median())
    return df.dropna()


def main() -> None:
    args = parse_args()

    stars = pd.read_csv(args.stars_input)
    bh = pd.read_csv(args.bh_input)

    stars_clean = clean_stars(stars)
    bh_clean = clean_blackholes(bh)

    args.stars_output.parent.mkdir(parents=True, exist_ok=True)
    stars_clean.to_csv(args.stars_output, index=False)
    bh_clean.to_csv(args.bh_output, index=False)

    print(
        f"Saved {args.stars_output} (rows={len(stars_clean)}, cols={stars_clean.shape[1]}); "
        f"{args.bh_output} (rows={len(bh_clean)}, cols={bh_clean.shape[1]})"
    )


if __name__ == "__main__":
    main()
