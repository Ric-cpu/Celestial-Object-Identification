from astroquery.gaia import Gaia
import pandas as pd

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

#Run the Gaia query (sync endpoint is more stable for small result sets)
job = Gaia.launch_job(query)
result = job.get_results()

#Convert to pandas DataFrame
df = result.to_pandas()

#Save to CSV
output_path = "data/blackholes_gaia.csv"
df.to_csv(output_path, index=False)
print("Saved", output_path)

