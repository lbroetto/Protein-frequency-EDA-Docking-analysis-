#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
EXPLORATORY DATA ANALYSIS: Heatmap, Clustermap, and Correlation Matrix.

REQUIRED INPUT:
- A matrix-style CSV file with features as rows and samples as columns.
- The first column should contain row labels (index).

CONFIGURATION:
1. Update 'INPUT_FILE' below with your CSV filename.
2. Adjust figure sizes if needed.
"""

# ================= CONFIGURATION =================
INPUT_FILE = 'input_data_table.csv'  # <<< UPDATE THIS
# =================================================

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
df = pd.read_csv(INPUT_FILE, index_col=0)

print(f"Data shape: {df.shape[0]} rows x {df.shape[1]} columns")

# 1. SIMPLE HEATMAP
plt.figure(figsize=(60, 10))
sns_plot = sns.heatmap(df, linewidth=1, linecolor='black', square=True, cmap='YlGnBu')
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=70, fontsize=12)
sns_plot.set_yticklabels(sns_plot.get_yticklabels(), fontsize=12)
plt.savefig('heatmap.png', dpi=300, bbox_inches='tight')
plt.show()

# 2. HIERARCHICAL CLUSTERING HEATMAP
sns_plot = sns.clustermap(df, metric="Dice", method="complete", linewidth=1,
                          linecolor='black', cmap="YlGnBu", standard_scale=1,
                          figsize=(20, 20))
sns_plot.ax_heatmap.tick_params(axis='x', labelsize=18, rotation=70)
sns_plot.ax_heatmap.tick_params(axis='y', labelsize=18)
cbar = sns_plot.ax_heatmap.collections[0].colorbar
cbar.ax.tick_params(labelsize=16)
plt.savefig('clustermap.png', dpi=300, bbox_inches='tight')
plt.show()

# 3. CORRELATION MATRIX WITH MASK
corr_matrix = df.corr()
mask = np.triu(np.ones_like(corr_matrix, dtype=bool), k=1)

plt.figure(figsize=(80, 20))
sns_plot = sns.heatmap(corr_matrix, mask=mask, linewidth=1, linecolor='white',
                       square=True, cmap='YlGnBu')
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), fontsize=20, rotation=70)
sns_plot.set_yticklabels(sns_plot.get_yticklabels(), fontsize=20, rotation=360)
cbar = sns_plot.collections[0].colorbar
cbar.ax.tick_params(labelsize=20)
plt.savefig('correlation_matrix.png', dpi=300, bbox_inches='tight')
plt.show()

print("Analysis complete. Figures saved as PNG files.")