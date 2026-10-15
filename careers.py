"""Career knowledge base: skills are ordered from foundational -> advanced."""

CAREERS = {
    "Data Scientist": {
        "skills": ["python", "statistics", "pandas", "sql", "data visualization", "machine learning", "scikit-learn", "feature engineering", "deep learning", "model deployment"],
        "specializations": ["Data Science", "Artificial Intelligence", "Computer Science", "Statistics"],
        "education": ["B.Tech", "M.Tech", "MCA", "M.Sc"],
        "certifications": ["IBM Data Science", "Google Data Analytics", "Coursera ML Specialization"],
        "min_cgpa": 7.5,
        "projects": ["Customer churn prediction", "House price regression with feature engineering", "End-to-end ML app deployed on Streamlit"],
    },
    "Machine Learning Engineer": {
        "skills": ["python", "linear algebra", "machine learning", "tensorflow", "pytorch", "mlops", "docker", "model deployment", "deep learning", "nlp"],
        "specializations": ["Artificial Intelligence", "Data Science", "Computer Science"],
        "education": ["B.Tech", "M.Tech", "M.Sc"],
        "certifications": ["TensorFlow Developer", "AWS ML Specialty", "Deep Learning Specialization"],
        "min_cgpa": 8.0,
        "projects": ["Image classifier with CNN", "NLP sentiment API with FastAPI", "ML pipeline with Docker and CI"],
    },
    "Data Analyst": {
        "skills": ["excel", "sql", "statistics", "python", "pandas", "data visualization", "power bi", "tableau", "data cleaning", "storytelling"],
        "specializations": ["Data Science", "Statistics", "Computer Science", "Business Analytics", "Information Technology"],
        "education": ["B.Tech", "B.Sc", "BCA", "MBA", "MCA"],
        "certifications": ["Google Data Analytics", "Microsoft PL-300", "Tableau Desktop Specialist"],
        "min_cgpa": 6.5,
        "projects": ["Sales dashboard in Power BI", "SQL-based retail analysis", "EDA report on public dataset"],
    },
    "Full Stack Developer": {
        "skills": ["html", "css", "javascript", "git", "react", "node.js", "rest apis", "sql", "mongodb", "docker"],
        "specializations": ["Computer Science", "Information Technology", "Software Engineering"],
        "education": ["B.Tech", "BCA", "MCA", "B.Sc"],
        "certifications": ["Meta Full Stack Developer", "freeCodeCamp Full Stack", "AWS Cloud Practitioner"],
        "min_cgpa": 6.5,
        "projects": ["MERN e-commerce app", "Real-time chat app", "Job portal with auth and REST APIs"],
    },
    "Frontend Developer": {
        "skills": ["html", "css", "javascript", "git", "responsive design", "react", "typescript", "testing", "web performance", "accessibility"],
        "specializations": ["Computer Science", "Information Technology", "Software Engineering"],
        "education": ["B.Tech", "BCA", "B.Sc", "MCA"],
        "certifications": ["Meta Front-End Developer", "freeCodeCamp Responsive Web Design", "W3C Front-End"],
        "min_cgpa": 6.0,
        "projects": ["Portfolio website", "Weather app with API", "Dashboard UI with React and charts"],
    },
    "Backend Developer": {
        "skills": ["python", "java", "sql", "data structures", "rest apis", "git", "django", "spring boot", "system design", "docker"],
        "specializations": ["Computer Science", "Information Technology", "Software Engineering"],
        "education": ["B.Tech", "M.Tech", "MCA", "BCA"],
        "certifications": ["Oracle Java SE", "AWS Developer Associate", "Python Institute PCAP"],
        "min_cgpa": 7.0,
        "projects": ["URL shortener with caching", "Library management REST API", "Microservice-based order system"],
    },
    "DevOps Engineer": {
        "skills": ["linux", "git", "bash scripting", "docker", "ci/cd", "jenkins", "kubernetes", "terraform", "monitoring", "aws"],
        "specializations": ["Computer Science", "Information Technology", "Cloud Computing"],
        "education": ["B.Tech", "M.Tech", "MCA", "BCA"],
        "certifications": ["CKA Kubernetes", "AWS DevOps Engineer", "HashiCorp Terraform Associate"],
        "min_cgpa": 6.5,
        "projects": ["CI/CD pipeline with Jenkins", "Dockerized app on Kubernetes", "Infra as code with Terraform"],
    },
    "Cloud Engineer": {
        "skills": ["linux", "networking", "aws", "azure", "virtualization", "iam", "terraform", "serverless", "cloud security", "cost optimization"],
        "specializations": ["Cloud Computing", "Computer Science", "Information Technology"],
        "education": ["B.Tech", "M.Tech", "MCA", "BCA"],
        "certifications": ["AWS Solutions Architect Associate", "Azure Fundamentals AZ-900", "Google Cloud Associate"],
        "min_cgpa": 6.5,
        "projects": ["Static site on S3 + CloudFront", "Serverless API with Lambda", "Multi-tier VPC architecture"],
    },
    "Cybersecurity Analyst": {
        "skills": ["networking", "linux", "security fundamentals", "python", "siem", "penetration testing", "cryptography", "incident response", "vulnerability assessment", "owasp"],
        "specializations": ["Cyber Security", "Computer Science", "Information Technology", "Networking"],
        "education": ["B.Tech", "M.Tech", "MCA", "B.Sc"],
        "certifications": ["CompTIA Security+", "CEH", "Google Cybersecurity"],
        "min_cgpa": 6.5,
        "projects": ["Network vulnerability scan report", "Log analysis with a SIEM", "OWASP Top 10 lab write-up"],
    },
    "Mobile App Developer": {
        "skills": ["java", "kotlin", "dart", "flutter", "android studio", "rest apis", "firebase", "state management", "ui design", "git"],
        "specializations": ["Computer Science", "Information Technology", "Software Engineering"],
        "education": ["B.Tech", "BCA", "MCA", "B.Sc"],
        "certifications": ["Google Associate Android Developer", "Flutter Certified", "Meta Android Developer"],
        "min_cgpa": 6.0,
        "projects": ["To-do app with Firebase", "Expense tracker in Flutter", "Food delivery app UI with APIs"],
    },
    "QA / Test Engineer": {
        "skills": ["testing fundamentals", "manual testing", "sql", "selenium", "java", "api testing", "postman", "test automation", "ci/cd", "bug tracking"],
        "specializations": ["Computer Science", "Information Technology", "Software Engineering"],
        "education": ["B.Tech", "BCA", "MCA", "B.Sc"],
        "certifications": ["ISTQB Foundation", "Selenium WebDriver", "Postman API Fundamentals"],
        "min_cgpa": 6.0,
        "projects": ["Selenium framework for an e-commerce site", "Postman API test suite", "Test plan and bug report portfolio"],
    },
    "UI/UX Designer": {
        "skills": ["design thinking", "figma", "wireframing", "prototyping", "user research", "typography", "color theory", "usability testing", "design systems", "html"],
        "specializations": ["Design", "Computer Science", "Information Technology", "Human Computer Interaction"],
        "education": ["B.Des", "B.Tech", "BCA", "M.Des", "B.Sc"],
        "certifications": ["Google UX Design", "Interaction Design Foundation", "Figma Professional"],
        "min_cgpa": 6.0,
        "projects": ["Mobile app redesign case study", "Design system in Figma", "Usability test report"],
    },
}

ALL_SKILLS = sorted({s for c in CAREERS.values() for s in c["skills"]})
ALL_SPECIALIZATIONS = sorted({s for c in CAREERS.values() for s in c["specializations"]})
ALL_EDUCATION = sorted({s for c in CAREERS.values() for s in c["education"]})
ALL_CERTIFICATIONS = sorted({s for c in CAREERS.values() for s in c["certifications"]})
