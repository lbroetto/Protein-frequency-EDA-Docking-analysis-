#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SCATTER PLOT: Energy vs Hydrogen Bonds, colored by Protein.

REQUIRED INPUT:
- CSV file with columns: 'Protein', 'Energy_Score(kcal/mol)', 'Hydrogen_Bonds'
- Additional columns are ignored

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
df['Energy_Score(kcal/mol)'] = df['Energy_Score(kcal/mol)'].astype(str).str.replace(',', '.').astype(float)

# Create relational plot
sns.relplot(data=df, x="Energy_Score(kcal/mol)", y="Hydrogen_Bonds", 
            hue="Protein", kind="scatter", palette="Set1")
plt.title('Energy vs Hydrogen Bonds (by Protein)')
plt.tight_layout()
plt.savefig('energy_vs_hbonds_by_protein.png', dpi=300, bbox_inches='tight')
plt.show()