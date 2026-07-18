# app.py — Main Flask application.
# All page data lives here as Python dicts/lists so you can
# update content without touching any HTML file.

from flask import Flask, render_template

app = Flask(__name__)

# ── Owner / sidebar data ─────────────────────────────────────
owner = {
    "name":     "Fannana Fahreen Aanan",
    "title":    "Data Scientist & AI Engineer",
    "bio":      (
        "I build production-ready ML systems, RAG pipelines, and graph "
        "intelligence platforms that solve real-world problems at scale. "
        "My work spans financial crime detection, regulatory ML research, "
        "energy market forecasting, and AI-powered applications — from raw "
        "data ingestion through to deployed, stakeholder-facing products."
    ),
    "email":    "fannanafahreen@gmail.com",
    "phone":    "07466158752",
    "github":   "https://github.com/fannanafahreen",
    "linkedin": "https://www.linkedin.com/in/fannana-fahreen/",
    "location": "London, UK",
}

# ── Skills ───────────────────────────────────────────────────
# Each skill group has a label and a list of items.
# Each item has a display name and a Font Awesome 6 icon class,
# rendered as an icon card in the Skills section.
skill_groups = [
    {
        "label": "Programming Languages",
        "items": [
            {"name": "Python",      "icon": "fa-brands fa-python"},
            {"name": "SQL",         "icon": "fa-solid fa-database"},
            {"name": "JavaScript",  "icon": "fa-brands fa-js"},
            {"name": "HTML & CSS",  "icon": "fa-brands fa-html5"},
            {"name": "Kotlin",      "icon": "fa-solid fa-mobile"},
            {"name": "C",           "icon": "fa-solid fa-code"},
        ],
    },
    {
        "label": "Machine Learning",
        "items": [
            {"name": "Scikit-learn",                   "icon": "fa-solid fa-brain"},
            {"name": "XGBoost",                         "icon": "fa-solid fa-bolt"},
            {"name": "Random Forest",                   "icon": "fa-solid fa-tree"},
            {"name": "Isolation Forest",                "icon": "fa-solid fa-filter"},
            {"name": "Feature Engineering",              "icon": "fa-solid fa-wrench"},
            {"name": "Anomaly Detection",                "icon": "fa-solid fa-triangle-exclamation"},
            {"name": "Model Evaluation",                 "icon": "fa-solid fa-chart-bar"},
            {"name": "Class Imbalance Handling",         "icon": "fa-solid fa-scale-balanced"},
            {"name": "Cross-Validation",                 "icon": "fa-solid fa-rotate"},
            {"name": "Expanding-Window Backtesting",     "icon": "fa-solid fa-clock-rotate-left"},
        ],
    },
    {
        "label": "AI & LLM Systems",
        "items": [
            {"name": "LangChain",                "icon": "fa-solid fa-link"},
            {"name": "FAISS",                     "icon": "fa-solid fa-magnifying-glass"},
            {"name": "sentence-transformers",     "icon": "fa-solid fa-vector-square"},
            {"name": "Amazon Bedrock",            "icon": "fa-brands fa-aws"},
            {"name": "OpenAI GPT-4o-mini",        "icon": "fa-solid fa-robot"},
            {"name": "Prompt Engineering",        "icon": "fa-solid fa-terminal"},
            {"name": "RAG Pipelines",             "icon": "fa-solid fa-sitemap"},
            {"name": "PDF Parsing",               "icon": "fa-solid fa-file-pdf"},
            {"name": "Semantic Chunking",         "icon": "fa-solid fa-scissors"},
            {"name": "AI Workflow Automation",    "icon": "fa-solid fa-gears"},
        ],
    },
    {
        "label": "Graph & Network Analysis",
        "items": [
            {"name": "NetworkX",                     "icon": "fa-solid fa-diagram-project"},
            {"name": "Neo4j",                         "icon": "fa-solid fa-circle-nodes"},
            {"name": "Louvain Community Detection",   "icon": "fa-solid fa-object-group"},
            {"name": "Betweenness Centrality",        "icon": "fa-solid fa-network-wired"},
            {"name": "Link Prediction",               "icon": "fa-solid fa-arrows-to-dot"},
            {"name": "Cytoscape.js",                  "icon": "fa-solid fa-share-nodes"},
            {"name": "Graph Database Design",         "icon": "fa-solid fa-database"},
        ],
    },
    {
        "label": "Time-Series & Forecasting",
        "items": [
            {"name": "Autocorrelation Analysis",          "icon": "fa-solid fa-chart-line"},
            {"name": "Seasonal Decomposition",            "icon": "fa-solid fa-wave-square"},
            {"name": "Lag Feature Engineering",           "icon": "fa-solid fa-hourglass-half"},
            {"name": "Rolling Statistics",                "icon": "fa-solid fa-chart-area"},
            {"name": "Volatility Regime Classification",  "icon": "fa-solid fa-chart-simple"},
            {"name": "Data Leakage Prevention",           "icon": "fa-solid fa-shield-halved"},
        ],
    },
    {
        "label": "Data Engineering & ETL",
        "items": [
            {"name": "Pandas",                  "icon": "fa-solid fa-table"},
            {"name": "NumPy",                    "icon": "fa-solid fa-square-root-variable"},
            {"name": "SciPy",                    "icon": "fa-solid fa-flask"},
            {"name": "ETL Pipeline Design",      "icon": "fa-solid fa-pipe-section"},
            {"name": "RapidFuzz",                "icon": "fa-solid fa-spell-check"},
            {"name": "PostgreSQL",               "icon": "fa-solid fa-database"},
            {"name": "MySQL",                    "icon": "fa-solid fa-database"},
            {"name": "SQLite",                   "icon": "fa-solid fa-database"},
            {"name": "SQLAlchemy",               "icon": "fa-solid fa-layer-group"},
            {"name": "Firebase",                 "icon": "fa-solid fa-fire"},
            {"name": "Star Schema Modelling",    "icon": "fa-solid fa-star"},
            {"name": "Data Quality Assurance",   "icon": "fa-solid fa-list-check"},
            {"name": "EDA",                      "icon": "fa-solid fa-magnifying-glass-chart"},
        ],
    },
    {
        "label": "Cloud & DevOps",
        "items": [
            {"name": "AWS EC2",           "icon": "fa-brands fa-aws"},
            {"name": "AWS IAM",           "icon": "fa-solid fa-user-shield"},
            {"name": "Docker",            "icon": "fa-brands fa-docker"},
            {"name": "Docker Compose",    "icon": "fa-solid fa-boxes-stacked"},
            {"name": "Git",               "icon": "fa-brands fa-git-alt"},
            {"name": "GitHub",            "icon": "fa-brands fa-github"},
            {"name": "Render",            "icon": "fa-solid fa-server"},
            {"name": "Vercel",            "icon": "fa-solid fa-rocket"},
            {"name": "Netlify",           "icon": "fa-solid fa-cloud"},
        ],
    },
    {
        "label": "Full-Stack Development",
        "items": [
            {"name": "FastAPI",         "icon": "fa-solid fa-bolt"},
            {"name": "Flask",           "icon": "fa-solid fa-flask"},
            {"name": "React 18",        "icon": "fa-brands fa-react"},
            {"name": "Vite",            "icon": "fa-solid fa-fire"},
            {"name": "React Router",    "icon": "fa-solid fa-route"},
            {"name": "Recharts",        "icon": "fa-solid fa-chart-pie"},
        ],
    },
    {
        "label": "Geographic & Mapping",
        "items": [
            {"name": "Leaflet.js",                  "icon": "fa-solid fa-map-location-dot"},
            {"name": "Choropleth Visualisation",    "icon": "fa-solid fa-earth-europe"},
            {"name": "Spatial Data Rendering",      "icon": "fa-solid fa-location-dot"},
        ],
    },
    {
        "label": "BI & Visualisation",
        "items": [
            {"name": "Power BI",        "icon": "fa-solid fa-chart-column"},
            {"name": "DAX",             "icon": "fa-solid fa-function"},
            {"name": "Power Query",     "icon": "fa-solid fa-filter"},
            {"name": "Matplotlib",      "icon": "fa-solid fa-chart-line"},
            {"name": "Seaborn",         "icon": "fa-solid fa-chart-area"},
            {"name": "Excel",           "icon": "fa-solid fa-file-excel"},
            {"name": "Power Pivot",     "icon": "fa-solid fa-table-columns"},
        ],
    },
    {
        "label": "Financial Crime & Regulatory",
        "items": [
            {"name": "Fraud Detection",              "icon": "fa-solid fa-shield-halved"},
            {"name": "Financial Crime Analytics",    "icon": "fa-solid fa-magnifying-glass-dollar"},
            {"name": "FCA Regulatory ML",            "icon": "fa-solid fa-landmark"},
            {"name": "Corporate Network Analysis",   "icon": "fa-solid fa-building"},
            {"name": "Phoenix Company Detection",    "icon": "fa-solid fa-fire-flame-curved"},
        ],
    },
    {
        "label": "Workflow Automation",
        "items": [
            {"name": "Go High Level",        "icon": "fa-solid fa-wand-magic-sparkles"},
            {"name": "Outreach Automation",  "icon": "fa-solid fa-paper-plane"},
            {"name": "Form Automation",      "icon": "fa-solid fa-envelope-open-text"},
        ],
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
# "category" is optional — when present it renders as a small gold
# tag at the top of the project card. "link" of None renders a
# "Pending Publication" badge instead of a View link.
projects = [
    {
        "title":       "Ask My Documents — RAG-Powered Regulatory Research Assistant",
        "description": (
            "Full-stack AI application that transforms FCA enforcement notices into an "
            "interactive, queryable knowledge base. Built a complete RAG pipeline from "
            "scratch covering PDF parsing, semantic chunking, and vector embeddings using "
            "sentence-transformers. Implements FAISS for fast similarity search across "
            "document chunks and integrates Amazon Bedrock (Nova 2 Lite) for grounded, "
            "hallucination-resistant answer generation. Provisioned full AWS infrastructure "
            "(EC2, IAM roles, security groups) with a focus on cost control and security best "
            "practices. Diagnosed and resolved real memory allocation constraints on cloud "
            "instances by migrating from self-hosted inference to managed AI infrastructure."
        ),
        "tags":     ["Python", "FastAPI", "FAISS", "sentence-transformers", "Amazon Bedrock", "AWS EC2", "AWS IAM", "HTML/CSS/JavaScript", "Git/GitHub"],
        "link":     "https://github.com/fannanafahreen/FCA-disciplinary-Q-A-App",
        "category": "GenAI / RAG / AWS",
    },
    {
        "title":       "FCA Adverse Outcome Prediction — Regulatory ML Research",
        "description": (
            "ML research pipeline to predict adverse regulatory outcomes for FCA-regulated "
            "firms. Applies XGBoost classification with an expanding-window backtesting "
            "methodology to preserve temporal integrity and prevent data leakage. Involves "
            "financial regulatory data analysis and feature engineering across FCA firm-level "
            "datasets. Currently being prepared for academic publication."
        ),
        "tags":     ["Python", "XGBoost", "Pandas", "Scikit-learn", "Jupyter"],
        "link":     None,
        "category": "Regulatory ML / Research",
    },
    {
        "title":       "LondonWatch",
        "description": (
            "Full-stack intelligence platform analysing 5.7M+ UK Companies House records and "
            "2M+ Land Registry records to detect business networks associated with human "
            "trafficking and labour exploitation across London. Applies Social Network Analysis "
            "(NetworkX, Louvain community detection, betweenness centrality, link prediction) to "
            "a graph of 569,000+ nodes and 366,000+ edges, surfacing 215,000+ corporate rings. "
            "Uses Isolation Forest for director anomaly detection and a weakly-supervised Random "
            "Forest for ring risk scoring across 150,000+ directors, with RapidFuzz name-matching "
            "deduplication and phoenix-company fraud detection."
        ),
        "tags":  ["Python", "FastAPI", "PostgreSQL", "Neo4j", "React", "Leaflet.js", "Cytoscape.js", "NetworkX", "Scikit-learn", "Docker"],
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
        "title":       "FraudGuard",
        "description": (
            "Real-time fraud detection dashboard trained on 284,807 credit-card transactions "
            "(0.17% fraud rate, 578:1 class imbalance). An XGBoost classifier with PR-AUC-optimised "
            "thresholds flags transactions as Fraud / Review / Safe, and a LangChain + OpenAI "
            "GPT-4o-mini pipeline generates plain-language explanations for every flagged case. "
            "React dashboard shows live KPI cards, a real-time transaction feed, fraud-by-hour "
            "trends, and model performance metrics. Deployed via Docker Compose, Render, and Vercel."
        ),
        "tags":  ["Python", "FastAPI", "XGBoost", "LangChain", "OpenAI GPT-4o-mini", "React", "Docker"],
        "link":  "https://github.com/fannanafahreen/fraud-detector",
    },
    {
        "title":       "GB Electricity Price Forecasting",
        "description": (
            "Quantitative forecasting pipeline for GB electricity price exposure, joining 6 years "
            "of daily data from four live UK energy APIs (Elexon BMRS, Ofgem, National Grid NESO, "
            "Open-Meteo ERA5). EDA identified gas price and autocorrelation as primary drivers; "
            "44 engineered features feed an XGBoost regressor achieving R²=0.97 and MAPE=5.99% "
            "on 351 unseen test days."
        ),
        "tags":  ["Python", "XGBoost", "Pandas", "NumPy", "Scikit-learn", "REST APIs"],
        "link":  "https://github.com/fannanafahreen/Nationwide-utilities-energy-forecast",
    },
    {
        "title":       "Customer Churn Predictor",
        "description": "End-to-end ML pipeline (EDA → feature engineering → "
                       "Random Forest) achieving 87 % accuracy on test data.",
        "tags":  ["Python", "Scikit-learn", "Pandas", "Jupyter"],
        "link":  "https://github.com/fannanafahreen/Customer-churn",
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


# ── Certifications & Virtual Experience ─────────────────────
certifications = [
    {
        "title":  "Lloyds Banking Group — Step Up Career Challenge",
        "issuer": "Digdata / The Data Inspiration Group",
        "period": "2025",
        "detail": (
            "Completed real-world data projects in financial services, recognised by the "
            "Group Chief Data & Analytics Officer, Lloyds Banking Group."
        ),
        "link":   "https://drive.google.com/file/d/1du58JCSH3I72xvbyhIDrYgWKM9xReN32/view?usp=sharing",
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
        certifications=certifications,
    )


# ── Entry point ──────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)
