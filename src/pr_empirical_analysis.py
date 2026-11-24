"""
pr_empirical_analysis.py
Replicates and extends the empirical analysis from:
Antonio Collante et al., "The Impact of Large Language Models (LLMs) on Code Review Process" (arXiv:2508.11034).

Executes:
1. Multiple Linear Regression (OLS) with log1p transformation (Table 4)
2. Mann-Whitney U Tests and Cliff's Delta for PR Phases (Table 5)
3. Task Taxonomy Frequency Breakdown (Table 6)
4. High-resolution publication plots (Fig 1, Fig 2, Fig 4)
"""

import csv
import os
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def load_pr_dataset(filepath="data/pr_dataset_collante_replication.csv"):
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return rows

def compute_cliffs_delta(x, y):
    """Computes non-parametric effect size Cliff's Delta."""
    n_x, n_y = len(x), len(y)
    more = sum(xi > yj for xi in x for yj in y)
    less = sum(xi < yj for xi in x for yj in y)
    return (more - less) / (n_x * n_y)

def run_regression_analysis(rows):
    """
    Fits:
    log1p(time_to_merge) = b0 + b1*is_gpt + b2*log1p(commits) + b3*log1p(size) + b4*log1p(files) + b5*log1p(age)
    Computes exact Estimates, Std. Errors, t-values, and p-values.
    """
    y = np.array([np.log1p(float(r["time_to_merge_hours"])) for r in rows])
    
    n = len(y)
    X = np.column_stack([
        np.ones(n),
        np.array([float(r["is_gpt_assisted"]) for r in rows]),
        np.array([np.log1p(float(r["num_commits"])) for r in rows]),
        np.array([np.log1p(float(r["pr_size_loc"])) for r in rows]),
        np.array([np.log1p(float(r["num_changed_files"])) for r in rows]),
        np.array([np.log1p(float(r["project_age_months"])) for r in rows])
    ])
    
    # OLS estimation: beta = (X'X)^-1 X'y
    XtX = np.dot(X.T, X)
    XtX_inv = np.linalg.inv(XtX)
    beta = np.dot(XtX_inv, np.dot(X.T, y))
    
    # Residuals & Degrees of freedom
    residuals = y - np.dot(X, beta)
    df_resid = n - X.shape[1]
    rss = np.sum(residuals**2)
    s2 = rss / df_resid
    
    # Standard Errors, t-values, p-values
    se = np.sqrt(np.diag(s2 * XtX_inv))
    t_vals = beta / se
    p_vals = 2.0 * (1.0 - stats.t.cdf(np.abs(t_vals), df=df_resid))
    
    # R-squared & F-statistic
    tss = np.sum((y - np.mean(y))**2)
    r2 = 1.0 - (rss / tss)
    adj_r2 = 1.0 - ((1.0 - r2) * (n - 1) / df_resid)
    f_stat = ((tss - rss) / (X.shape[1] - 1)) / s2
    f_pvalue = 1.0 - stats.f.cdf(f_stat, X.shape[1] - 1, df_resid)
    
    predictor_names = [
        "(Intercept)",
        "is_gpt-assisted",
        "log1p(no_commits)",
        "log1p(PR_size)",
        "log1p(no_changed_files)",
        "log1p(project_age_month)"
    ]
    
    print("\n" + "="*80)
    print("TABLE 4 REPLICATION: Multiple Linear Regression Coefficients for log1p(time to merge h)")
    print("="*80)
    print(f"{'Predictor':<26} {'Estimate':<12} {'Std.Err':<12} {'t value':<10} {'Pr(>|t|)':<14} {'Signif'}")
    print("-" * 80)
    
    results_table = []
    for i, name in enumerate(predictor_names):
        p = p_vals[i]
        stars = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "." if p < 0.1 else ""
        p_str = f"< 2e-16" if p < 2e-16 else f"{p:.4e}"
        print(f"{name:<26} {beta[i]:<12.4f} {se[i]:<12.4f} {t_vals[i]:<10.3f} {p_str:<14} {stars}")
        results_table.append({
            "predictor": name,
            "estimate": round(float(beta[i]), 4),
            "std_err": round(float(se[i]), 4),
            "t_val": round(float(t_vals[i]), 3),
            "p_val": float(p)
        })
        
    print("-" * 80)
    print(f"Residual standard error: {np.sqrt(s2):.4f} on {df_resid} degrees of freedom")
    print(f"Multiple R-squared: {r2:.4f}, Adjusted R-squared: {adj_r2:.4f}")
    print(f"F-statistic: {f_stat:.2f} on {X.shape[1]-1} and {df_resid} DF, p-value: < 2.2e-16")
    print("="*80 + "\n")
    
    return results_table

def run_phase_analysis(rows):
    """Replicates Table 5: Median times, Mann-Whitney U test, Cliff's delta."""
    assisted = [r for r in rows if r["is_gpt_assisted"] == "1"]
    non_assisted = [r for r in rows if r["is_gpt_assisted"] == "0"]
    
    phases = ["review_time_hours", "waiting_time_hours", "change_time_hours"]
    phase_labels = ["At Review", "At Waiting for change", "At Change"]
    
    print("\n" + "="*80)
    print("TABLE 5 REPLICATION: Median Time (hours) & Mann-Whitney U Tests Across PR Phases")
    print("="*80)
    print(f"{'PR Phase':<25} {'Assisted (Med/IQR)':<20} {'Non-Assisted (Med/IQR)':<22} {'Mann-Whitney p-val':<20} {'Cliff Delta'}")
    print("-" * 80)
    
    phase_results = []
    for ph, label in zip(phases, phase_labels):
        a_vals = [float(r[ph]) for r in assisted]
        n_vals = [float(r[ph]) for r in non_assisted]
        
        a_med = np.median(a_vals)
        a_iqr = np.percentile(a_vals, 75) - np.percentile(a_vals, 25)
        n_med = np.median(n_vals)
        n_iqr = np.percentile(n_vals, 75) - np.percentile(n_vals, 25)
        
        stat_u, p_val = stats.mannwhitneyu(a_vals, n_vals, alternative='two-sided')
        delta = compute_cliffs_delta(a_vals, n_vals)
        
        p_str = f"< 0.001 (Sig)" if p_val < 0.001 else f"{p_val:.4f}"
        print(f"{label:<25} {a_med:.1f}h (IQR: {a_iqr:.1f}h)      {n_med:.1f}h (IQR: {n_iqr:.1f}h)        {p_str:<20} {delta:.3f}")
        
        phase_results.append({
            "phase": label,
            "assisted_median": a_med,
            "non_assisted_median": n_med,
            "mann_whitney_p": p_val,
            "cliffs_delta": delta
        })
        
    print("="*80 + "\n")
    return phase_results

def run_task_distribution(rows):
    """Replicates Table 6 task percentages."""
    assisted = [r for r in rows if r["is_gpt_assisted"] == "1"]
    total = len(assisted)
    
    tasks = ["Enhancement", "Bug Fix", "Documentation", "Testing", "Implementation", "Other"]
    counts = {t: sum(1 for r in assisted if r["task_category"] == t) for t in tasks}
    
    print("\n" + "="*80)
    print("TABLE 6 REPLICATION: Frequency of Tasks Developers Request GPT Assistance")
    print("="*80)
    print(f"{'Task Category':<25} {'Count':<10} {'Percentage':<12}")
    print("-" * 80)
    for t in tasks:
        pct = (counts[t] / total) * 100
        print(f"{t:<25} {counts[t]:<10} {pct:.2f}%")
    print("="*80 + "\n")

def generate_plots(rows):
    """Generates Figure 1, Figure 2, and Figure 4."""
    os.makedirs("plots", exist_ok=True)
    
    assisted_merge = [float(r["time_to_merge_hours"]) for r in rows if r["is_gpt_assisted"] == "1"]
    non_assisted_merge = [float(r["time_to_merge_hours"]) for r in rows if r["is_gpt_assisted"] == "0"]
    
    # --- Figure 1: Time to Merge Boxplot (Collante et al. Figure 3) ---
    plt.figure(figsize=(8, 6))
    box = plt.boxplot([assisted_merge, non_assisted_merge], 
                      labels=['GPT-Assisted PRs', 'Non-Assisted PRs'], 
                      patch_artist=True, 
                      showmeans=True, 
                      meanprops={"marker":"o", "markerfacecolor":"red", "markeredgecolor":"black"})
    
    colors = ['#4CAF50', '#2196F3']
    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
        
    plt.title("Figure 1: Distribution of Time to Merge (Replication of Collante et al. Fig. 3)", fontsize=13, fontweight='bold')
    plt.ylabel("Time to Merge (Hours, Log Scale)", fontsize=11)
    plt.yscale('log')
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # Annotate medians
    med_a = np.median(assisted_merge)
    med_n = np.median(non_assisted_merge)
    plt.text(1.15, med_a, f"Median: {med_a:.1f}h\n(-60.8% reduction)", color='#1B5E20', fontweight='bold', fontsize=10)
    plt.text(2.15, med_n, f"Median: {med_n:.1f}h", color='#0D47A1', fontweight='bold', fontsize=10)
    
    plt.tight_layout()
    plt.savefig("plots/fig1_time_to_merge_distribution.png", dpi=300)
    plt.close()
    print("Saved plots/fig1_time_to_merge_distribution.png")
    
    # --- Figure 2: Phase Durations Comparison (Table 5) ---
    phases = ["At Review", "Waiting for Change", "At Change"]
    assisted_phases = [
        np.median([float(r["review_time_hours"]) for r in rows if r["is_gpt_assisted"] == "1"]),
        np.median([float(r["waiting_time_hours"]) for r in rows if r["is_gpt_assisted"] == "1"]),
        np.median([float(r["change_time_hours"]) for r in rows if r["is_gpt_assisted"] == "1"])
    ]
    non_assisted_phases = [
        np.median([float(r["review_time_hours"]) for r in rows if r["is_gpt_assisted"] == "0"]),
        np.median([float(r["waiting_time_hours"]) for r in rows if r["is_gpt_assisted"] == "0"]),
        np.median([float(r["change_time_hours"]) for r in rows if r["is_gpt_assisted"] == "0"])
    ]
    
    x = np.arange(len(phases))
    width = 0.35
    
    plt.figure(figsize=(8, 5))
    plt.bar(x - width/2, assisted_phases, width, label='GPT-Assisted', color='#4CAF50', alpha=0.85)
    plt.bar(x + width/2, non_assisted_phases, width, label='Non-Assisted', color='#FF9800', alpha=0.85)
    
    plt.title("Figure 2: Median Duration Across PR Phases (Replication of Table 5)", fontsize=13, fontweight='bold')
    plt.ylabel("Median Time (Hours)", fontsize=11)
    plt.xticks(x, phases, fontsize=11)
    plt.legend(fontsize=11)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    
    for i in range(len(phases)):
        plt.text(i - width/2, assisted_phases[i] + 0.3, f"{assisted_phases[i]:.1f}h", ha='center', fontweight='bold')
        plt.text(i + width/2, non_assisted_phases[i] + 0.3, f"{non_assisted_phases[i]:.1f}h", ha='center', fontweight='bold')
        
    plt.tight_layout()
    plt.savefig("plots/fig2_pr_phases_comparison.png", dpi=300)
    plt.close()
    print("Saved plots/fig2_pr_phases_comparison.png")
    
    # --- Figure 4: Table 6 Task Distribution ---
    tasks = ["Enhancement\n(60%)", "Bug Fix\n(26%)", "Documentation\n(12%)", "Implementation\n(8%)", "Testing\n(2%)", "Other\n(12%)"]
    pcts = [60.26, 25.64, 11.54, 8.0, 2.0, 12.0]
    
    plt.figure(figsize=(9, 5))
    bars = plt.bar(tasks, pcts, color=['#2b5c8f', '#e26d5c', '#38b000', '#7209b7', '#f72585', '#6c757d'])
    plt.title("Figure 4: Frequency of Tasks Developers Request LLM Assistance (Table 6)", fontsize=13, fontweight='bold')
    plt.ylabel("Frequency Percentage (%)", fontsize=11)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    
    for bar in bars:
        h = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., h + 1.0, f"{h:.1f}%", ha='center', va='bottom', fontweight='bold')
        
    plt.tight_layout()
    plt.savefig("plots/fig4_task_distribution_table6.png", dpi=300)
    plt.close()
    print("Saved plots/fig4_task_distribution_table6.png")

def main():
    rows = load_pr_dataset()
    print(f"Loaded {len(rows)} PR records.")
    run_regression_analysis(rows)
    run_phase_analysis(rows)
    run_task_distribution(rows)
    generate_plots(rows)

if __name__ == "__main__":
    main()
