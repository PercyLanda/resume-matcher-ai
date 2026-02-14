# Resume Matcher AI

Resume Matcher AI is a Natural Language Processing (NLP) application that evaluates the semantic alignment between a resume and a job description using vector space modeling and cosine similarity.

The system transforms unstructured text into numerical feature representations using TF-IDF vectorization, enabling quantitative comparison between candidate qualifications and job requirements. This project demonstrates applied NLP, feature engineering, similarity modeling, and practical ML implementation in a real-world hiring context.

---

## Executive Summary

This project provides an interpretable similarity score that measures resume–job alignment. It simulates a simplified Applicant Tracking System (ATS) scoring workflow by quantifying keyword relevance and contextual overlap.

Key outcomes:

* Objective resume–job similarity scoring
* Transparent keyword overlap analysis
* Modular architecture for future ML extension
* Reproducible NLP pipeline

---

## Problem Statement

Job seekers often lack measurable feedback on how well their resumes align with specific roles. Recruiters and ATS systems evaluate resumes based on contextual similarity and keyword relevance.

This project provides a structured and quantitative approach to measuring alignment between resumes and job descriptions.

---

## Technical Approach

1. Text preprocessing and normalization
2. Tokenization and cleaning
3. TF-IDF feature extraction
4. Vector space transformation
5. Cosine similarity computation
6. Keyword overlap extraction

Cosine similarity formula:

Similarity(A, B) = (A · B) / (||A|| × ||B||)

---

## Model Architecture

Text Input (Resume + Job Description)
→ Text Cleaning & Normalization
→ TF-IDF Vectorization
→ Vector Space Representation
→ Cosine Similarity Scoring
→ Keyword Overlap Extraction
→ Alignment Score Output

This modular pipeline allows future replacement of TF-IDF with transformer embeddings or contextual vector models.

---

## Results & Evaluation

The system produces:

* A similarity score between 0 and 1
* Ranked overlapping terms
* Interpretable keyword matches

Example Output:

Resume Match Score: 0.82

Top Overlapping Terms:

* python
* sql
* machine learning
* data analysis

Interpretation:
A score above 0.75 indicates strong keyword and contextual alignment under TF-IDF modeling assumptions.

---

## Tech Stack

* Python 3
* scikit-learn
* NumPy
* Pandas
* TF-IDF Vectorizer
* Cosine Similarity

---

## Project Structure

```
resume-matcher-ai/
│
├── app.py            # Application entry point
├── matcher.py        # Core NLP and similarity logic
├── utils.py          # Text preprocessing utilities
├── requirements.txt  # Dependency list
└── README.md         # Project documentation
```

---

## Installation

Clone the repository:

```
git clone https://github.com/PercyLanda/resume-matcher-ai.git
cd resume-matcher-ai
```

Create and activate a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Usage

Run the application:

```
python app.py
```

Provide:

* Resume text
* Job description text

The system outputs:

* Similarity score
* Overlapping keywords

---

## Future Enhancements

* Transformer-based embeddings (e.g., SentenceTransformers)
* Context-aware semantic similarity
* Skill gap detection module
* ATS-style weighted scoring
* Web interface (Streamlit or Flask)
* Deployment-ready API endpoint

---

## Why This Project Matters

This project demonstrates:

* Applied NLP implementation
* Feature engineering in text pipelines
* Vector space modeling
* Similarity-based scoring systems
* Modular ML architecture design
* Practical AI use case for career optimization

It serves as a portfolio-ready example for roles in Data Science, Machine Learning, NLP, and Applied AI.

---

## Author

Percy Landa<br>
San Francisco Bay Area<br>
GitHub: https://github.com/PercyLanda