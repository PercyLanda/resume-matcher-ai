# Resume Matcher AI (NLP)

A lightweight NLP project that compares a resume and job description using transformer embeddings
(`sentence-transformers/all-MiniLM-L6-v2`) and provides an explainable match report (skills/domain overlaps).

## Features
- Semantic similarity match score (cosine similarity on embeddings)
- Explainability: common skills/domain keywords and other overlaps
- Simple file-based input: `data/raw/resume.txt` and `data/raw/job.txt`

## Project Structure
- `src/` - core code
- `data/raw/` - input text files (resume/job)
- `configs/`, `models/`, `tests/` - reserved for future expansions

## Setup

Create and activate a virtual environment:

```bash
python3.12 -m venv venv
source venv/bin/activate

