"""
run_full_experiment.py
Master Experiment Runner for UAS Software Quality Assurance (SQA):
"Empirical Study on Large Language Models (LLMs) and Oracle AI Vector Search
for Automated Modern Code Review"

Integrates:
1. Replicating Antonio Collante et al. (arXiv:2508.11034) PR Dataset & Statistical Modeling (Table 4, Table 5, Table 6)
2. Oracle Database 23ai AI Vector Search Engine & Vector Distance functions (Cosine, Manhattan, Euclidean)
3. SQA Benchmark Evaluation (N = 100 cases) across Baseline, Vanilla LLM, and Oracle Vector RAG
4. Generating all visualization plots (plots/fig1..fig4)
5. Exporting summary metrics for reporting
"""

import os
import sys
import time

def main():
    print("=" * 80)
    print("STARTING COMPLETE EMPIRICAL EXPERIMENT & BENCHMARK PIPELINE")
    print("=" * 80)
    start_time = time.time()
    
    # Step 1: Ensure dataset files exist
    print("\n>>> STEP 1: Verifying Datasets & Knowledge Base...")
    from pr_dataset_generator import generate_replication_dataset
    from sqa_knowledge_base_generator import create_knowledge_base
    from sqa_ground_truth_generator import generate_ground_truth_benchmark
    
    generate_replication_dataset()
    create_knowledge_base()
    generate_ground_truth_benchmark()
    
    # Step 2: Run Empirical Analysis (Collante et al. Replication)
    print("\n>>> STEP 2: Running Empirical Statistical Modeling (Collante et al. Replication)...")
    from pr_empirical_analysis import main as run_pr_analysis
    run_pr_analysis()
    
    # Step 3: Run SQA Benchmark Evaluation (Oracle AI Vector Search + RAG)
    print("\n>>> STEP 3: Running SQA Benchmark Evaluation across 3 Review Strategies...")
    from evaluate_sqa_benchmark import main as run_benchmark
    run_benchmark()
    
    elapsed = time.time() - start_time
    print("=" * 80)
    print(f"EXPERIMENT COMPLETED SUCCESSFULLY IN {elapsed:.2f} SECONDS")
    print("All plots generated in 'plots/' and metric summaries in 'results/'")
    print("=" * 80)

if __name__ == "__main__":
    # Ensure src is in sys.path
    src_dir = os.path.join(os.path.dirname(__file__), "src")
    if src_dir not in sys.path:
        sys.path.insert(0, src_dir)
    main()
