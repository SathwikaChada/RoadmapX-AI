"""Generate a synthetic career-profile dataset (5,000+ records)."""
import random
import pandas as pd
from careers import CAREERS, ALL_SKILLS, ALL_SPECIALIZATIONS, ALL_EDUCATION, ALL_CERTIFICATIONS

random.seed(42)
N_PER_CAREER = 450  # 12 careers x 450 = 5,400 records


def make_profile(career: str) -> dict:
    info = CAREERS[career]
    k = max(3, int(len(info["skills"]) * random.uniform(0.3, 0.75)))
    skills = set(random.sample(info["skills"], k))
    skills |= set(random.sample(ALL_SKILLS, random.randint(2, 6)))  # noise
    spec = random.choice(info["specializations"]) if random.random() < 0.65 else random.choice(ALL_SPECIALIZATIONS)
    edu = random.choice(info["education"]) if random.random() < 0.7 else random.choice(ALL_EDUCATION)
    certs = set(random.sample(info["certifications"], random.randint(0, 2)))
    if random.random() < 0.15:
        certs.add(random.choice(ALL_CERTIFICATIONS))
    cgpa = round(min(10, max(5.0, random.gauss(info["min_cgpa"] + 0.5, 0.9))), 2)
    return {
        "skills": ", ".join(sorted(skills)),
        "specialization": spec,
        "education": edu,
        "certifications": ", ".join(sorted(certs)),
        "cgpa": cgpa,
        "career": career,
    }


def main():
    rows = [make_profile(c) for c in CAREERS for _ in range(N_PER_CAREER)]
    random.shuffle(rows)
    df = pd.DataFrame(rows)
    df.to_csv("data/career_profiles.csv", index=False)
    print(f"Saved {len(df)} records across {df['career'].nunique()} careers -> data/career_profiles.csv")


if __name__ == "__main__":
    main()
