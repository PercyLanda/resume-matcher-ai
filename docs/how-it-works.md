# How It Works

## Purpose

Resume Matcher AI evaluates alignment between a resume and a job description by combining:

- Semantic similarity scoring with sentence embeddings.
- Keyword overlap extraction for interpretability.

The design goal is to provide both a quantitative signal (`match score`) and a human-readable explanation (`common terms`).

## System Components

- `src/main.py`: command-line entry point and output formatting.
- `src/embedder.py`: model loading, similarity scoring, and keyword extraction.
- `data/raw/resume.txt`: resume input text.
- `data/raw/job.txt`: job description input text.
- `tests/test_embedder.py`: unit tests for core matching logic.

## Runtime Flow

When `python src/main.py` is executed, the following sequence occurs:

1. The script resolves project paths and reads `resume.txt` and `job.txt`.
2. `ResumeMatcher` is initialized.
3. The embedding model (`all-MiniLM-L6-v2`) is loaded through `sentence-transformers`.
4. The spaCy pipeline (`en_core_web_sm`) is loaded.
5. Both documents are encoded into dense vectors.
6. Cosine similarity is calculated between the two vectors.
7. Keywords are extracted from both texts using token filters and lemma normalization.
8. Overlapping terms are split into:
   - `common_skills`: overlaps matching the skill/domain whitelist.
   - `common_other`: additional overlaps.
9. A final report is printed.

## Scoring Method

`compute_similarity` uses cosine similarity:

`similarity(A, B) = (A · B) / (||A|| * ||B||)`

Interpretation guidance:

- Closer to `1.0`: stronger semantic alignment.
- Mid-range values: partial alignment.
- Closer to `0.0`: weaker alignment.

This score reflects textual alignment, not hiring probability.

## Keyword and Explanation Logic

`extract_keywords` applies a lightweight NLP pipeline:

- Lowercases and tokenizes text with spaCy.
- Removes stopwords, punctuation, spaces, short tokens, and non-alphabetic tokens.
- Keeps only selected parts of speech (`NOUN`, `PROPN`, `ADJ`).
- Normalizes lemmas (for example, `datum` -> `data`).
- Applies banlists to reduce generic noise and location terms.
- Builds simple adjacent bigrams from surviving tokens.

`explain_match` then computes set overlap between resume and job keywords and classifies overlaps based on a skill whitelist.

## Understanding Typical Output

A report contains:

- `Match Score`: semantic similarity signal.
- `Common Keywords (Skills / Domain)`: high-value shared terms related to technical/domain relevance.
- `Common Keywords (Other Overlaps)`: shared context terms that are still relevant but less skill-specific.

Example interpretation:

- A score around `0.80` with overlap terms like `sql`, `risk`, `trust`, `safety`, and `policy` indicates strong role-domain alignment.

## Model Loading Messages

During startup, transformer load logs may include warnings such as `UNEXPECTED` keys in a load report. In many cross-wrapper transformer loads, this can be non-fatal if inference continues and output is produced. Fatal startup issues are surfaced as clear runtime errors in `main.py`.

## Limitations

- No API or web UI in the current implementation (CLI only).
- Skill classification uses a static whitelist.
- Bigrams are adjacency-based and may produce awkward phrase combinations.
- First run may require internet access for model download unless assets are already cached locally.
- A single score compresses multiple factors and should not be treated as a hiring decision.

## Validation

Core behavior is covered by unit tests in `tests/test_embedder.py`:

- Similarity returns numeric output.
- Keyword extraction filters noise and builds bigrams.
- Explanation splits overlaps into expected categories.
