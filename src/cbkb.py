"""CBKB-34: Cancer Basics Knowledge Benchmark (34 chapters, 2nd Ed. grounded)."""
from dataclasses import dataclass

@dataclass
class Chapter:
    n: int
    title: str
    section: str
    questions: int = 5

SECTIONS = {
    "I Foundations": [1, 2, 3, 4, 5, 6],
    "II Treatment Options": [7, 8, 9, 10, 11, 12, 13, 14],
    "III Symptom Management": [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
    "IV Survivorship & Family": [29, 30, 31, 32, 33, 34],
}

CHAPTERS = [
    (1, "Biology of Cancer"), (2, "Staging and Performance Status"),
    (3, "Cancer Epidemiology and Prevention"), (4, "Genetic Risk for Developing Cancer"),
    (5, "Cancer Detection Measures"), (6, "Pharmacogenomics"),
    (7, "Surgery"), (8, "Radiation Therapy"), (9, "Chemotherapy"),
    (10, "Precision Medicine: Biologics and Targeted Therapies"),
    (11, "Hormone Therapy"), (12, "Clinical Trials"),
    (13, "Complementary and Alternative Medicine"), (14, "Hematopoietic Stem Cell Transplantation"),
    (15, "Alopecia"), (16, "Cardiotoxicity"), (17, "Cognitive Changes"),
    (18, "Dermatologic Complications"), (19, "Fatigue"), (20, "Gastrointestinal Symptoms"),
    (21, "Genitourinary Symptoms"), (22, "Hematologic Issues"), (23, "Hepatic Toxicities"),
    (24, "Hypersensitivity"), (25, "Oncologic Emergencies"), (26, "Pain"),
    (27, "Peripheral Neuropathy"), (28, "Pulmonary Toxicities"),
    (29, "Developmental Life Stage Issues"), (30, "Ethical Issues"),
    (31, "Palliative Care"), (32, "Psychosocial Issues"),
    (33, "Sexual and Reproductive Issues"), (34, "Caring for the Cancer Survivor"),
]

def section_of(n: int) -> str:
    for s, ns in SECTIONS.items():
        if n in ns:
            return s
    return "?"

def benchmark_stats():
    total_q = len(CHAPTERS) * 5
    return {
        "chapters": len(CHAPTERS),
        "total_questions": total_q,
        "sections": {k: len(v) for k, v in SECTIONS.items()},
    }

if __name__ == "__main__":
    print(benchmark_stats())
