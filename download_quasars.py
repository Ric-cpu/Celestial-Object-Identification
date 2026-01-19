from astroquery.gaia import Gaia
import pandas as pd

# Optional: if the Gaia archive requires login, uncomment and set your credentials.
# Gaia.login(user="your_email_or_username", password="your_password")

Gaia.ROW_LIMIT = 50000   # set a size you want, or -1 for “all”

query = """
SELECT
    agn.source_id,
    agn.catalogue_name,
    agn.source_name_in_catalogue,
    gs.ra, gs.dec,
    gs.pmra, gs.pmdec,
    gs.pmra_error, gs.pmdec_error,
    gs.parallax, gs.parallax_error,
    gs.phot_g_mean_mag,
    gs.phot_bp_mean_mag,
    gs.phot_rp_mean_mag,
    gs.bp_rp,
    gs.ruwe,
    gs.astrometric_params_solved,
    gs.classprob_dsc_combmod_quasar AS quasar_probability
FROM gaiadr3.agn_cross_id AS agn
JOIN gaiadr3.gaia_source AS gs
ON agn.source_id = gs.source_id
"""

print("Launching Gaia async job...")
job = Gaia.launch_job_async(query)  # async for bigger pulls
print(f"Job ID: {job.jobid}")
df = job.get_results().to_pandas()

df.to_csv("data/full/quasars_gaia.csv", index=False)
print("Saved", "data/full/quasars_gaia.csv")

# Gaia.logout()
