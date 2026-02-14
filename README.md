# Resume Matcher AI

Resume Matcher AI compares a resume and a job description with sentence embeddings and cosine similarity, then explains overlap with lightweight keyword extraction.

## What It Does

- Computes a semantic match score in `[0, 1]` using `sentence-transformers`.
- Extracts overlapping keywords and bigrams with spaCy.
- Separates overlaps into:
  - `common_skills`: terms that include known skill indicators (for quick ATS-style signal).
  - `common_other`: other shared topical terms.

## Project Structure

```text
resume-matcher-ai/
├── data/
│   └── raw/
│       ├── resume.txt
│       └── job.txt
├── src/
│   ├── embedder.py
│   └── main.py
├── tests/
│   └── test_embedder.py
├── requirements.txt
└── README.md
```

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

Note: the first run also downloads the embedding model (`all-MiniLM-L6-v2`) from Hugging Face unless already cached locally.

## Usage

```bash
python src/main.py
```

By default, the app reads:
- `data/raw/resume.txt`
- `data/raw/job.txt`

## Process

1. Activate a virtual environment so dependencies stay isolated from system Python.
2. Install required packages from `requirements.txt`.
3. Install the spaCy English model (`en_core_web_sm`).
4. Run `python src/main.py` to generate a match score and overlap terms.

## What Each File Does

- `src/main.py`: Entry point; loads input files, runs matching, and prints output.
- `src/embedder.py`: Core scoring and keyword extraction logic.
- `data/raw/resume.txt`: Resume input text.
- `data/raw/job.txt`: Job description input text.
- `tests/test_embedder.py`: Unit tests for matching and keyword logic.
- `requirements.txt`: Project dependency list.
- `README.md`: Setup, usage, and project documentation.
- `.gitignore`: Excludes local environment and cache files from git.

## Testing

```bash
python -m unittest discover -s tests -v
```

## Current Limits

- No API/UI yet; this is a CLI prototype.
- Skill matching uses a small static whitelist.
- Inference needs model assets available locally (download on first run).

## Author

Author<br>
Percy Landa<br>
San Francisco Bay Area<br>
GitHub: https://github.com/PercyLanda
