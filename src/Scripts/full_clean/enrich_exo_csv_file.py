import pandas as pd
from pathlib import Path
from astroquery.gaia import Gaia
from astropy.table import Table


def main():
    repo_root = Path(__file__).resolve().parents[3]
    exo_path = repo_root / "data/full/exoplanets_clean.csv"
    out_path = repo_root / "data/full/exoplanets_gaia_enriched.csv"
    tmp_dir = repo_root / "data/tmp"
    tmp_dir.mkdir(parents=True, exist_ok=True)

    exo = pd.read_csv(exo_path)

    # normalize gaia_id in exo (important!)
    exo["gaia_id"] = (
    exo["gaia_id"].astype(str)
    .str.replace(r"[^0-9]", "", regex=True)  # keep digits only
)
    exo["gaia_id"] = pd.to_numeric(exo["gaia_id"], errors="coerce")
    exo = exo.dropna(subset=["gaia_id"])
    exo["gaia_id"] = exo["gaia_id"].astype("int64")

    ids = exo[["gaia_id"]].drop_duplicates()


    query = """
    SELECT t.gaia_id,
           gs.pmra, gs.pmdec,
           gs.phot_g_mean_mag, gs.bp_rp
    FROM TAP_UPLOAD.user_exo t
    JOIN gaiadr2.gaia_source gs
    ON t.gaia_id = gs.source_id
    """


    all_rows = []
    chunk_size = 2000

    for start in range(0, len(ids), chunk_size):
        chunk = ids.iloc[start:start + chunk_size]
        chunk_path = tmp_dir / f"exo_gaia_ids_{start}.vot"
        Table.from_pandas(chunk).write(chunk_path, format="votable", overwrite=True)

        print(f"Fetching ids {start}–{start + len(chunk)}...")
        job = Gaia.launch_job(query, upload_resource=str(chunk_path), upload_table_name="user_exo")
        all_rows.append(job.get_results().to_pandas())

    gaia_df = pd.concat(all_rows, ignore_index=True)

    # normalize gaia_id in gaia_df (important!)
    gaia_df["gaia_id"] = pd.to_numeric(gaia_df["gaia_id"], errors="coerce")
    gaia_df = gaia_df.dropna(subset=["gaia_id"])
    gaia_df["gaia_id"] = gaia_df["gaia_id"].astype("int64")

    enriched = exo.merge(gaia_df, on="gaia_id", how="left")
    enriched.to_csv(out_path, index=False)
    print(f"Saved {out_path} (rows={len(enriched)}, cols={enriched.shape[1]})")


if __name__ == "__main__":
    main()
