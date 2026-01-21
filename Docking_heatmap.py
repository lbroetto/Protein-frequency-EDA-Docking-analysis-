#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
HEATMAP OF PROTEIN-LIGAND DOCKING ENERGY SCORES.

REQUIRED INPUT:
- CSV file with columns: 'Protein', 'Ligand', 'Energy_Score'
- Energy scores can use comma (,) or period (.) as decimal separator

CONFIGURATION:
1. Update 'INPUT_FILE' below with your CSV filename.
"""

# ================= CONFIGURATION =================
INPUT_FILE = 'input_data_table.csv'  # <<< UPDATE THIS
# =================================================

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load and preprocess data
df = pd.read_csv(INPUT_FILE)
df['Energy_Score'] = df['Energy_Score'].astype(str).str.replace(',', '.').astype(float)

# Create pivot table
df_pivot_energy = df.pivot(index="Protein", columns="Ligand", values="Energy_Score")

# Generate heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df_pivot_energy, annot=True, cmap="coolwarm", 
            cbar_kws={'label': 'Energy Score (kcal/mol)'}, fmt=".1f")
plt.title('Heatmap of Energy Scores for Protein-Ligand Docking')
plt.tight_layout()
plt.savefig('docking_energy_heatmap.png', dpi=300, bbox_inches='tight')
plt.show()