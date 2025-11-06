"""
COMPAS Recidivism Dataset Bias Audit
Using AI Fairness 360 to analyze racial bias in risk scores

Requirements:
pip install aif360 pandas numpy matplotlib seaborn scikit-learn
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from aif360.datasets import BinaryLabelDataset
from aif360.metrics import BinaryLabelDatasetMetric, ClassificationMetric
from aif360.algorithms.preprocessing import Reweighing
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# ============================================================================
# STEP 1: Load and Prepare COMPAS Data
# ============================================================================

def load_compas_data():
    """
    Load COMPAS dataset from ProPublica's analysis
    Source: https://github.com/propublica/compas-analysis
    """
    # If you have the CSV file locally, use:
    # df = pd.read_csv('compas-scores-two-years.csv')
    
    # For demonstration, we'll use the processed version available via AIF360
    from aif360.datasets import CompasDataset
    
    dataset_orig = CompasDataset()
    df = dataset_orig.convert_to_dataframe()[0]
    
    print("Dataset Shape:", df.shape)
    print("\nColumns:", df.columns.tolist())
    print("\nFirst few rows:")
    print(df.head())
    
    return df, dataset_orig

# ============================================================================
# STEP 2: Exploratory Data Analysis
# ============================================================================

def exploratory_analysis(df, dataset_orig):
    """Analyze dataset composition and initial bias indicators"""
    
    print("\n" + "="*80)
    print("EXPLORATORY DATA ANALYSIS")
    print("="*80)
    
    # Distribution of race
    print("\nRace Distribution:")
    print(df['race'].value_counts())
    
    # Recidivism rates by race
    print("\nRecidivism Rates by Race:")
    recidivism_by_race = df.groupby('race')['two_year_recid'].mean()
    print(recidivism_by_race.sort_values(ascending=False))
    
    # COMPAS score distribution by race
    print("\nAverage COMPAS Decile Score by Race:")
    compas_by_race = df.groupby('race')['decile_score'].mean()
    print(compas_by_race.sort_values(ascending=False))
    
    # Create visualizations
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # Plot 1: Race distribution
    race_counts = df['race'].value_counts()
    axes[0, 0].bar(race_counts.index, race_counts.values, color='skyblue')
    axes[0, 0].set_title('Distribution of Race in Dataset', fontsize=14, fontweight='bold')
    axes[0, 0].set_xlabel('Race')
    axes[0, 0].set_ylabel('Count')
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # Plot 2: Recidivism rates by race
    axes[0, 1].bar(recidivism_by_race.index, recidivism_by_race.values, color='coral')
    axes[0, 1].set_title('Actual Two-Year Recidivism Rates by Race', fontsize=14, fontweight='bold')
    axes[0, 1].set_xlabel('Race')
    axes[0, 1].set_ylabel('Recidivism Rate')
    axes[0, 1].tick_params(axis='x', rotation=45)
    axes[0, 1].axhline(y=df['two_year_recid'].mean(), color='red', 
                       linestyle='--', label='Overall Average')
    axes[0, 1].legend()
    
    # Plot 3: COMPAS score distribution by race
    axes[1, 0].bar(compas_by_race.index, compas_by_race.values, color='lightgreen')
    axes[1, 0].set_title('Average COMPAS Risk Score by Race', fontsize=14, fontweight='bold')
    axes[1, 0].set_xlabel('Race')
    axes[1, 0].set_ylabel('Average Decile Score')
    axes[1, 0].tick_params(axis='x', rotation=45)
    axes[1, 0].axhline(y=df['decile_score'].mean(), color='red', 
                       linestyle='--', label='Overall Average')
    axes[1, 0].legend()
    
    # Plot 4: Score distribution comparison
    african_american_scores = df[df['race'] == 'African-American']['decile_score']
    caucasian_scores = df[df['race'] == 'Caucasian']['decile_score']
    
    axes[1, 1].hist([caucasian_scores, african_american_scores], 
                    bins=10, label=['Caucasian', 'African-American'],
                    color=['blue', 'orange'], alpha=0.7)
    axes[1, 1].set_title('COMPAS Score Distribution: Caucasian vs African-American', 
                         fontsize=14, fontweight='bold')
    axes[1, 1].set_xlabel('Decile Score')
    axes[1, 1].set_ylabel('Frequency')
    axes[1, 1].legend()
    
    plt.tight_layout()
    plt.savefig('compas_exploratory_analysis.png', dpi=300, bbox_inches='tight')
    print("\n✓ Saved: compas_exploratory_analysis.png")
    plt.show()

# ============================================================================
# STEP 3: Fairness Metrics Analysis
# ============================================================================

def analyze_fairness_metrics(dataset_orig):
    """Calculate comprehensive fairness metrics"""
    
    print("\n" + "="*80)
    print("FAIRNESS METRICS ANALYSIS")
    print("="*80)
    
    # Define privileged and unprivileged groups
    privileged_groups = [{'race': 1}]  # Caucasian
    unprivileged_groups = [{'race': 0}]  # African-American
    
    # Calculate dataset metrics
    metric_orig = BinaryLabelDatasetMetric(
        dataset_orig,
        unprivileged_groups=unprivileged_groups,
        privileged_groups=privileged_groups
    )
    
    print("\n--- DATASET FAIRNESS METRICS ---")
    print(f"Statistical Parity Difference: {metric_orig.statistical_parity_difference():.4f}")
    print("  (Difference in positive prediction rates between groups)")
    print("  Interpretation: 0 = perfect fairness, <0 = disadvantages unprivileged group")
    
    print(f"\nDisparate Impact: {metric_orig.disparate_impact():.4f}")
    print("  (Ratio of positive prediction rates)")
    print("  Interpretation: 1 = perfect fairness, <0.8 = significant bias")
    
    print(f"\nBase Rate Difference: {metric_orig.base_rate():.4f}")
    print("  (Difference in actual positive outcomes between groups)")
    
    # Calculate classification metrics if predictions are available
    # For COMPAS, the 'score' is the prediction, 'two_year_recid' is the ground truth
    
    return metric_orig

# ============================================================================
# STEP 4: False Positive/Negative Rate Analysis
# ============================================================================

def analyze_error_rates(df):
    """Analyze false positive and false negative rates by race"""
    
    print("\n" + "="*80)
    print("ERROR RATE ANALYSIS")
    print("="*80)
    
    # Define "high risk" as score >= 5 (medium to high risk)
    df['predicted_recid'] = (df['decile_score'] >= 5).astype(int)
    
    # Calculate confusion matrix metrics by race
    results = []
    
    for race in ['Caucasian', 'African-American']:
        race_df = df[df['race'] == race]
        
        # True Positives: Predicted recidivism AND actually recidivated
        tp = ((race_df['predicted_recid'] == 1) & (race_df['two_year_recid'] == 1)).sum()
        
        # False Positives: Predicted recidivism but did NOT recidivate
        fp = ((race_df['predicted_recid'] == 1) & (race_df['two_year_recid'] == 0)).sum()
        
        # True Negatives: Predicted no recidivism AND did not recidivate
        tn = ((race_df['predicted_recid'] == 0) & (race_df['two_year_recid'] == 0)).sum()
        
        # False Negatives: Predicted no recidivism but DID recidivate
        fn = ((race_df['predicted_recid'] == 0) & (race_df['two_year_recid'] == 1)).sum()
        
        # Calculate rates
        fpr = fp / (fp + tn) if (fp + tn) > 0 else 0  # False Positive Rate
        fnr = fn / (fn + tp) if (fn + tp) > 0 else 0  # False Negative Rate
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        
        results.append({
            'Race': race,
            'False Positive Rate': fpr,
            'False Negative Rate': fnr,
            'Precision': precision,
            'Recall': recall,
            'Total': len(race_df)
        })
        
        print(f"\n{race}:")
        print(f"  Total cases: {len(race_df)}")
        print(f"  False Positive Rate: {fpr:.4f} ({fp}/{fp+tn} of non-recidivists)")
        print(f"  False Negative Rate: {fnr:.4f} ({fn}/{fn+tp} of recidivists)")
        print(f"  Precision: {precision:.4f}")
        print(f"  Recall: {recall:.4f}")
    
    # Create visualization
    results_df = pd.DataFrame(results)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # False Positive Rates
    axes[0].bar(results_df['Race'], results_df['False Positive Rate'], 
                color=['blue', 'orange'], alpha=0.7)
    axes[0].set_title('False Positive Rates by Race\n(Incorrectly Labeled as High Risk)', 
                     fontsize=14, fontweight='bold')
    axes[0].set_ylabel('False Positive Rate')
    axes[0].set_ylim(0, max(results_df['False Positive Rate']) * 1.2)
    
    # Add value labels
    for i, v in enumerate(results_df['False Positive Rate']):
        axes[0].text(i, v + 0.01, f'{v:.3f}', ha='center', fontweight='bold')
    
    # False Negative Rates
    axes[1].bar(results_df['Race'], results_df['False Negative Rate'], 
                color=['blue', 'orange'], alpha=0.7)
    axes[1].set_title('False Negative Rates by Race\n(Incorrectly Labeled as Low Risk)', 
                     fontsize=14, fontweight='bold')
    axes[1].set_ylabel('False Negative Rate')
    axes[1].set_ylim(0, max(results_df['False Negative Rate']) * 1.2)
    
    # Add value labels
    for i, v in enumerate(results_df['False Negative Rate']):
        axes[1].text(i, v + 0.01, f'{v:.3f}', ha='center', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('compas_error_rates.png', dpi=300, bbox_inches='tight')
    print("\n✓ Saved: compas_error_rates.png")
    plt.show()
    
    return results_df

# ============================================================================
# STEP 5: Bias Mitigation with Reweighing
# ============================================================================

def mitigate_bias(dataset_orig):
    """Apply reweighing algorithm to mitigate bias"""
    
    print("\n" + "="*80)
    print("BIAS MITIGATION - REWEIGHING")
    print("="*80)
    
    privileged_groups = [{'race': 1}]
    unprivileged_groups = [{'race': 0}]
    
    # Apply reweighing
    RW = Reweighing(unprivileged_groups=unprivileged_groups,
                    privileged_groups=privileged_groups)
    dataset_transf = RW.fit_transform(dataset_orig)
    
    # Calculate metrics before and after
    metric_orig = BinaryLabelDatasetMetric(
        dataset_orig,
        unprivileged_groups=unprivileged_groups,
        privileged_groups=privileged_groups
    )
    
    metric_transf = BinaryLabelDatasetMetric(
        dataset_transf,
        unprivileged_groups=unprivileged_groups,
        privileged_groups=privileged_groups
    )
    
    print("\nBEFORE Mitigation:")
    print(f"  Statistical Parity Difference: {metric_orig.statistical_parity_difference():.4f}")
    print(f"  Disparate Impact: {metric_orig.disparate_impact():.4f}")
    
    print("\nAFTER Mitigation:")
    print(f"  Statistical Parity Difference: {metric_transf.statistical_parity_difference():.4f}")
    print(f"  Disparate Impact: {metric_transf.disparate_impact():.4f}")
    
    # Visualize improvement
    metrics = ['Statistical Parity\nDifference', 'Disparate Impact']
    before = [metric_orig.statistical_parity_difference(), metric_orig.disparate_impact()]
    after = [metric_transf.statistical_parity_difference(), metric_transf.disparate_impact()]
    
    x = np.arange(len(metrics))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x - width/2, before, width, label='Before Mitigation', color='coral')
    ax.bar(x + width/2, after, width, label='After Mitigation', color='lightgreen')
    
    ax.set_ylabel('Metric Value')
    ax.set_title('Fairness Metrics: Before vs After Bias Mitigation', 
                 fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(metrics)
    ax.legend()
    ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax.axhline(y=0.8, color='red', linestyle='--', linewidth=1, alpha=0.5, 
               label='Disparate Impact Threshold (0.8)')
    
    plt.tight_layout()
    plt.savefig('compas_bias_mitigation.png', dpi=300, bbox_inches='tight')
    print("\n✓ Saved: compas_bias_mitigation.png")
    plt.show()

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function"""
    
    print("="*80)
    print("COMPAS RECIDIVISM DATASET - RACIAL BIAS AUDIT")
    print("Using AI Fairness 360 Toolkit")
    print("="*80)
    
    # Load data
    df, dataset_orig = load_compas_data()
    
    # Exploratory analysis
    exploratory_analysis(df, dataset_orig)
    
    # Fairness metrics
    analyze_fairness_metrics(dataset_orig)
    
    # Error rate analysis
    error_results = analyze_error_rates(df)
    
    # Bias mitigation
    mitigate_bias(dataset_orig)
    
    print("\n" + "="*80)
    print("AUDIT COMPLETE")
    print("="*80)
    print("\nGenerated files:")
    print("  1. compas_exploratory_analysis.png")
    print("  2. compas_error_rates.png")
    print("  3. compas_bias_mitigation.png")
    print("\nNext steps: Review the 300-word report below")

if __name__ == "__main__":
    main()
