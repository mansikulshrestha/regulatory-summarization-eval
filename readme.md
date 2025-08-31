# 📑 Regulatory Summarization Evaluation

This project evaluates **summarization models** on a **regulatory dataset** using standard metrics (**ROUGE-1, ROUGE-L, BERTScore**) and provides both **static plots** and an **interactive dashboard** for analysis.

---

## 📌 Features

- Evaluate multiple models against reference summaries
- Metrics supported:

  - **ROUGE-1**
  - **ROUGE-L**
  - **BERTScore**

- Save results to CSV (`summary_eval_scores.csv`)
- Generate **EDA plots** (bar charts across models & testcases)
- Explore results in an **interactive Dash dashboard**

---

## 📂 Project Structure

```
.
├── regulatory_summarization_dataset.json   # Input dataset
├── evaluation.py                           # Main script for computing metrics
├── eda_summary_metrics.py                  # Static visualization (matplotlib/seaborn)
├── summary_eval_dashboard.py               # Interactive dashboard (Dash/Plotly)
├── requirements.txt                        # Dependencies
├── README.md                               # Documentation
└── analysis/                               # Saved plots
```

---

## ⚙️ Installation

1. **Clone the repo**

   ```bash
   git clone git@github.com:mansikulshrestha/regulatory-summarization-eval.git
   cd regulatory-summarization-eval
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

### 1. Run Evaluation

Compute ROUGE & BERTScore metrics and save results to CSV:

```bash
python evaluation.py
```

Output:

- Tabulated scores in terminal
- `summary_eval_scores.csv` file with all results

---

### 2. Generate EDA Plots

Barplots comparing models across metrics:

```bash
python eda_summary_metrics.py
```

Plots will be saved in the `analysis/` folder.

---

### 3. Launch Interactive Dashboard

Explore results dynamically with Dash:

```bash
python summary_eval_dashboard.py
```

Go to → [http://127.0.0.1:8050](http://127.0.0.1:8050) in your browser.

---

## 📊 Example Output

### Tabulated Results

```
╒══════════════╤══════════╤════════════════╤════════════════╤═══════════╕
│ Testcase ID  │ Model    │ ROUGE-1 Score  │ ROUGE-L Score  │ BERTScore │
╞══════════════╪══════════╪════════════════╪════════════════╪═══════════╡
│ 0            │ model_1  │ 0.55           │ 0.50           │ 0.84      │
│ 0            │ model_2  │ 0.62           │ 0.58           │ 0.86      │
│ 0            │ model_3  │ 0.42           │ 0.39           │ 0.77      │
╘══════════════╧══════════╧════════════════╧════════════════╧═══════════╛
```

### Dashboard Screenshot

---

## 📌 Future Improvements

- Add more evaluation metrics (BLEU, METEOR, etc.)
- Deploy dashboard on Render/Streamlit Cloud
- Extend dataset for other regulatory bodies

---

## 🛠️ Tech Stack

- **Python** (pandas, numpy)
- **Metrics**: `rouge-score`, `bert-score`
- **Visualization**: matplotlib, seaborn, plotly, dash
- **Utils**: tqdm, tabulate

---

## 👤 Author

**Mansi Kulshrestha**

🔗 [GitHub](https://github.com/mansikulshrestha) | [LinkedIn](https://www.linkedin.com/in/mansikulshrestha)
