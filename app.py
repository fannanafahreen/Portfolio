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
        "items": ["Python", "SQL", "Kotlin", "C"],
    },
    {
        "label": "Libraries / Tools",
        "items": ["Pandas", "NumPy", "Scikit-learn", "Matplotlib"],
    },
    {
        "label": "Data Analytics",
        "items": ["Data Cleaning", "EDA", "Feature Engineering", "Model Evaluation"],
    },
    {
        "label": "Visualization",
        "items": ["Power BI", "Excel (Power Query, Power Pivot)"],
    },
    {
        "label": "Other",
        "items": ["Git", "GitHub", "Firebase"],
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
        "title":       "Weather Dashboard",
        "description": "Fetches real-time weather data from a public API "
                       "and displays it with clean interactive charts.",
        "tags":  ["Python", "Flask", "REST API", "Chart.js"],
        "link":  "#",
    },
    {
        "title":       "Customer Churn Predictor",
        "description": "End-to-end ML pipeline (EDA → feature engineering → "
                       "Random Forest) achieving 87 % accuracy on test data.",
        "tags":  ["Python", "Scikit-learn", "Pandas", "Jupyter"],
        "link":  "#",
    },
    {
        "title":       "Data Visualiser",
        "description": "Upload any CSV and get an auto-generated set of "
                       "charts to explore distributions and correlations.",
        "tags":  ["Python", "Pandas", "Seaborn", "Flask"],
        "link":  "#",
    },
    {
        "title":       "Portfolio Website",
        "description": "This CV-style portfolio, built from scratch with "
                       "Flask and plain CSS — no frameworks.",
        "tags":  ["Python", "Flask", "HTML/CSS"],
        "link":  "#",
    },
    {
        "title":       "Fraud Detector",
        "description": "Full-stack credit-card fraud detection app. "
                       "An Isolation Forest model (scikit-learn) flags "
                       "anomalous transactions via a FastAPI /predict endpoint; "
                       "a React 18 / Vite frontend renders a confidence gauge "
                       "with green/red result cards. Backend deployed on Render, "
                       "frontend on Vercel.",
        "tags":  ["Python", "FastAPI", "Scikit-learn", "React", "Vite"],
        "link":  "https://github.com/fannanafahreen/fannanafahreen",
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
