import unittest

from src.embedder import ResumeMatcher


class FakeModel:
    def encode(self, texts):
        assert len(texts) == 2
        return [[1.0, 0.0], [0.5, 0.5]]


class FakeToken:
    def __init__(
        self,
        text,
        lemma,
        pos,
        is_stop=False,
        is_punct=False,
        is_space=False,
        is_alpha=True,
    ):
        self.text = text
        self.lemma_ = lemma
        self.pos_ = pos
        self.is_stop = is_stop
        self.is_punct = is_punct
        self.is_space = is_space
        self.is_alpha = is_alpha


class FakeNLP:
    def __call__(self, text):
        source = text.lower()
        if "python" in source:
            return [
                FakeToken("Python", "python", "NOUN"),
                FakeToken("and", "and", "CCONJ"),
                FakeToken("SQL", "sql", "PROPN"),
                FakeToken("data", "datum", "NOUN"),
                FakeToken("San", "san", "PROPN"),
            ]
        return [
            FakeToken("SQL", "sql", "PROPN"),
            FakeToken("risk", "risk", "NOUN"),
            FakeToken("data", "datum", "NOUN"),
        ]


class ResumeMatcherTests(unittest.TestCase):
    def test_compute_similarity_returns_float(self):
        matcher = ResumeMatcher(model=FakeModel(), nlp=FakeNLP())
        score = matcher.compute_similarity("resume", "job")
        self.assertIsInstance(score, float)
        self.assertEqual(round(score, 4), 0.7071)

    def test_extract_keywords_filters_and_bigrams(self):
        matcher = ResumeMatcher(model=FakeModel(), nlp=FakeNLP())
        keywords = matcher.extract_keywords("python sql data san")
        self.assertIn("python", keywords)
        self.assertIn("sql", keywords)
        self.assertIn("data", keywords)
        self.assertNotIn("san", keywords)
        self.assertIn("python sql", keywords)

    def test_explain_match_splits_skill_and_other_overlap(self):
        matcher = ResumeMatcher(model=FakeModel(), nlp=FakeNLP())
        explanation = matcher.explain_match("python sql data", "sql risk data")
        self.assertEqual(explanation["common_skills"], ["sql"])
        self.assertEqual(explanation["common_other"], ["data"])


if __name__ == "__main__":
    unittest.main()
