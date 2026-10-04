from src.cbkb import benchmark_stats
from src.hidden_patterns import main as hp_main

def test_benchmark_counts():
    s = benchmark_stats()
    assert s["chapters"] == 34
    assert s["total_questions"] == 170
    assert sum(s["sections"].values()) == 34
    # Symptom Management is the plurality (14/34 = 41.2%)
    assert max(s["sections"].values()) == 14

def test_hidden_patterns_runs(tmp_path):
    out = hp_main()
    assert "H1_section_imbalance" in out
    assert "H3_symptom_cluster" in out
