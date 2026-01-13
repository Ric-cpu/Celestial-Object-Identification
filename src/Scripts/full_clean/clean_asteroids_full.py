"""
Clean the full asteroids catalog.

Drops extremely sparse physical columns (albedo, diameter) and keeps robust orbital elements.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


KEEP_COLS = ["full_name", "epoch", "e", "a", "q", "i", "ad", "moid", "H"]


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description="Clean full asteroids catalog")
    parser.add_argument(
        "--input",
        type=Path,
        default=repo_root / "data/full/asteroids.csv",
        help="Path to raw asteroids CSV",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=repo_root / "data/full/asteroids_clean.csv",
        help="Path to cleaned asteroids CSV",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.input)
    df = df[KEEP_COLS].copy()
    df["epoch"] = pd.to_numeric(df["epoch"], errors="coerce")
    for col in ["e", "a", "q", "i", "ad", "moid", "H"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(df[col].median())
    df = df.dropna()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.output, index=False)
    print(f"Saved {args.output} (rows={len(df)}, cols={df.shape[1]})")


if __name__ == "__main__":
    main()
