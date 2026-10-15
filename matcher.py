"""5-factor weighted matching, skill-gap analysis and roadmap generation."""
from careers import CAREERS

WEIGHTS = {"Skills": 0.40, "Specialization": 0.20, "Education": 0.15, "Certifications": 0.15, "CGPA": 0.10}


def factor_scores(profile: dict, career: str) -> dict:
    info = CAREERS[career]
    user_skills = {s.lower() for s in profile["skills"]}
    req = set(info["skills"])
    skills = len(user_skills & req) / len(req)
    spec = 1.0 if profile["specialization"] in info["specializations"] else 0.3
    edu = 1.0 if profile["education"] in info["education"] else 0.4
    n_certs = len(set(profile["certifications"]) & set(info["certifications"]))
    certs = min(1.0, n_certs / 2)
    cgpa = min(1.0, profile["cgpa"] / info["min_cgpa"])
    return {"Skills": skills, "Specialization": spec, "Education": edu, "Certifications": certs, "CGPA": cgpa}


def weighted_score(profile: dict, career: str) -> tuple[float, dict]:
    f = factor_scores(profile, career)
    return sum(f[k] * WEIGHTS[k] for k in WEIGHTS), f


def skill_gap(profile: dict, career: str) -> dict:
    have = {s.lower() for s in profile["skills"]}
    req = CAREERS[career]["skills"]
    return {"matched": [s for s in req if s in have], "missing": [s for s in req if s not in have]}


def build_roadmap(profile: dict, career: str) -> dict:
    info = CAREERS[career]
    missing = skill_gap(profile, career)["missing"]
    n = len(missing)
    a, b = -(-n // 3), -(-2 * n // 3)  # ceil thirds
    p3, p6, p12 = missing[:a], missing[a:b], missing[b:]
    certs = [c for c in info["certifications"] if c not in profile["certifications"]]
    projs = info["projects"]
    return {
        "3 Months": {
            "focus": "Foundations",
            "skills": p3 or ["Revise core concepts and fundamentals"],
            "actions": [f"Build project: {projs[0]}", "Practice 3-4 coding problems per week", "Create/refresh GitHub and LinkedIn"],
        },
        "6 Months": {
            "focus": "Applied skills",
            "skills": p6 or ["Deepen intermediate skills with real projects"],
            "actions": [f"Build project: {projs[1]}"] + ([f"Start certification: {certs[0]}"] if certs else ["Contribute to an open-source project"]),
        },
        "12 Months": {
            "focus": "Job readiness",
            "skills": p12 or ["Advanced topics and system design basics"],
            "actions": [f"Capstone project: {projs[2]}", "Mock interviews and resume polishing", "Apply to roles (service + product companies)"]
                       + ([f"Complete certification: {certs[1]}"] if len(certs) > 1 else []),
        },
    }


def recommend(profile: dict, model, top_k: int = 3) -> list[dict]:
    from train_model import profile_to_text
    text = profile_to_text(", ".join(profile["skills"]), profile["specialization"], profile["education"], ", ".join(profile["certifications"]))
    probs = dict(zip(model.classes_, model.predict_proba([text])[0]))
    results = []
    for career in CAREERS:
        w, factors = weighted_score(profile, career)
        final = 0.6 * w + 0.4 * probs.get(career, 0.0)
        results.append({"career": career, "final": final, "weighted": w, "ml_prob": probs.get(career, 0.0), "factors": factors})
    return sorted(results, key=lambda r: r["final"], reverse=True)[:top_k]
