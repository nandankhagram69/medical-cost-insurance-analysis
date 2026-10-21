import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({'font.sans-serif': 'Segoe UI', 'font.family': 'sans-serif'})

os.makedirs('eda_plots', exist_ok=True)
df = pd.read_csv('insurance.csv')

# 1. Histogram of insurance charges
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df['charges'], kde=True, color='#2563eb', bins=35, ax=ax)
ax.set_title('1. Distribution of Insurance Charges', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Charges ($ USD)', fontsize=11)
ax.set_ylabel('Frequency / Count', fontsize=11)
plt.tight_layout()
fig.savefig('eda_plots/1_charges_histogram.png', dpi=200)
plt.close(fig)

# 2. Box plot: smoker vs non-smoker
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x='smoker', y='charges', data=df, hue='smoker', palette=['#10b981', '#ef4444'], legend=False, ax=ax, width=0.45)
ax.set_title('2. Insurance Charges by Smoking Status', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Smoker Status', fontsize=11)
ax.set_ylabel('Charges ($ USD)', fontsize=11)
ax.set_xticklabels(['Non-Smoker (Avg: $8,434)', 'Smoker (Avg: $32,050)'])
plt.tight_layout()
fig.savefig('eda_plots/2_smoker_boxplot.png', dpi=200)
plt.close(fig)

# 3. Scatter plot: age vs charges
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(x='age', y='charges', hue='smoker', data=df, palette={'no': '#10b981', 'yes': '#ef4444'}, alpha=0.75, ax=ax)
ax.set_title('3. Age vs. Insurance Charges', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Age (Years)', fontsize=11)
ax.set_ylabel('Charges ($ USD)', fontsize=11)
ax.legend(title='Smoker', loc='upper left')
plt.tight_layout()
fig.savefig('eda_plots/3_age_vs_charges_scatter.png', dpi=200)
plt.close(fig)

# 4. Scatter plot: BMI vs charges
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(x='bmi', y='charges', hue='smoker', data=df, palette={'no': '#10b981', 'yes': '#ef4444'}, alpha=0.75, ax=ax)
ax.axvline(30, color='#f59e0b', linestyle='--', label='Obesity Threshold (BMI=30)')
ax.set_title('4. BMI vs. Insurance Charges', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Body Mass Index (BMI)', fontsize=11)
ax.set_ylabel('Charges ($ USD)', fontsize=11)
ax.legend(title='Smoker / Benchmark', loc='upper left')
plt.tight_layout()
fig.savefig('eda_plots/4_bmi_vs_charges_scatter.png', dpi=200)
plt.close(fig)

# 5. Bar chart: average charges by region
fig, ax = plt.subplots(figsize=(8, 5))
region_avg = df.groupby('region')['charges'].mean().reset_index()
sns.barplot(x='region', y='charges', hue='region', data=region_avg, palette='Blues_d', legend=False, ax=ax)
for p in ax.patches:
    ax.annotate(f"${p.get_height():,.0f}", (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 8), textcoords='offset points', fontsize=10, fontweight='bold')
ax.set_title('5. Average Insurance Charges by Region', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Geographical Region', fontsize=11)
ax.set_ylabel('Average Charges ($ USD)', fontsize=11)
ax.set_ylim(0, max(region_avg['charges']) * 1.15)
plt.tight_layout()
fig.savefig('eda_plots/5_region_barchart.png', dpi=200)
plt.close(fig)

# 6. Bar chart: average charges by sex
fig, ax = plt.subplots(figsize=(8, 5))
sex_avg = df.groupby('sex')['charges'].mean().reset_index()
sns.barplot(x='sex', y='charges', hue='sex', data=sex_avg, palette=['#ec4899', '#3b82f6'], legend=False, ax=ax, width=0.45)
for p in ax.patches:
    ax.annotate(f"${p.get_height():,.0f}", (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 8), textcoords='offset points', fontsize=10, fontweight='bold')
ax.set_title('6. Average Insurance Charges by Sex', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Sex', fontsize=11)
ax.set_ylabel('Average Charges ($ USD)', fontsize=11)
ax.set_ylim(0, max(sex_avg['charges']) * 1.15)
plt.tight_layout()
fig.savefig('eda_plots/6_sex_barchart.png', dpi=200)
plt.close(fig)

print("All 6 visualization plots saved successfully into eda_plots/!")
