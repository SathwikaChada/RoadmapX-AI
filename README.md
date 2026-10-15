# RoadmapX AI: Personalized Career Roadmap Recommendation System

**Tech:** Python, Streamlit, Pandas, Scikit-learn

- Analyzes 5,000+ career-profile records
- TF-IDF + Logistic Regression classifier across 12 career categories
- 5-factor weighted matching: skills (40%), specialization (20%), education (15%), certifications (15%), CGPA (10%)
- Skill-gap analysis for each recommended career
- Personalized 3, 6 and 12-month learning roadmaps in an interactive Streamlit dashboard

## Run
```bash
pip install -r requirements.txt
python generate_data.py   # creates data/career_profiles.csv
python train_model.py     # trains and saves models/career_model.joblib
streamlit run app.py
```

## Structure
- `careers.py` career knowledge base
- `generate_data.py` dataset builder
- `train_model.py` TF-IDF + Logistic Regression
- `matcher.py` weighted matching, skill gap, roadmap
- `app.py` Streamlit dashboard
