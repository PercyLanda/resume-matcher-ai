# Resume Matcher AI

Resume Matcher AI is a Natural Language Processing (NLP) application that evaluates the alignment between a resume and a job description using vector space modeling and cosine similarity. The system converts unstructured text into numerical representations using TF-IDF vectorization and computes similarity scores to quantify candidate–role alignment.

This project demonstrates applied NLP, feature engineering, and similarity modeling in a practical hiring-context use case.

---

## Problem Statement

Job seekers often lack objective feedback on how closely their resumes align with specific roles. Applicant Tracking Systems (ATS) and recruiters frequently rely on keyword relevance and contextual alignment when screening candidates.

This project provides a measurable similarity score and keyword overlap analysis to help quantify resume–job alignment.

---

## Technical Approach

1. Text preprocessing and normalization
2. TF-IDF feature extraction
3. Vector space transformation
4. Cosine similarity computation
5. Keyword overlap extraction

Cosine similarity is computed as:

Similarity(A, B) = (A · B) / (||A|| × ||B||)

---

## Tech Stack

* Python 3
* scikit-learn
* NumPy
* Pandas
* TF-IDF Vectorization
* Cosine Similarity

---

## Project Structure

resume-matcher-ai/
│
├── app.py
├── matcher.py
├── utils.py
├── requirements.txt
└── README.md

---

## Installation

Clone the repository:

git clone [https://github.com/PercyLanda/resume-matcher-ai.git](https://github.com/PercyLanda/resume-matcher-ai.git)
cd resume-matcher-ai

Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

---

## Usage

Run the application:

python app.py

Provide:

* Resume text
* Job description text

The system outputs:

* Similarity score (percentage or decimal value)
* Top overlapping keywords

---

## Example Output

Resume Match Score: 0.82

Top Overlapping Terms:

* python
* sql
* machine learning
* data analysis

---

## Future Enhancements

* Transformer-based embeddings (e.g., SentenceTransformers)
* Context-aware similarity scoring
* Skill gap identification
* Web-based interface (Streamlit or Flask)
* ATS-style keyword weighting

---

## Author

Percy Landa
San Francisco Bay Area
GitHub: [https://github.com/PercyLanda](https://github.com/PercyLanda)
