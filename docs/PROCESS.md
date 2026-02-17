# Process Documentation

## Overview

Resume Matcher AI is a command-line application that compares a resume against a job description and outputs:

- A numeric match score based on semantic similarity.
- Interpretable overlap terms grouped into skill/domain terms and other shared terms.

The main objective is to combine a quantitative signal with human-readable reasoning.

## Architecture

### Core Components

- `src/main.py`: Application entry point. Reads input files, runs matching, and prints results.
- `src/embedder.py`: Implements similarity scoring, keyword extraction, and overlap explanation.
- `data/raw/resume.txt`: Resume input text.
- `data/raw/job.txt`: Job description input text.
- `tests/test_embedder.py`: Unit tests for matcher behavior.
- `requirements.txt`: Python dependencies.

### Processing Pipeline

1. Load resume and job description text files.
2. Initialize `ResumeMatcher`.
3. Load `sentence-transformers` model (`all-MiniLM-L6-v2`) and spaCy pipeline (`en_core_web_sm`).
4. Encode both documents into vector embeddings.
5. Compute cosine similarity between vectors.
6. Extract normalized keywords and bigrams from both documents.
7. Compute overlapping terms and classify into `common_skills` and `common_other`.
8. Print match score and overlap output in the CLI.

## How the Project Works

### Cosine Similarity

The current implementation computes semantic similarity using cosine similarity between dense document embeddings:

`cosine(A, B) = (A · B) / (||A|| * ||B||)`

- Values near `1.0` indicate stronger alignment.
- Values near `0.0` indicate weaker alignment.
- This is an alignment score, not a hiring decision.

### TF-IDF Similarity Scoring

TF-IDF (Term Frequency-Inverse Document Frequency) is a classic sparse-vector approach for text similarity:

- **Term Frequency (TF):** how often a term appears in a document.
- **Inverse Document Frequency (IDF):** down-weights terms common across many documents.
- The combined TF-IDF vector represents term importance per document.

Similarity is then commonly computed with cosine similarity on TF-IDF vectors. In this project, TF-IDF is useful to understand baseline lexical matching, while the implemented scorer uses sentence embeddings for stronger semantic matching.

### Project Structure

```text
resume-matcher-ai/
├── configs/
├── data/
│   └── raw/
│       ├── job.txt
│       └── resume.txt
├── docs/
│   ├── how-it-works.md
│   └── PROCESS.md
├── models/
├── notebooks/
├── src/
│   ├── embedder.py
│   └── main.py
├── tests/
│   └── test_embedder.py
├── requirements.txt
└── README.md
```

## Environment Setup

Create and activate a virtual environment, then install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

Notes:

- The first run may download `all-MiniLM-L6-v2` if not cached locally.
- Keep the environment activated while installing packages or running the app.

## Running the Application

From the repository root:

```bash
python src/main.py
```

The script reads:

- `data/raw/resume.txt`
- `data/raw/job.txt`

Then prints:

- Match score
- Common keywords (skills/domain)
- Common keywords (other overlaps)

## Virtual Environment Management

### Deactivate the Environment

When finished, run:

```bash
deactivate
```

### Delete the Environment Safely

1. Ensure the environment is deactivated (`deactivate`).
2. Verify you are in the project root.
3. Remove only the local `venv` directory:

```bash
rm -rf venv
```

### Recreate the Environment

Use exactly:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Recommended after recreation:

```bash
python -m spacy download en_core_web_sm
```

## Reopening the Project

When returning later:

1. Open a terminal in `resume-matcher-ai/`.
2. Activate the environment:

```bash
source venv/bin/activate
```

3. Confirm dependencies are available (optional):

```bash
pip list
```

4. Run the application:

```bash
python src/main.py
```

## Usage Examples

### Example 1: Normal Run

```bash
source venv/bin/activate
python src/main.py
```

### Example 2: Run Tests

```bash
source venv/bin/activate
python -m unittest discover -s tests -v
```

### Example 3: Refresh Input Files and Re-run

1. Update `data/raw/resume.txt` and `data/raw/job.txt`.
2. Execute:

```bash
python src/main.py
```
