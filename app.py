# app.py — Main Flask application.
# All page data lives here as Python dicts/lists so you can
# update content without touching any HTML file.

from flask import Flask, render_template

app = Flask(__name__)

# ── Owner / sidebar data ─────────────────────────────────────
owner = {
    "name":     "Fannana Fahreen Aanan",
    "title":    "Data Science Enthusiast",
    "bio":      (
        "Aspiring data scientist passionate about turning raw data "
        "into meaningful insights. I enjoy building end-to-end ML "
        "pipelines, data visualisations, and web applications that "
        "make analysis accessible to everyone."
    ),
    "email":    "fannanafahreen@gmail.com",
    "phone":    "07466158752",
    "github":   "https://github.com/fannanafahreen",
    "linkedin": "https://www.linkedin.com/in/fannana-fahreen/",
    "location": "London, UK",
}

# ── Skills ───────────────────────────────────────────────────
# Each skill group has a label and a list of items.
skill_groups = [
    {
        "label": "Programming",
        "items": ["Python", "SQL", "JavaScript", "Kotlin", "C"],
    },
    {
        "label": "Machine Learning",
        "items": ["Scikit-learn", "Isolation Forest", "Random Forest", "NetworkX", "Feature Engineering", "Model Evaluation"],
    },
    {
        "label": "Data & Analytics",
        "items": ["Pandas", "NumPy", "Matplotlib", "Seaborn", "EDA", "Data Cleaning"],
    },
    {
        "label": "Web & APIs",
        "items": ["React", "FastAPI", "Flask", "Vite", "Leaflet.js", "HTML", "CSS", "RESTful APIs"],
    },
    {
        "label": "Databases",
        "items": ["PostgreSQL", "SQLAlchemy", "Firebase","Neo4j"],
    },
    {
        "label": "Visualization & BI",
        "items": ["Power BI", "Excel (Power Query, Power Pivot)"],
    },
    {
        "label": "Tools",
        "items": ["Git", "GitHub", "Jupyter", "Go High Level"],
    },
]

# ── Education ────────────────────────────────────────────────
education = [
   {
        "degree":      "M.Sc. in Data Science(Fintech)",
        "institution": "University of Greenwich",
        "period":      "2026 – Present",
        "detail":      "Relevant courses: Machine Learning, Databases, Statistics, Data Structures.",
    },
    {
        "degree":      "B.Sc. in Computer Science & Engineering",
        "institution": "North South University ",
        "period":      "2021 – 2024",
        "detail":      "Relevant courses: Machine Learning, Databases, Statistics, Data Structures.",
    },

]

# ── Work Experience ──────────────────────────────────────────
experience = [
    {
        "role":        "Data Science Intern",
        "company":     "Rahab's Daughters",
        "period":      "May 2026 – Present",
        "points": [
            "Developing the organisation's website using Go High Level for an anti-human trafficking charity.",
            "Building landing pages, forms, and automation workflows to support outreach and fundraising.",
            "Collaborating with staff to translate mission and programme content into effective web design.",
        ],
    },
    {
        "role":        "Data Analyst",
        "company":     "Redorch Technology LTD",
        "period":      "Feb 2025 – Nov 2025",
        "points": [
            "Cleaned and preprocessed datasets to improve data quality and usability.",
            "Conducted exploratory data analysis to identify trends and insights.",
            "Built interactive dashboards using Power BI for data visualization.",
            "Produced reports to support data-driven decision making.",
        ],
    },
]

# ── Projects ─────────────────────────────────────────────────
projects = [
    {
        "title":       "LondonWatch",
        "description": (
            "Intelligence platform supporting anti-human trafficking investigations in London. "
            "Analyses 5.7M+ UK business registrations, census data, crime statistics, and NRM "
            "records using Isolation Forest and graph network analysis to classify all 33 boroughs "
            "by risk level. Includes an interactive Leaflet.js map with real-time Companies House API integration."
        ),
        "tags":  ["Python", "FastAPI", "PostgreSQL", "React", "Leaflet.js", "scikit-learn", "NetworkX", "Pandas"],
        "link":  "https://github.com/fannanafahreen/London_based_Anti_Human_Trafficking_Platform",
    },
    {
        "title":       "UK Banking Risk Intelligence Dashboard",
        "description": (
            "End-to-end banking risk project combining three real-world datasets to predict "
            "loan default risk with a Random Forest model. Key finding: students aged 26–35 "
            "defaulted at 95%, nearly 14x the portfolio average. Presented in a 6-page "
            "interactive Power BI dashboard with DAX measures, drill-through, and key influencer visuals."
        ),
        "tags":  ["Python", "Scikit-learn", "Power BI", "DAX", "SQLite", "Pandas"],
        "link":  "https://github.com/fannanafahreen/uk-banking-risk-intelligence-dashboard",
    },
    {
        "title":       "Fraud Detector",
        "description": "Full-stack credit-card fraud detection app. "
                       "An Isolation Forest model flags anomalous transactions via a FastAPI /predict endpoint; "
                       "a React 18 / Vite frontend renders a confidence gauge "
                       "with green/red result cards. Backend deployed on Render, frontend on Vercel.",
        "tags":  ["Python", "FastAPI", "Scikit-learn", "React", "Vite"],
        "link":  "https://github.com/fannanafahreen/fraud-detector",
    },
    {
        "title":       "Customer Churn Predictor",
        "description": "End-to-end ML pipeline (EDA → feature engineering → "
                       "Random Forest) achieving 87 % accuracy on test data.",
        "tags":  ["Python", "Scikit-learn", "Pandas", "Jupyter"],
        "link":  "#",
    },
    {
        "title":       "Portfolio Website",
        "description": "This CV-style portfolio, built from scratch with "
                       "Flask and plain CSS — no frameworks.",
        "tags":  ["Python", "Flask", "HTML", "CSS"],
        "link":  "#",
    },
    {
        "title":       "Human Trafficking Analysis",
        "description": "Interactive Power BI dashboard analysing global human "
                       "trafficking patterns using UNODC data (2003–2023, 160+ countries). "
                       "Covers victim gender, age, exploitation type trends, and a country "
                       "distribution map. Dataset cleaned with Python (Pandas) in Jupyter Notebook.",
        "tags":  ["Power BI", "Python", "Pandas", "Jupyter"],
        "link":  "https://github.com/fannanafahreen/Human-Trafficking-Analysis",
    },
]


# ── Routes ───────────────────────────────────────────────────
@app.route("/")
def home():
    """Render the CV home page (skills, education, experience, projects)."""
    return render_template(
        "index.html",
        owner=owner,
        skill_groups=skill_groups,
        education=education,
        experience=experience,
        projects=projects,
    )


# ── Entry point ──────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)
