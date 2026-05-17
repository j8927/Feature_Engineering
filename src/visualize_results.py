from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_metrics(results: pd.DataFrame, fig_dir: str = "results/figures"):
    Path(fig_dir).mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(10, 5))
    sns.barplot(data=results, x="Experiment", y="F1", hue="Model")
    plt.title("F1-score by Experiment and Model")
    plt.ylim(0, 1)
    plt.tight_layout()
    plt.savefig(Path(fig_dir) / "comparison_f1.png", dpi=150)
    plt.close()

    plt.figure(figsize=(10, 5))
    sns.barplot(data=results, x="Experiment", y="ROC_AUC", hue="Model")
    plt.title("ROC-AUC by Experiment and Model")
    plt.ylim(0, 1)
    plt.tight_layout()
    plt.savefig(Path(fig_dir) / "comparison_roc_auc.png", dpi=150)
    plt.close()
