import json
import pandas as pd
from typing import List, Dict
from tabulate import tabulate
from rouge_score import rouge_scorer
import bert_score


# ---- Metrics ----
class RougeMetric:
    def measure(self, reference: str, summary: str) -> Dict[str, float]:
        scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
        scores = scorer.score(reference, summary)
        return {k: v.fmeasure for k, v in scores.items()}


class BertScoreMetric:
    def measure(self, reference: str, summary: str) -> float:
        _, _, f1 = bert_score.score([summary], [reference], lang="en", verbose=False)
        return f1[0].item()


# ---- Dataset Helpers ----
def load_dataset_to_dataframe(json_path: str, models: List[str]) -> pd.DataFrame:
    with open(json_path, 'r') as f:
        raw_data = json.load(f)

    records = []
    for idx, item in enumerate(raw_data):
        row = {
            "Testcase ID": idx,
            "Source": item["source"],
            "Reference Summary": item.get("reference_summary", "")
        }
        for model in models:
            row[f"{model}_Summary"] = item.get(f"{model}_summary", "")
        records.append(row)

    return pd.DataFrame(records)


# ---- Evaluation ----
def evaluate_all_metrics(reference: str, summary: str) -> Dict:
    rouge = RougeMetric().measure(reference, summary)
    bert = BertScoreMetric().measure(reference, summary)
    return {
        "ROUGE-1 Score": rouge["rouge1"],
        "ROUGE-L Score": rouge["rougeL"],
        "BERTScore": bert
    }


def evaluate_and_format_results(df: pd.DataFrame, models: List[str]) -> pd.DataFrame:
    all_results = []

    for _, row in df.iterrows():
        for model in models:
            summary = row[f"{model}_Summary"]
            reference = row["Reference Summary"]

            results = evaluate_all_metrics(reference, summary)

            flat_result = {
                "Testcase ID": row["Testcase ID"],
                "Model": model,
                **results
            }
            all_results.append(flat_result)

    return pd.DataFrame(all_results)


# ---- Main ----
def main():
    dataset_file = "regulatory_summarization_dataset.json"
    test_models = ['model_1', 'model_2', 'model_3']

    df = load_dataset_to_dataframe(dataset_file, test_models)
    results_df = evaluate_and_format_results(df, test_models)

    # Display nicely in terminal
    print(tabulate(results_df, headers='keys', tablefmt='fancy_grid', showindex=False))

    # Save results
    results_df.to_csv("summary_eval_scores.csv", index=False)
    print("\n✅ Results saved to summary_eval_scores.csv")


if __name__ == "__main__":
    main()
