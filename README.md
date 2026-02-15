# Celestial Object Identification

Celestial Object Identification applies machine‑learning classification to tabular astronomical datasets (stars, exoplanet hosts, asteroids, comets, and quasars). The project focuses on **data cleaning, feature alignment, and rigorous evaluation** for binary and multiclass classification.

**What’s In This Repo**
- `data/` sample datasets and cleaned files
- `data/full/` full datasets (gitignored)
- `notebooks/` experiments (binary + multiclass)
- `src/` reusable Python modules and cleaning scripts
- `Main_plots/` saved plots from experiments
- `docs/` report sections and project documentation

**Datasets (samples in repo)**
- `data/asteroids_sample.csv`
- `data/comets_sample.csv`
- `data/comets_clean.csv`
- `data/exoplanets_sample.csv`
- `data/exoplanets_clean.csv`
- `data/stars_gaia_sample.csv`
- `data/quasars_gaia_sample.csv`

**Full datasets (not committed)**
- Stored under `data/full/` and excluded from Git due to size.
- If you need them, add a download link here (Google Drive / OneDrive) or regenerate with the scripts in `src/Scripts/full_clean/`.

**Experiments**
- Binary classification (full datasets)
- `notebooks/full_binary/asteroids_vs_comets_full.ipynb`
- `notebooks/full_binary/quasars_vs_stars_full.ipynb`
- `notebooks/full_binary/host_vs_non-host_stars.ipynb`
- Multiclass classification (stars vs exoplanet hosts vs quasars)
- `notebooks/multiclass_expetiment/multiclass_stars_exo_quasars.ipynb`

**Evaluation Protocol**
- Balanced sampling across classes
- Multiple dataset sizes (10k, 20k, 37.8k)
- Macro‑averaged metrics (accuracy, precision, recall, F1)
- K‑fold cross‑validation + held‑out test set
- Overfitting diagnostics (train/test gap)
- Confusion matrix + label‑shuffle sanity check

**Project Structure (Key Paths)**
- `src/data_loader.py`
- `src/preprocess.py`
- `src/plotting.py`
- `src/ml_models.py`
- `src/train_host_classifier.py`
- `src/utils.py`
- `src/Scripts/full_clean/` cleaning + enrichment scripts
- `notebooks/` all experiments
- `Main_plots/` saved plots

**Quick Start**
1. Create and activate a virtual environment
```bash
python -m venv .venv
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Run notebooks
```bash
jupyter notebook
```

**Plots**
- Binary results: `Main_plots/binary_*`
- Multiclass results: `Main_plots/multiclass_stars_exo_quasars/`

**Data Sources**
- NASA Exoplanet Archive (exoplanets)
- Gaia DR3 via `astroquery` (stars / quasars)

---

If you want me to add a results summary table or a Google Drive link for the full datasets, tell me and I’ll update this README.
