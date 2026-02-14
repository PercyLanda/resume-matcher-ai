from pathlib import Path

try:
    from src.embedder import ResumeMatcher
except ModuleNotFoundError:
    from embedder import ResumeMatcher


def read_text_file(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return path.read_text(encoding="utf-8").strip()


def main():
    project_root = Path(__file__).resolve().parents[1]

    resume_path = project_root / "data" / "raw" / "resume.txt"
    job_path = project_root / "data" / "raw" / "job.txt"

    resume_text = read_text_file(resume_path)
    job_text = read_text_file(job_path)

    try:
        matcher = ResumeMatcher()
    except RuntimeError as err:
        print(f"Startup error: {err}")
        return

    score = matcher.compute_similarity(resume_text, job_text)
    explanation = matcher.explain_match(resume_text, job_text)

    print("\n==============================")
    print("AI Resume Matcher")
    print("==============================\n")

    print(f"Resume file: {resume_path}")
    print(f"Job file:    {job_path}")

    print(f"\nMatch Score: {score:.4f}\n")

    print("Common Keywords (Skills / Domain):")
    if explanation["common_skills"]:
        for term in explanation["common_skills"]:
            print(f"- {term}")
    else:
        print("(none found)")

    print("\nCommon Keywords (Other Overlaps):")
    if explanation["common_other"]:
        for term in explanation["common_other"][:25]:
            print(f"- {term}")
    else:
        print("(none found)")

    print("\n==============================\n")


if __name__ == "__main__":
    main()
