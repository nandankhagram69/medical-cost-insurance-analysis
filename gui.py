import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np

# Matplotlib embedded in Tkinter
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns

class MedicalInsuranceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Medical Cost Personal Insurance Analysis & Estimator")
        self.root.geometry("1080x750")
        self.root.minsize(900, 650)
        
        # Load dataset
        self.csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "insurance.csv")
        if os.path.exists(self.csv_path):
            self.df = pd.read_csv(self.csv_path)
        else:
            self.df = pd.DataFrame()

        self.setup_styles()
        self.create_header()
        self.create_tabs()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        
        # Color palette
        style.configure("TNotebook", background="#f1f5f9")
        style.configure("TNotebook.Tab", padding=[14, 8], font=("Segoe UI", 10, "bold"), background="#e2e8f0", foreground="#334155")
        style.map("TNotebook.Tab", background=[("selected", "#2563eb")], foreground=[("selected", "white")])
        
        style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"), background="#1e3a8a", foreground="white")
        style.configure("SubHeader.TLabel", font=("Segoe UI", 9), background="#1e3a8a", foreground="#cbd5e1")
        
        style.configure("Primary.TButton", font=("Segoe UI", 10, "bold"), background="#2563eb", foreground="white", padding=6)
        style.map("Primary.TButton", background=[("active", "#1d4ed8")])
        
        style.configure("Card.TFrame", background="white", relief="solid", borderwidth=1)

    def create_header(self):
        header_frame = tk.Frame(self.root, bg="#1e3a8a", height=75, padx=20, pady=12)
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(header_frame, text="🏥 Medical Cost Personal Insurance Analysis", font=("Segoe UI", 15, "bold"), bg="#1e3a8a", fg="white")
        title_label.pack(anchor="w")
        
        info_label = tk.Label(header_frame, text="Indus University | PSC(CE0525) | 5 CSE-F | Roll Nos: IU2441230558, IU2441230559", font=("Segoe UI", 9), bg="#1e3a8a", fg="#93c5fd")
        info_label.pack(anchor="w")

    def create_tabs(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Tab 1: Predictor
        self.tab_predictor = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_predictor, text="  💡 Cost Estimator  ")
        self.build_predictor_tab()
        
        # Tab 2: Visualizations
        self.tab_visuals = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_visuals, text="  📊 6 Visualizations  ")
        self.build_visuals_tab()
        
        # Tab 3: Dataset Explorer
        self.tab_data = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_data, text="  📋 Dataset Explorer (1,338)  ")
        self.build_data_tab()

        # Tab 4: Proposal Info
        self.tab_info = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_info, text="  📄 Proposal & Summary  ")
        self.build_info_tab()

    def build_predictor_tab(self):
        paned = tk.PanedWindow(self.tab_predictor, orient=tk.HORIZONTAL, bg="#f8fafc", sashwidth=4)
        paned.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left Panel: Form
        left_frame = tk.LabelFrame(paned, text=" Individual Health & Demographic Inputs ", font=("Segoe UI", 11, "bold"), bg="white", padx=15, pady=15)
        paned.add(left_frame, minsize=420)
        
        # Age
        tk.Label(left_frame, text="Age (Years):", font=("Segoe UI", 10, "bold"), bg="white").pack(anchor="w", pady=(5, 2))
        self.age_var = tk.IntVar(value=35)
        self.age_label = tk.Label(left_frame, text="35 yrs", font=("Segoe UI", 9, "bold"), bg="white", fg="#2563eb")
        self.age_label.pack(anchor="w")
        self.age_slider = tk.Scale(left_frame, from_=18, to=64, orient=tk.HORIZONTAL, variable=self.age_var, bg="white", highlightthickness=0, command=self.update_age_label)
        self.age_slider.pack(fill=tk.X, pady=(0, 10))

        # BMI
        tk.Label(left_frame, text="Body Mass Index (BMI):", font=("Segoe UI", 10, "bold"), bg="white").pack(anchor="w", pady=(5, 2))
        self.bmi_var = tk.DoubleVar(value=27.5)
        self.bmi_label = tk.Label(left_frame, text="27.5 kg/m² (Overweight)", font=("Segoe UI", 9, "bold"), bg="white", fg="#f59e0b")
        self.bmi_label.pack(anchor="w")
        self.bmi_slider = tk.Scale(left_frame, from_=15.0, to=53.0, resolution=0.1, orient=tk.HORIZONTAL, variable=self.bmi_var, bg="white", highlightthickness=0, command=self.update_bmi_label)
        self.bmi_slider.pack(fill=tk.X, pady=(0, 10))

        # Smoker
        tk.Label(left_frame, text="Smoking Status:", font=("Segoe UI", 10, "bold"), bg="white").pack(anchor="w", pady=(5, 2))
        self.smoker_var = tk.StringVar(value="no")
        smoker_frame = tk.Frame(left_frame, bg="white")
        smoker_frame.pack(fill=tk.X, pady=(0, 10))
        tk.Radiobutton(smoker_frame, text="Non-Smoker", variable=self.smoker_var, value="no", bg="white", font=("Segoe UI", 9), command=self.calculate_estimate).pack(side=tk.LEFT, padx=(0, 15))
        tk.Radiobutton(smoker_frame, text="Smoker (High Risk)", variable=self.smoker_var, value="yes", bg="white", fg="#ef4444", font=("Segoe UI", 9, "bold"), command=self.calculate_estimate).pack(side=tk.LEFT)

        # Sex
        tk.Label(left_frame, text="Biological Sex:", font=("Segoe UI", 10, "bold"), bg="white").pack(anchor="w", pady=(5, 2))
        self.sex_var = tk.StringVar(value="female")
        sex_frame = tk.Frame(left_frame, bg="white")
        sex_frame.pack(fill=tk.X, pady=(0, 10))
        tk.Radiobutton(sex_frame, text="Female", variable=self.sex_var, value="female", bg="white", font=("Segoe UI", 9), command=self.calculate_estimate).pack(side=tk.LEFT, padx=(0, 15))
        tk.Radiobutton(sex_frame, text="Male", variable=self.sex_var, value="male", bg="white", font=("Segoe UI", 9), command=self.calculate_estimate).pack(side=tk.LEFT)

        # Children
        tk.Label(left_frame, text="Children / Dependents:", font=("Segoe UI", 10, "bold"), bg="white").pack(anchor="w", pady=(5, 2))
        self.children_var = tk.IntVar(value=1)
        children_frame = tk.Frame(left_frame, bg="white")
        children_frame.pack(fill=tk.X, pady=(0, 10))
        for num in range(6):
            tk.Radiobutton(children_frame, text=str(num), variable=self.children_var, value=num, bg="white", font=("Segoe UI", 9), command=self.calculate_estimate).pack(side=tk.LEFT, padx=5)

        # Region
        tk.Label(left_frame, text="Geographical Region:", font=("Segoe UI", 10, "bold"), bg="white").pack(anchor="w", pady=(5, 2))
        self.region_var = tk.StringVar(value="southeast")
        region_combo = ttk.Combobox(left_frame, textvariable=self.region_var, values=["northeast", "northwest", "southeast", "southwest"], state="readonly", font=("Segoe UI", 9))
        region_combo.pack(fill=tk.X, pady=(0, 15))
        region_combo.bind("<<ComboboxSelected>>", lambda e: self.calculate_estimate())

        # Reset button
        tk.Button(left_frame, text="↺ Reset to Defaults", font=("Segoe UI", 9), command=self.reset_inputs, bg="#f1f5f9", relief="groove").pack(anchor="w")

        # Right Panel: Results Box
        right_frame = tk.LabelFrame(paned, text=" Insurance Cost Prediction & Analysis ", font=("Segoe UI", 11, "bold"), bg="#0f172a", fg="white", padx=20, pady=20)
        paned.add(right_frame, minsize=420)
        
        tk.Label(right_frame, text="PROJECTED ANNUAL MEDICAL PREMIUM", font=("Segoe UI", 9, "bold"), bg="#0f172a", fg="#94a3b8").pack(anchor="w", pady=(10, 0))
        
        self.result_label = tk.Label(right_frame, text="$6,128", font=("Segoe UI", 32, "bold"), bg="#0f172a", fg="#38bdf8")
        self.result_label.pack(anchor="w", pady=(5, 15))

        tk.Label(right_frame, text="Model Cost Factors Breakdown ($R^2 = 0.751$):", font=("Segoe UI", 10, "bold"), bg="#0f172a", fg="#e2e8f0").pack(anchor="w", pady=(5, 5))
        
        self.breakdown_frame = tk.Frame(right_frame, bg="#1e293b", padx=15, pady=15, relief="flat")
        self.breakdown_frame.pack(fill=tk.X, pady=10)

        self.lbl_baseline = tk.Label(self.breakdown_frame, text="• Base Constant: -$11,939", font=("Segoe UI", 9), bg="#1e293b", fg="#cbd5e1")
        self.lbl_baseline.pack(anchor="w", pady=2)

        self.lbl_age_factor = tk.Label(self.breakdown_frame, text="• Age Impact (35 yrs × $256.86): +$8,990", font=("Segoe UI", 9), bg="#1e293b", fg="#fca5a5")
        self.lbl_age_factor.pack(anchor="w", pady=2)

        self.lbl_bmi_factor = tk.Label(self.breakdown_frame, text="• BMI Impact (27.5 × $339.19): +$9,328", font=("Segoe UI", 9), bg="#1e293b", fg="#fca5a5")
        self.lbl_bmi_factor.pack(anchor="w", pady=2)

        self.lbl_smoker_factor = tk.Label(self.breakdown_frame, text="• Smoker Penalty: +$0 (Non-Smoker)", font=("Segoe UI", 9), bg="#1e293b", fg="#86efac")
        self.lbl_smoker_factor.pack(anchor="w", pady=2)

        self.lbl_child_factor = tk.Label(self.breakdown_frame, text="• Dependents (1 child × $475.50): +$476", font=("Segoe UI", 9), bg="#1e293b", fg="#fca5a5")
        self.lbl_child_factor.pack(anchor="w", pady=2)

        self.lbl_region_factor = tk.Label(self.breakdown_frame, text="• Region Adjustment (Southeast): -$1,035", font=("Segoe UI", 9), bg="#1e293b", fg="#93c5fd")
        self.lbl_region_factor.pack(anchor="w", pady=2)

        # Quick insight note
        note_box = tk.Label(right_frame, text="💡 Key Takeaway: Smoking status causes the largest penalty (~+$23,848), followed by BMI when BMI > 30. Age steadily adds $257 every year.",
                            font=("Segoe UI", 9, "italic"), bg="#0f172a", fg="#94a3b8", wraplength=380, justify="left")
        note_box.pack(anchor="w", pady=(20, 0))

        self.calculate_estimate()

    def update_age_label(self, val):
        self.age_label.config(text=f"{val} yrs")
        self.calculate_estimate()

    def update_bmi_label(self, val):
        bmi = float(val)
        if bmi < 18.5:
            cat = "Underweight"
            color = "#3b82f6"
        elif bmi < 25.0:
            cat = "Normal Weight"
            color = "#10b981"
        elif bmi < 30.0:
            cat = "Overweight"
            color = "#f59e0b"
        else:
            cat = "Obese (High Risk)"
            color = "#ef4444"
        self.bmi_label.config(text=f"{bmi:.1f} kg/m² ({cat})", fg=color)
        self.calculate_estimate()

    def calculate_estimate(self):
        age = self.age_var.get()
        bmi = self.bmi_var.get()
        is_smoker = self.smoker_var.get() == "yes"
        sex = self.sex_var.get()
        children = self.children_var.get()
        region = self.region_var.get()

        intercept = -11938.54
        age_imp = 256.86 * age
        bmi_imp = 339.19 * bmi
        child_imp = 475.50 * children
        sex_imp = -131.31 if sex == "male" else 0
        smoker_imp = 23848.53 if is_smoker else 0

        region_imp = 0
        if region == "northwest": region_imp = -352.96
        elif region == "southeast": region_imp = -1035.02
        elif region == "southwest": region_imp = -960.05

        interaction = 0
        if is_smoker and bmi >= 30:
            interaction = (bmi - 30) * 450

        total = intercept + age_imp + bmi_imp + child_imp + sex_imp + smoker_imp + region_imp + interaction
        if total < 1120: total = 1120

        self.result_label.config(text=f"${int(round(total)):,}")
        self.lbl_age_factor.config(text=f"• Age Impact ({age} yrs × $256.86): +${int(round(age_imp)):,}")
        self.lbl_bmi_factor.config(text=f"• BMI Impact ({bmi:.1f} × $339.19): +${int(round(bmi_imp)):,}")
        self.lbl_child_factor.config(text=f"• Dependents ({children} × $475.50): +${int(round(child_imp)):,}")
        
        if is_smoker:
            self.lbl_smoker_factor.config(text=f"• Smoker Penalty: +${int(round(smoker_imp + interaction)):,} (High Risk)", fg="#f87171")
        else:
            self.lbl_smoker_factor.config(text="• Smoker Penalty: +$0 (Non-Smoker)", fg="#86efac")

        reg_name = region.capitalize()
        self.lbl_region_factor.config(text=f"• Region Adjustment ({reg_name}): {'+$' if region_imp >= 0 else '-$'}{abs(int(round(region_imp))):,}")

    def reset_inputs(self):
        self.age_var.set(35)
        self.bmi_var.set(27.5)
        self.smoker_var.set("no")
        self.sex_var.set("female")
        self.children_var.set(1)
        self.region_var.set("southeast")
        self.update_age_label(35)
        self.update_bmi_label(27.5)

    def build_visuals_tab(self):
        top_ctrl = tk.Frame(self.tab_visuals, bg="#f1f5f9", pady=8, padx=10)
        top_ctrl.pack(fill=tk.X)
        
        tk.Label(top_ctrl, text="Select Planned Visualization:", font=("Segoe UI", 10, "bold"), bg="#f1f5f9").pack(side=tk.LEFT, padx=(0, 10))
        
        self.visual_choice = tk.StringVar(value="1. Charges Histogram")
        choices = [
            "1. Charges Histogram",
            "2. Smoker vs. Non-Smoker Box Plot",
            "3. Age vs. Charges Scatter",
            "4. BMI vs. Charges Scatter",
            "5. Average Charges by Region Bar",
            "6. Average Charges by Sex Bar"
        ]
        combo = ttk.Combobox(top_ctrl, textvariable=self.visual_choice, values=choices, state="readonly", width=35, font=("Segoe UI", 9))
        combo.pack(side=tk.LEFT, padx=5)
        combo.bind("<<ComboboxSelected>>", lambda e: self.render_plot())
        
        tk.Button(top_ctrl, text="🔄 Render Plot", font=("Segoe UI", 9, "bold"), bg="#2563eb", fg="white", command=self.render_plot).pack(side=tk.LEFT, padx=10)

        # Plot Display Canvas Container
        self.plot_container = tk.Frame(self.tab_visuals, bg="white")
        self.plot_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.render_plot()

    def render_plot(self):
        for widget in self.plot_container.winfo_children():
            widget.destroy()

        if self.df.empty:
            tk.Label(self.plot_container, text="insurance.csv not found in folder", font=("Segoe UI", 12)).pack(pady=40)
            return

        choice = self.visual_choice.get()
        fig, ax = plt.subplots(figsize=(8.5, 4.8), dpi=100)
        sns.set_theme(style="whitegrid", palette="muted")

        if "1. Charges Histogram" in choice:
            sns.histplot(self.df['charges'], kde=True, color='#2563eb', bins=35, ax=ax)
            ax.set_title("1. Distribution of Medical Insurance Charges", fontsize=12, fontweight='bold', pad=10)
            ax.set_xlabel("Charges ($ USD)")
            ax.set_ylabel("Count / Frequency")
        elif "2. Smoker" in choice:
            sns.boxplot(x='smoker', y='charges', data=self.df, hue='smoker', palette=['#10b981', '#ef4444'], legend=False, ax=ax, width=0.45)
            ax.set_title("2. Medical Charges by Smoker Status", fontsize=12, fontweight='bold', pad=10)
            ax.set_xlabel("Smoking Status")
            ax.set_ylabel("Charges ($ USD)")
            ax.set_xticks([0, 1])
            ax.set_xticklabels(['Non-Smoker (Avg: $8,434)', 'Smoker (Avg: $32,050)'])
        elif "3. Age" in choice:
            sns.scatterplot(x='age', y='charges', hue='smoker', data=self.df, palette={'no': '#10b981', 'yes': '#ef4444'}, alpha=0.75, ax=ax)
            ax.set_title("3. Age vs. Insurance Charges", fontsize=12, fontweight='bold', pad=10)
            ax.set_xlabel("Age (Years)")
            ax.set_ylabel("Charges ($ USD)")
        elif "4. BMI" in choice:
            sns.scatterplot(x='bmi', y='charges', hue='smoker', data=self.df, palette={'no': '#10b981', 'yes': '#ef4444'}, alpha=0.75, ax=ax)
            ax.axvline(30, color='#f59e0b', linestyle='--', label='Obesity Line (BMI=30)')
            ax.set_title("4. BMI vs. Insurance Charges", fontsize=12, fontweight='bold', pad=10)
            ax.set_xlabel("Body Mass Index (BMI)")
            ax.set_ylabel("Charges ($ USD)")
            ax.legend(loc='upper left')
        elif "5. Region" in choice:
            reg_avg = self.df.groupby('region')['charges'].mean().reset_index()
            sns.barplot(x='region', y='charges', hue='region', data=reg_avg, palette='Blues_d', legend=False, ax=ax)
            for p in ax.patches:
                ax.annotate(f"${p.get_height():,.0f}", (p.get_x() + p.get_width() / 2., p.get_height()),
                            ha='center', va='center', xytext=(0, 6), textcoords='offset points', fontsize=9, fontweight='bold')
            ax.set_title("5. Average Charges by Region", fontsize=12, fontweight='bold', pad=10)
            ax.set_xlabel("Geographical Region")
            ax.set_ylabel("Average Charges ($ USD)")
            ax.set_ylim(0, max(reg_avg['charges']) * 1.15)
        elif "6. Sex" in choice:
            sex_avg = self.df.groupby('sex')['charges'].mean().reset_index()
            sns.barplot(x='sex', y='charges', hue='sex', data=sex_avg, palette=['#ec4899', '#3b82f6'], legend=False, ax=ax, width=0.45)
            for p in ax.patches:
                ax.annotate(f"${p.get_height():,.0f}", (p.get_x() + p.get_width() / 2., p.get_height()),
                            ha='center', va='center', xytext=(0, 6), textcoords='offset points', fontsize=9, fontweight='bold')
            ax.set_title("6. Average Charges by Sex", fontsize=12, fontweight='bold', pad=10)
            ax.set_xlabel("Sex")
            ax.set_ylabel("Average Charges ($ USD)")
            ax.set_ylim(0, max(sex_avg['charges']) * 1.15)

        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=self.plot_container)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def build_data_tab(self):
        ctrl_frame = tk.Frame(self.tab_data, bg="#f1f5f9", pady=6, padx=10)
        ctrl_frame.pack(fill=tk.X)
        
        tk.Label(ctrl_frame, text="Filter Smoker:", bg="#f1f5f9", font=("Segoe UI", 9, "bold")).pack(side=tk.LEFT, padx=(0, 4))
        self.filter_smoker = ttk.Combobox(ctrl_frame, values=["All", "no", "yes"], width=8, state="readonly")
        self.filter_smoker.set("All")
        self.filter_smoker.pack(side=tk.LEFT, padx=(0, 15))
        self.filter_smoker.bind("<<ComboboxSelected>>", lambda e: self.refresh_table())

        tk.Label(ctrl_frame, text="Filter Region:", bg="#f1f5f9", font=("Segoe UI", 9, "bold")).pack(side=tk.LEFT, padx=(0, 4))
        self.filter_region = ttk.Combobox(ctrl_frame, values=["All", "northeast", "northwest", "southeast", "southwest"], width=12, state="readonly")
        self.filter_region.set("All")
        self.filter_region.pack(side=tk.LEFT, padx=(0, 15))
        self.filter_region.bind("<<ComboboxSelected>>", lambda e: self.refresh_table())

        self.lbl_table_count = tk.Label(ctrl_frame, text="Total: 1,338 records", font=("Segoe UI", 9, "italic"), bg="#f1f5f9", fg="#475569")
        self.lbl_table_count.pack(side=tk.RIGHT, padx=10)

        # Treeview table
        columns = ("#", "Age", "Sex", "BMI", "Children", "Smoker", "Region", "Charges ($)")
        self.tree = ttk.Treeview(self.tab_data, columns=columns, show="headings", height=20)
        
        col_widths = [50, 70, 90, 90, 80, 90, 120, 130]
        for col, width in zip(columns, col_widths):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor="center" if col != "Charges ($)" else "e")

        scrollbar = ttk.Scrollbar(self.tab_data, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0), pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 10), pady=10)

        self.refresh_table()

    def refresh_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        if self.df.empty:
            return

        filtered = self.df.copy()
        s_val = self.filter_smoker.get()
        if s_val != "All":
            filtered = filtered[filtered['smoker'] == s_val]

        r_val = self.filter_region.get()
        if r_val != "All":
            filtered = filtered[filtered['region'] == r_val]

        self.lbl_table_count.config(text=f"Showing {len(filtered):,} records")

        # Load first 250 rows for smooth UI performance
        for idx, row in filtered.iloc[:250].iterrows():
            self.tree.insert("", "end", values=(
                idx + 1,
                row['age'],
                row['sex'].capitalize(),
                f"{row['bmi']:.2f}",
                row['children'],
                row['smoker'].upper(),
                row['region'].capitalize(),
                f"${row['charges']:,.2f}"
            ))

    def build_info_tab(self):
        container = tk.Frame(self.tab_info, bg="white", padx=25, pady=20)
        container.pack(fill=tk.BOTH, expand=True)

        tk.Label(container, text="Medical Cost Personal (Insurance) Data Analysis", font=("Segoe UI", 14, "bold"), bg="white", fg="#1e3a8a").pack(anchor="w", pady=(0, 5))
        tk.Label(container, text="Course: PSC(CE0525) | Class: 5 CSE-F | Indus University", font=("Segoe UI", 10, "bold"), bg="white", fg="#475569").pack(anchor="w", pady=(0, 15))

        info_text = (
            "1. Project Objectives:\n"
            "   • Clean dataset (missing values, duplicates, outliers).\n"
            "   • Conduct Exploratory Data Analysis (EDA) on 1,338 Kaggle benchmark cases.\n"
            "   • Generate 6 statistical graphs (charges histogram, smoker boxplot, age scatter, BMI scatter, region & sex barcharts).\n"
            "   • Provide an Interactive UI & Multiple Linear Regression cost predictor ($R^2 = 0.751$).\n\n"
            "2. Student Team Details:\n"
            "   • Student ID 1: IU2441230558\n"
            "   • Student ID 2: IU2441230559\n\n"
            "3. Key Findings:\n"
            "   • Smokers incur 3.8x higher premiums ($32,050 vs $8,434 for non-smokers).\n"
            "   • Individuals with BMI >= 30 and smoker status face the highest compound risk (> $40,000/yr).\n"
            "   • Age adds ~ $257/yr linearly to medical insurance costs.\n\n"
            "4. GitHub Repository:\n"
            "   • https://github.com/nandankhagram69/medical-cost-insurance-analysis"
        )
        
        tk.Label(container, text=info_text, font=("Segoe UI", 10), bg="white", fg="#334155", justify="left").pack(anchor="w", pady=10)

        btn_box = tk.Frame(container, bg="white")
        btn_box.pack(anchor="w", pady=15)

        tk.Button(btn_box, text="🌐 Open Web Dashboard in Browser", font=("Segoe UI", 10, "bold"), bg="#2563eb", fg="white", padx=10, pady=6,
                  command=lambda: os.system("start index.html")).pack(side=tk.LEFT, padx=(0, 10))

        tk.Button(btn_box, text="📄 Open Proposal PDF", font=("Segoe UI", 10), bg="#f1f5f9", padx=10, pady=6,
                  command=lambda: os.system('start "" "Python proposal.pdf"')).pack(side=tk.LEFT)

if __name__ == "__main__":
    root = tk.Tk()
    app = MedicalInsuranceApp(root)
    root.mainloop()
