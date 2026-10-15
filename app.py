import os
import joblib
import pandas as pd
import streamlit as st

from careers import ALL_SKILLS, ALL_SPECIALIZATIONS, ALL_EDUCATION, ALL_CERTIFICATIONS, CAREERS
from matcher import WEIGHTS, recommend, skill_gap, build_roadmap

st.set_page_config(page_title="RoadmapX AI", page_icon="🧭", layout="wide")


@st.cache_resource
def load_model():
    from train_model import MODEL_PATH, train
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return train()[0]


@st.cache_data
def load_data():
    from train_model import DATA_PATH
    if not os.path.exists(DATA_PATH):
        import generate_data
        generate_data.main()
    return pd.read_csv(DATA_PATH)


model, df = load_model(), load_data()

st.title("🧭 RoadmapX AI")
st.caption("Personalized Career Roadmap Recommendation System")

with st.sidebar:
    st.header("Your Profile")
    skills = st.multiselect("Skills", ALL_SKILLS, default=["python", "sql"])
    specialization = st.selectbox("Specialization", ALL_SPECIALIZATIONS, index=ALL_SPECIALIZATIONS.index("Computer Science"))
    education = st.selectbox("Education", ALL_EDUCATION, index=ALL_EDUCATION.index("B.Tech"))
    certs = st.multiselect("Certifications", ALL_CERTIFICATIONS)
    cgpa = st.slider("CGPA", 5.0, 10.0, 7.5, 0.1)
    go = st.button("Generate my roadmap", type="primary", use_container_width=True)

tab_reco, tab_data = st.tabs(["Recommendations", "Dataset insights"])

with tab_reco:
    if not go:
        st.info("Fill in your profile on the left and click **Generate my roadmap**.")
    elif not skills:
        st.warning("Select at least one skill.")
    else:
        profile = {"skills": skills, "specialization": specialization, "education": education, "certifications": certs, "cgpa": cgpa}
        results = recommend(profile, model, top_k=3)

        st.subheader("Top career matches")
        cols = st.columns(3)
        for col, r in zip(cols, results):
            col.metric(r["career"], f"{r['final']*100:.0f}% match", f"ML {r['ml_prob']*100:.0f}% | Rules {r['weighted']*100:.0f}%")

        names = [r["career"] for r in results]
        chosen = st.selectbox("Explore a career path", names)
        r = next(x for x in results if x["career"] == chosen)

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### 5-factor match breakdown")
            st.bar_chart(pd.DataFrame({"Score": r["factors"]}))
            st.caption("Weights: " + ", ".join(f"{k} {int(v*100)}%" for k, v in WEIGHTS.items()))
        with c2:
            gap = skill_gap(profile, chosen)
            st.markdown("#### Skill-gap analysis")
            st.success("Matched: " + (", ".join(gap["matched"]) or "none yet"))
            st.error("Missing: " + (", ".join(gap["missing"]) or "none, you cover everything!"))
            st.progress(len(gap["matched"]) / len(CAREERS[chosen]["skills"]))

        st.markdown("#### Your personalized roadmap")
        road = build_roadmap(profile, chosen)
        for tab, (period, plan) in zip(st.tabs(list(road)), road.items()):
            with tab:
                st.markdown(f"**Focus:** {plan['focus']}")
                st.markdown("**Skills to learn**")
                for s in plan["skills"]:
                    st.markdown(f"- {s}")
                st.markdown("**Actions**")
                for a in plan["actions"]:
                    st.markdown(f"- {a}")

with tab_data:
    st.metric("Career-profile records analysed", f"{len(df):,}")
    st.metric("Career categories", df["career"].nunique())
    st.markdown("#### Records per career")
    st.bar_chart(df["career"].value_counts())
    st.markdown("#### Average CGPA per career")
    st.bar_chart(df.groupby("career")["cgpa"].mean())
    st.dataframe(df.head(50), use_container_width=True)
