# Medical Cost Personal (Insurance) Data Analysis & Predictor

**Course:** PSC(CE0525) &mdash; 5 CSE-F &mdash; Indus University  
**Student Team:** `IU2441230558`, `IU2441230559`  
**GitHub Repository:** [nandankhagram69/medical-cost-insurance-analysis](https://github.com/nandankhagram69/medical-cost-insurance-analysis)

---

## 🚀 Quick Start (Running the UI)

You have two simple ways to launch the UI:

### Option 1: Browser Web Dashboard (Recommended & Easiest)
- Simply double-click [`index.html`](file:///C:/Project%2021-10/index.html) to open the interactive dashboard in any browser.
- **Zero dependencies required** &mdash; works offline immediately.

### Option 2: Python Desktop GUI (Tkinter)
- Double-click [`run_ui.bat`](file:///C:/Project%2021-10/run_ui.bat) and choose `[2] Launch Python Desktop GUI`.
- Or run in terminal:
  ```bash
  python gui.py
  ```

---

## 📁 Project Contents

- [`index.html`](file:///C:/Project%2021-10/index.html): Responsive, interactive web dashboard featuring:
  - **KPI summary cards** (1,338 records, mean charges, smoker stats, BMI averages)
  - **Interactive Medical Cost Predictor** (Sliders for Age, BMI, Dependents, Smoker status, Region with instant ML-calibrated cost estimates and breakdown)
  - **All 6 Planned Visualizations** rendered interactively with Chart.js
  - **Searchable & Filterable Dataset Explorer** with pagination across all 1,338 records
  - **Project Proposal & Research Findings summary**
- [`gui.py`](file:///C:/Project%2021-10/gui.py): Native Python Desktop GUI built with standard `tkinter` + embedded `matplotlib`.
- [`run_ui.bat`](file:///C:/Project%2021-10/run_ui.bat): Interactive one-click Windows launcher.
- [`insurance.csv`](file:///C:/Project%2021-10/insurance.csv): Benchmark Kaggle dataset (1,338 records, 7 columns).
- [`generate_plots.py`](file:///C:/Project%2021-10/generate_plots.py): Generates high-resolution Seaborn plots into `eda_plots/`.
- [`eda_plots/`](file:///C:/Project%2021-10/eda_plots): Contains all 6 generated high-res visualization images.

---

## 📊 The 6 Planned Visualizations (Proposal Deliverables)

1. **Histogram of Insurance Charges**: Distribution showing a heavy right skew with peak charges between \$2,000&ndash;\$5,000.
2. **Box Plot (Smoker vs. Non-Smoker)**: Direct comparison showing smokers pay nearly 4x more (\$32,050 average vs. \$8,434 for non-smokers).
3. **Scatter Plot (Age vs. Charges)**: Clear upward trend (~+\$257 per year of age) divided into three distinct risk tiers.
4. **Scatter Plot (BMI vs. Charges)**: Demonstrates the critical inflection point at BMI = 30 (obesity threshold) where smoker costs surge past \$40,000.
5. **Bar Chart (Average Charges by Region)**: Southeast region has the highest average charges (\$14,735), followed by Northeast (\$13,406).
6. **Bar Chart (Average Charges by Sex)**: Males incur slightly higher average charges (\$13,957) than females (\$12,570).

---

## 📄 Proposal PDF Status

- **Original Proposal:** [`Python proposal.pdf`](file:///C:/Project%2021-10/Python%20proposal.pdf) is preserved completely intact.
- **Updated Proposal:** [`Python proposal_updated.pdf`](file:///C:/Project%2021-10/Python%20proposal_updated.pdf) has been generated with identical formatting, incorporating the Interactive User Interface (UI), Scikit-Learn regression modeling, and UI project deliverables in case your instructor requires the proposal to reflect the added UI.
