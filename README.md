# :rocket: Celestial Object Identification

Celestial Object Identification is a project focused on applying artificial intelligence and computer vision techniques to detect and classify astronomical objects such as stars, planets, asteroids, comets, exoplanets, and quasars. The system leverages machine learning and deep learning models trained on astronomical datasets to automate the identification process.

---

## :file_folder: Project Structure

Explore the different components of this project:

- **[:database: Data Directory](#-data-directory)** - Astronomical datasets and samples
- **[:books: Documentation](#-documentation-directory)** - Project vision, ethics, and risk planning
- **[:notebook: Notebooks](#-notebooks-directory)** - Jupyter notebooks for analysis and experimentation
- **[:gear: Source Code](#-src-directory)** - Core Python modules and scripts

---

## :database: Data Directory

Located in `data/` - Contains sample datasets and cleaned versions of astronomical objects.

### Contents:
- **Asteroids**: `asteroids_clean.csv`
- **Comets**: `comets_clean.csv`
- **Exoplanets**: `exoplanets_clean.csv`, 
- **Quasars**: `quasars_gaia_clean.csv`
- **Stars**: `stars_gaia_clean.csv`
- **Temporary Files**: `tmp/` directory for VOTable data

:memo: These datasets are used for training and testing the classification models.

---

## :books: Documentation Directory

Located in `docs/` - Contains comprehensive documentation about the project.

### Key Documents:
- **[project_vision.md](docs/report_sections/project_vision.md)** - Overall project goals and vision
- **[ethics_legal_social.md](docs/report_sections/ethics_legal_social.md)** - Ethical considerations and legal aspects
- **[risk_plan.md](docs/report_sections/risk_plan.md)** - Risk assessment and mitigation strategies

---

## :notebook: Notebooks Directory

Located in `notebooks/` - Interactive Jupyter notebooks for data exploration and model development.

### Subdirectories:



#### **full_binary** - Binary classification experiments (full dataset)
- `10_full_data_profile.ipynb` - Complete data profiling
- `asteroids_vs_comets_full.ipynb` - Full dataset classification
- `host_vs_non-host_stars.ipynb` - Host star classification
- `quasars_vs_stars_full.ipynb` - Quasar vs Star classification

#### **multiclass_expetiment** - Multi-class classification experiments
- `multiclass_stars_exo_quasars.ipynb` - Multi-class classification (Stars, Exoplanets, Quasars)
- `test.ipynb` - Testing notebook

---

## :gear: Src Directory

Located in `src/` - Core Python modules and utilities for the project.

### Main Modules:

| Module | Purpose |
|--------|---------|
| **[data_loader.py](src/data_loader.py)** | Load and manage astronomical datasets |
| **[preprocess.py](src/preprocess.py)** | Data preprocessing and cleaning |
| **[plotting.py](src/plotting.py)** | Visualization utilities |
| **[ml_models.py](src/ml_models.py)** | Machine learning model definitions |
| **[train_host_classifier.py](src/train_host_classifier.py)** | Training pipeline for host star classifier |
| **[utils.py](src/utils.py)** | General utility functions |

### Scripts Directory

Located in `src/Scripts/` - Specialized data cleaning and preparation scripts.

#### **[full_clean/](src/Scripts/full_clean/)** - Full dataset cleaning scripts
- `clean_asteroids_full.py` - Clean and process entire asteroid dataset
- `clean_comets_full.py` - Clean and process entire comet dataset
- `clean_exoplanets_full.py` - Clean and process entire exoplanet dataset
- `clean_stars_quasars_full.py` - Clean and process stars and quasars
- `enrich_exo_csv_file.py` - Enrich exoplanet CSV with additional data
- `enrich_exo_with_gaia.py` - Integrate GAIA data with exoplanets



---

## :hammer: Root-Level Scripts

Main entry point scripts for dataset management and preprocessing:

- **[download_quasars.py](download_quasars.py)** - Download quasar data from external sources
- **[split_small_bodies.py](split_small_bodies.py)** - Split small bodies dataset (asteroids, comets)

---

## :rocket: Quick Start

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Celestial-Object-Identification
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Notebooks

1. **Start Jupyter**
   ```bash
   jupyter notebook
   ```

2. **Navigate to the `notebooks/` directory** and open any `.ipynb` file to explore the analysis and experiments.

### Using the Modules

Import modules in your Python scripts:
```python
from src.data_loader import load_data
from src.preprocess import preprocess_data
from src.ml_models import train_model
```

---

## :bulb: Key Features

- :star: Multi-class classification of celestial objects
- :chart_with_upwards_trend: Comprehensive data preprocessing pipelines
- :test_tube: Extensive notebook-based experimentation
- :mag: GAIA data integration for enhanced star classification
- :floppy_disk: Sample and full dataset variants for flexible testing

---

## :memo: Dependencies

Core dependencies (see `requirements.txt`):
- `numpy` - Numerical computing
- `pandas` - Data manipulation
- `matplotlib` & `seaborn` - Visualization
- `scikit-learn` - Machine learning algorithms
- `astroquery` - Astronomical data queries
- `jupyter` & `ipykernel` - Interactive notebooks
- `tqdm` - Progress bars

---

## :page_with_curl: License & Attribution

This project uses astronomical data from various sources including GAIA, exoplanet surveys, and asteroid/comet catalogs.

---

:arrow_right: **Start exploring**: Head to the [notebooks/](notebooks/) directory to see the analysis in action!
