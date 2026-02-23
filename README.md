# Celestial Object Identification

Celestial Object Identification is a machine-learning project for classifying astronomical objects from **tabular survey/catalog data**. The project focuses on **data cleaning, schema alignment, feature selection, and fair model evaluation** across binary and multiclass tasks.

## Project Focus (Current)
- **Main focus:** multiclass classification of `star`, `exo_host`, and `quasar`
- **Supporting work:** binary classification experiments (asteroids/comets, quasars/stars, host vs non-host stars)
- **Emphasis:** robust preprocessing, balanced sampling, stratified validation, and clear performance comparison

## What Is In This Repository
- `data/` sample datasets and cleaned sample files
- `data/full/` full datasets and cleaned full files (large files may be gitignored depending on setup)
- `notebooks/` exploratory analysis and experiment notebooks
- `src/` reusable Python modules and data cleaning scripts
- `Main_plots/` and `Main_plts/` saved figures from experiments (both exist due notebook iterations)
- `docs/` report sections and project documentation

## Datasets Used (High Level)
This project uses tabular astronomical data for objects including:
- Stars (Gaia-based)
- Quasars (Gaia-based)
- Exoplanet host stars (NASA exoplanet catalog + Gaia-aligned/enriched fields)
- Asteroids
- Comets

### Multiclass Experiment Classes
The main multiclass notebook uses three labels:
- `star`
- `exo_host`
- `quasar`

### Full Dataset Counts Used in Multiclass (cleaned files)
- `stars_gaia_clean.csv`: `50,000`
- `quasars_gaia_clean.csv`: `50,000`
- `exoplanets_clean.csv`: `37,871`

Balanced multiclass subset sizes tested:
- `10,000` target total (actual `9,999` due equal-per-class sampling)
- `20,000` target total (actual `19,998`)
- `37,800` total

## Data Cleaning and Preparation
Cleaning scripts are located under `src/Scripts/`.

### Full Dataset Cleaning (`src/Scripts/full_clean/`)
- `clean_asteroids_full.py` - cleans full asteroid catalog (keeps robust orbital features)
- `clean_comets_full.py` - cleans full comet catalog (keeps robust orbital features)
- `clean_exoplanets_full.py` - cleans exoplanet catalog, aligns columns, imputes numeric gaps, writes `exoplanets_clean.csv`
- `clean_stars_quasars_full.py` - cleans Gaia stars and quasars and writes cleaned CSVs
- `enrich_exo_csv_file.py` - enriches exoplanet hosts with Gaia fields (`pmra`, `pmdec`, `phot_g_mean_mag`, `bp_rp`) via `astroquery`
- `enrich_exo_with_gaia.py` - helper script for aligning/combining cleaned multiclass-ready features

### Sample Cleaning (`src/Scripts/sample_clean/`)
- `clean_comets.py` - sample comet dataset cleaning for lightweight experiments

### Key Preprocessing Choices (Multiclass)
- Column alignment (e.g. exoplanet `sy_plx` renamed to `parallax`)
- Shared feature selection across classes for a fair comparison
- Median imputation in cleaning scripts for numeric gaps
- `dropna()` on selected final feature subsets used for modelling
- Balanced sampling across classes at each experiment size

## Experiments
### Multiclass (Main)
- `notebooks/multiclass_expetiment/multiclass_stars_exo_quasars.ipynb`
  - Classes: stars vs exoplanet hosts vs quasars
  - Models: Dummy baseline, Logistic Regression, Random Forest, MLP
  - Extensions: kNN, Decision Tree, SVM (linear / RBF / polynomial)
  - Additional comparison: `MLP + StandardScaler` vs `MLP + MinMaxScaler`
  - Outputs: metric plots, model comparison plots, confusion matrix (RF)

### Binary (Supporting)
- `notebooks/full_binary/10_full_data_profile.ipynb`
- `notebooks/full_binary/asteroids_vs_comets_full.ipynb`
- `notebooks/full_binary/host_vs_non-host_stars.ipynb`
- `notebooks/full_binary/quasars_vs_stars_full.ipynb`

### Archived Sample Binary Notebooks
- `notebooks/archive_sample_binary/` (early/prototype experiments on sample-sized data)

## Evaluation Protocol (Multiclass)
- Balanced sampling across the three classes
- Dataset sizes: `10k`, `20k`, `37.8k` (balanced total samples)
- `80%` train+validation / `20%` held-out test split (stratified)
- `StratifiedKFold` cross-validation on train+validation (`k=5`)
- Metrics:
  - Accuracy
  - Macro Precision
  - Macro Recall
  - Macro F1
- Confusion matrix and classification report for the best-performing model (Random Forest)
- Overfitting checks via CV vs test performance comparison

## Feature Scaling Strategy
- **Scaled (StandardScaler):** Logistic Regression, MLP, SVMs
- **Scaled (MinMaxScaler comparison):** kNN and an additional MLP comparison experiment
- **Not scaled (intentionally):** Random Forest and Decision Tree (tree-based models are largely scale-insensitive)

## Data Integrity Notes
- The multiclass experiment uses **three labels**: `star`, `exo_host`, `quasar`
- A Gaia ID overlap check was performed between stars and exoplanet hosts for the multiclass setup
- In the current cleaned full datasets used for the experiment, **0 overlapping Gaia IDs** were found (so no explicit overlap-removal step was needed)

## Project Structure (Key Paths)
- `src/data_loader.py`
- `src/preprocess.py`
- `src/plotting.py`
- `src/ml_models.py`
- `src/train_host_classifier.py`
- `src/utils.py`
- `src/Scripts/full_clean/`
- `src/Scripts/sample_clean/`
- `notebooks/full_binary/`
- `notebooks/multiclass_expetiment/`
- `Main_plots/`
- `Main_plts/`

## Quick Start
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

3. Run Jupyter
```bash
jupyter notebook
```

4. Open the main multiclass notebook
- `notebooks/multiclass_expetiment/multiclass_stars_exo_quasars.ipynb`

## Plot Outputs (Current)
Saved plots are currently split across two folders because of notebook iteration history:
- `Main_plots/multiclass_stars_exo_quasars/` (e.g. confusion matrix)
- `Main_plts/supervised_models/`
- `Main_plts/supervised_models_all/`
- `Main_plts/mlp_scaler_comparison/`

## Data Sources
- NASA Exoplanet Archive (exoplanet catalog)
- Gaia (via `astroquery` and Gaia catalog joins)
- Gaia-derived stars/quasars CSV datasets used in the project

## Notes
- Full datasets may be excluded from Git depending on file size and local setup.
- If needed, add a shared storage link (Google Drive / OneDrive) for reproducibility.
- The multiclass notebook is the most up-to-date end-to-end experiment workflow.
