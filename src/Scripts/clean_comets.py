"""
Create a cleaned comets dataset by dropping sparse columns and any remaining NaNs.

Usage:
    python clean_comets.py [--input data/comets_sample.csv] [--output data/comets_clean.csv]
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


SPARSE_COLUMNS = ["H", "albedo", "diameter", "condition_code", "ad", "rms", "moid", "a"]


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description="Clean the comets sample CSV.")
    parser.add_argument(
        "--input",
        type=Path,
        default=repo_root / "data/comets_sample.csv",
        help="Path to the raw comets sample CSV.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=repo_root / "data/comets_clean.csv",
        help="Destination for the cleaned CSV.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    df = pd.read_csv(args.input)
    cleaned = df.drop(columns=[c for c in SPARSE_COLUMNS if c in df.columns]).dropna()
    cleaned.to_csv(args.output, index=False)

    print(
        f"Cleaned comets dataset written to {args.output} "
        f"(rows={len(cleaned)}, cols={cleaned.shape[1]})"
    )


if __name__ == "__main__":
    main()
