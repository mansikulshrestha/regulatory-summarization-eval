import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set up plotting style
sns.set(style="whitegrid")

# File & folder config
CSV_FILE = "summary_eval_scores.csv"
SAVE_DIR = "analysis"
os.makedirs(SAVE_DIR, exist_ok=True)

# Load dataset
df = pd.read_csv(CSV_FILE)


def plot_metric_grouped(df, metric_names):
    for metric in metric_names:
        if metric not in df.columns:
            continue

        plt.figure(figsize=(12, 6))
        sns.barplot(
            data=df,
            x="Testcase ID",
            y=metric,
            hue="Model",
            palette="Set2"
        )
        plt.title(f"{metric} Comparison Across Models")
        plt.ylabel(metric)
        plt.xticks(rotation=45)
        plt.tight_layout()

        filename = os.path.join(SAVE_DIR, f"{metric.lower().replace(' ', '_')}_scores.png")
        plt.savefig(filename)
        print(f"📈 Saved: {filename}")
        plt.show()


def main():
    print("📊 Generating EDA Charts...")

    # Only metrics we now have
    metrics_to_plot = ["ROUGE-1 Score", "ROUGE-L Score", "BERTScore"]
    plot_metric_grouped(df, metrics_to_plot)

    print(f"\n✅ All plots saved to ./{SAVE_DIR}/")


if __name__ == "__main__":
    main()
