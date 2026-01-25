# Computational Analysis Scripts for Exploratory data analysis and docking analysis of proteins

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18365240.svg)](https://doi.org/10.5281/zenodo.18365240)

The scripts were written and developed by Leonardo Broetto (leonardo.broetto@arapiraca.ufal.br, Lbroetto@gmail.com)

This repository contains the custom Python scripts used for the computational analyses in the manuscript:

**Exploring the Molecular Basis of Potassium Usnate Activity Against Staphylococcus warneri Persistence and Resistance Through Protein Interaction Networks and Molecular Docking**  
*Submitted to: Network Modeling Analysis in Health Informatics and Bioinformatics (Springer Nature)*

# Contact
**Authors:** Leonardo Broetto
**Correspondence:** Lbroetto@gmail.com, leonardo.broetto@arapiraca.ufal.br
**Affiliation:** Núcleo de Pesquisa em Bioinformática e Filogenômica (NPBF), Universidade Federal de Alagoas, Brasil

---

## Repository Structure

| Directory/File | Description |
|----------------|-------------|
| `scripts/` | Main analysis scripts |
| `├── EDA_analysis.py` | Exploratory data analysis (heatmaps, clustering, correlation) |
| `├── docking_heatmap.py` | Heatmap of docking energy scores |
| `├── docking_relplot_ligand.py` | Scatter plot: Energy vs H-bonds (by Ligand) |
| `└── docking_relplot_protein.py` | Scatter plot: Energy vs H-bonds (by Protein) |
| `data/` | Input data files (not included in repository) |
| `figures/` | Generated output figures (PNG format) |
| `README.md` | This documentation file |
| `LICENSE` | GNU GPLv3 license file |
---

## Scripts Overview

### 1. `EDA_analysis.py`
**Purpose:** Exploratory data analysis of proteins frequency  
**Analyses performed:**
- Simple heatmap visualization of raw data
- Hierarchical clustering using Dice dissimilarity metric and complete linkage
- Pearson correlation matrix with triangular mask
- All figures are automatically saved as PNG files

**Key statistical elements:**
- **Dice dissimilarity:** Distance metric for binary/binarized data
- **Pearson correlation:** Measure of linear association between variables
- **Z-score normalization:** Applied via `standard_scale=1` parameter

### 2. `Docking_heatmap.py`
**Purpose:** Visualization of molecular docking results as a heatmap.  
**Functionality:**
- Processes docking energy scores from CSV
- Converts European decimal format (comma to period)
- Creates annotated heatmap with proteins as rows, ligands as columns
- Color gradient represents binding affinity (kcal/mol)

### 3. `Docking_relplot_ligand.py` & `Docking_relplot_protein.py`
**Purpose:** Relationship analysis between docking energy and hydrogen bond formation.  
**Key features:**
- Scatter plots with hue differentiation by ligand or protein
- Visualization of the energy-vs-stability relationship
- Automated data cleaning for decimal format conversion

| Script | Purpose | Required CSV Columns | Output Figure |
|--------|---------|----------------------|---------------|
| `EDA_analysis.py` | Exploratory heatmaps & clustering | Matrix format (rows=features, cols=samples) | `heatmap.png`, `clustermap.png`, `correlation_matrix.png` |
| `docking_heatmap.py` | Energy score heatmap | `Protein`, `Ligand`, `Energy_Score` | `docking_energy_heatmap.png` |
| `docking_relplot_ligand.py` | Energy vs H-bonds by ligand | `Ligand`, `Energy_Score(kcal/mol)`, `Hydrogen_Bonds` | `energy_vs_hbonds_by_ligand.png` |
| `docking_relplot_protein.py` | Energy vs H-bonds by protein | `Protein`, `Energy_Score(kcal/mol)`, `Hydrogen_Bonds` | `energy_vs_hbonds_by_protein.png` |


----
# Quick Start: Using the Scripts
Before running any script:

Prepare your data: Format your CSV file according to the specific requirements listed for each script below.

Configure the script: Open the script file and locate the INPUT_FILE variable at the top. Change its value to match your CSV filename.

Install dependencies: Ensure you have the required Python packages installed (see Requirements).

Run the script: Execute it from your terminal or IDE: python script_name.py

Data Privacy Note: The original research data is not included in this repository as the associated manuscript is under review. The scripts are configured to work with generic filenames (input_data_table.csv). Replace this with your own data filename.

Expected Data Location: By default, scripts look for the CSV file in the same directory as the script. You can modify the path in the INPUT_FILE variable if needed (e.g., 'data/my_file.csv').

---

## Data Availability Note

**Important:** The original input data files (`*.csv`) used in this study are **not included** in this repository, as the associated manuscript is currently under review. This protects the primary research data prior to formal publication.

### For Reproducibility and Reuse:
1.  **Code Execution:** To run these scripts with your own data, simply place your CSV file in the `data/` directory and update the filename in the script (or rename your file to match the expected name in the script).
2.  **Data Format:** Each script includes a comment at the top describing the **required column structure** for the input CSV. Please ensure your data follows this format.

### Expected Input Format (for each script):
- `EDA_analysis.py`: requires a matrix-style CSV file structured as follows: Rows: Protein families or protein identifiers. Columns: Genomes or sample names. Cell values: Numerical frequencies representing the count or presence of each protein identified in each genome via pHMM (profile Hidden Markov Model for each differente protein family) prediction.
- `Docking_heatmap.py`: Requires CSV with columns: `Protein`, `Ligand`, `Energy_Score`.
- `Docking_relplot_*.py`: Require CSV with columns: `Protein`, `Ligand`, `Energy_Score(kcal/mol)`, `Hydrogen_Bonds`.

## Requirements & Installation

### Python Dependencies
Create a conda environment or install directly:
``bash
pip install pandas numpy matplotlib seaborn

## Versions Tested
Python 3.8+
pandas >= 1.3.0
seaborn >= 0.11.0
matplotlib >= 3.3.0
numpy >= 1.19.0

# License and Citation

### Please cite:
Marcio Renan Santos Tavares, Nayara Andreo, Teresa de Lisieux Guedes Ferreira Lôbo, Chirles Araújo de França, Wagner Pereira Felix, Maria Aparecida Scatamburlo Moreira, Vasco Ariston de Carvalho Azevedo, Bertram Brenig, Leonardo Broetto, Mateus Matiuzzi da Costa (2026). Exploring the Molecular Basis of Potassium Usnate Activity Against Staphylococcus warneri Persistence and Resistance Through Protein Interaction Networks and Molecular Docking. Network Modeling Analysis in Health Informatics and Bioinformatics (under review).

If you use this scripts in your research, please cite:

### For the analysis scripts:
```bibtex
@software{broetto_docking_analysis_2026,
  author       = {Leonardo Broetto},
  title        = {{Python scripts for proteins exploratory data analysis 
                   and molecular docking visualization}},
  month        = jan,
  year         = 2026,
  publisher    = {Zenodo},
  version      = {v1.0.0},
  doi          = {10.5281/zenodo.18365240},
  url          = {https://doi.org/10.5281/zenodo.18365240}
}
```

This project is licensed under the **GNU General Public License v3.0**.

### Terms for Academic/Research Use:
- Free to use, study, and modify
- Must distribute derivatives under GPLv3
- Must provide source code when distributing binaries
- Must preserve copyright notices and license text

### Terms for Commercial Use:
For commercial applications or proprietary integration, please contact the author (Lbroetto@gmail.com, leonardo.broetto@arapiraca.ufal.br) to discuss alternative licensing options.

**Full license text:** [LICENSE](LICENSE)

## Intellectual Property Notice

The computational methods, algorithms, and models implemented in this software are research outcomes from Universidade Federal de Alagoas. While the source code is licensed under GPLv3 for academic and open-source use, commercial licensing options are available.

This software is available under two licenses:
1. GNU GPLv3 for open source/academic use
2. Commercial license for proprietary use (contact author)
For commercial licensing, technology transfer, or collaboration inquiries:
Contact: Lbroetto@gmail.com, leonardo.broetto@arapiraca.ufal.br


### Copyright and Licensing
- **Copyright Holder:** Leonardo Broetto  
- **License:** GNU General Public License v3.0  
- **Year:** 2026

### Research Attribution
The computational methodologies implemented in this software were developed as part of research activities conducted by Leonardo Broetto. Associated research work is linked to Universidade Federal de Alagoas.

### Usage Terms
- **Academic/Research Use:** Permitted under GPLv3 with mandatory citation
- **Commercial Use:** Requires alternative licensing (contact author)
- **Derivative Works:** Must be released under GPLv3

### Contact for Licensing
Leonardo Broetto  
Lbroetto@gmail.com, leonardo.broetto@arapiraca.ufal.br
(Associated with Universidade Federal de Alagoas)
