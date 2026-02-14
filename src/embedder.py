from sklearn.metrics.pairwise import cosine_similarity


# Generic filler words to ignore
GENERIC_BANLIST = {
    "experience", "team", "work", "working", "role", "responsibility",
    "ability", "skills", "skill", "strong", "required", "preferred",
    "business", "process", "product", "operations",
    "project", "projects", "support", "improvement",
    "finding", "trend", "pattern"
}

# Location words to ignore
PROPN_BANLIST = {
    "san", "francisco", "menlo", "park", "california", "bay", "area"
}

# Important skill indicators
SKILL_WHITELIST = {
    "python", "sql", "tableau", "excel",
    "machine", "learning", "tensorflow", "pytorch",
    "nlp", "transformer", "embedding",
    "xgboost", "lightgbm",
    "dashboard", "analytics",
    "trust", "safety", "integrity",
    "risk", "fraud", "policy"
}


class ResumeMatcher:
    def __init__(self, model_name="all-MiniLM-L6-v2", model=None, nlp=None):
        self.model = model or self._load_embedding_model(model_name)
        self.nlp = nlp or self._load_spacy_pipeline()

    @staticmethod
    def _load_embedding_model(model_name):
        try:
            from sentence_transformers import SentenceTransformer
        except ImportError as exc:
            raise RuntimeError(
                "Missing dependency 'sentence-transformers'. Install requirements first."
            ) from exc

        try:
            return SentenceTransformer(model_name)
        except Exception as exc:
            raise RuntimeError(
                "Could not load sentence-transformer model. "
                "Ensure internet access for first download, or use a locally cached model."
            ) from exc

    @staticmethod
    def _load_spacy_pipeline():
        try:
            import spacy
        except ImportError as exc:
            raise RuntimeError(
                "Missing dependency 'spacy'. Install requirements first."
            ) from exc

        try:
            return spacy.load("en_core_web_sm")
        except OSError as exc:
            raise RuntimeError(
                "spaCy model 'en_core_web_sm' is not installed. "
                "Run: python -m spacy download en_core_web_sm"
            ) from exc

    def compute_similarity(self, resume_text, job_text):
        embeddings = self.model.encode([resume_text, job_text])
        score = cosine_similarity([embeddings[0]], [embeddings[1]])
        return float(score[0][0])

    def extract_keywords(self, text):
        doc = self.nlp(text.lower())
        keywords = set()
        tokens = []

        for token in doc:
            if token.is_stop or token.is_punct or token.is_space:
                continue

            if not token.is_alpha:
                continue

            if token.pos_ not in {"NOUN", "PROPN", "ADJ"}:
                continue

            lemma = token.lemma_

            if lemma == "datum":
                lemma = "data"

            if len(lemma) < 3:
                continue

            if lemma in GENERIC_BANLIST:
                continue

            if token.pos_ == "PROPN" and lemma in PROPN_BANLIST:
                continue

            keywords.add(lemma)
            tokens.append(lemma)

        # Add simple bigrams
        for i in range(len(tokens) - 1):
            bigram = f"{tokens[i]} {tokens[i+1]}"
            keywords.add(bigram)

        return keywords

    def explain_match(self, resume_text, job_text):
        resume_keywords = self.extract_keywords(resume_text)
        job_keywords = self.extract_keywords(job_text)

        common = resume_keywords.intersection(job_keywords)

        common_skills = sorted([
            term for term in common
            if any(word in SKILL_WHITELIST for word in term.split())
        ])

        common_other = sorted([
            term for term in common
            if term not in common_skills
        ])

        return {
            "common_skills": common_skills,
            "common_other": common_other
        }
