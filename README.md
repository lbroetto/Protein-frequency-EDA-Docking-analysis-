# EDA-Resistance_Persistence-protein-docking-analysis
Analysis scripts for the manuscript "Exploring the Molecular Basis of Potassium Usnate Activity Against Staphylococcus warneri Persistence and Resistance Through Protein Interaction Networks and Molecular Docking"

# Computational Analysis Scripts for Exploratory data analysis and docking analysis of proteins

The scripts were written and developed by Leonardo Broetto (leonardo.broetto@arapiraca.ufal.br, Lbroetto@gmail.com)

This repository contains the custom Python scripts used for the computational analyses in the manuscript:

**Exploring the Molecular Basis of Potassium Usnate Activity Against Staphylococcus warneri Persistence and Resistance Through Protein Interaction Networks and Molecular Docking**  
*Submitted to: Network Modeling Analysis in Health Informatics and Bioinformatics (Springer Nature)*

# Contact
**Authors:** Leonardo Broetto
**Correspondence:** Lbroetto@gmail.com, leonardo.broetto@arapiraca.ufal.br
**Affiliation:** Núcleo de Pesquisa em Bioinformática e Filogenômica, Universidade Federal de Alagoas, Brasil

---

## Repository Structure
├── scripts/ # Main analysis scripts
│ ├── EDA_analysis.py # Exploratory data analysis (heatmaps, clustering, correlation)
│ ├── docking_heatmap.py # Heatmap of docking energy scores
│ ├── docking_relplot_ligand.py # Scatter plot: Energy vs H-bonds (by Ligand)
│ └── docking_relplot_protein.py # Scatter plot: Energy vs H-bonds (by Protein)
└── README.md # This file

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

Script	                     Purpose	                           Required CSV                                   Columns	Output Figure
EDA_analysis.py	            Exploratory heatmaps & clustering	Matrix format (rows=features, cols=samples)	  heatmap.png, clustermap.png, correlation_matrix.png
docking_heatmap.py	         Energy score heatmap	Protein,       Ligand, Energy_Score	                          docking_energy_heatmap.png
docking_relplot_ligand.py	   Energy vs H-bonds by ligand	      Ligand, Energy_Score(kcal/mol),                Hydrogen_Bonds	energy_vs_hbonds_by_ligand.png
docking_relplot_protein.py	   Energy vs H-bonds by protein	      Protein, Energy_Score(kcal/mol),               Hydrogen_Bonds	energy_vs_hbonds_by_protein.png


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
- `EDA_analysis.py`: Requires a matrix-style CSV with proteins as rows and ligands as columns.
- `Docking_heatmap.py`: Requires CSV with columns: `Protein`, `Ligand`, `Energy_Score`.
- `Docking_relplot_*.py`: Require CSV with columns: `Protein`, `Ligand`, `Energy_Score(kcal/mol)`, `Hydrogen_Bonds`.

## Requirements & Installation

### Python Dependencies
Create a conda environment or install directly:
```bash
pip install pandas numpy matplotlib seaborn


