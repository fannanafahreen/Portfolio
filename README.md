# Fannana Fahreen — Portfolio Website

A CV-style personal portfolio built with Python (Flask) and plain HTML/CSS. No frontend frameworks — just clean, handwritten code.

---

## About

This portfolio showcases my background in Data Science, including my skills, education, work experience, and projects. It uses a two-column layout with a fixed sidebar and a scrollable main content area.

---

## Features

- Responsive two-column layout (sidebar + main)
- Sticky sidebar with profile photo, bio, and contact links
- Sections: Skills, Education, Work Experience, Projects
- All content managed from a single Python file (`app.py`) — no HTML edits needed to update content
- Mobile-friendly (stacks to single column on small screens)

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Templating | Jinja2 |
| Frontend | HTML5, CSS3 (plain, no frameworks) |

---

## Project Structure

```
Portfolio/
├── app.py               # Flask app + all page content (data lives here)
├── static/
│   ├── style.css        # All styling
│   └── Fannana.jpg      # Profile photo
└── templates/
    ├── base.html        # Shared layout (sidebar + page shell)
    ├── index.html       # Main CV page (skills, education, experience, projects)
    └── projects.html    # Redirects to home
```

---

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/fannanafahreen/Portfolio.git
cd Portfolio
```

**2. Install Flask**
```bash
pip install flask
```

**3. Run the app**
```bash
python app.py
```

**4. Open in browser**
```
http://127.0.0.1:5000
```

---

## Updating Content

All content lives in `app.py` as Python dictionaries and lists. To update anything — just edit that file and refresh the browser. No HTML changes needed.

| What to update | Where in app.py |
|---|---|
| Name, bio, email, phone, links | `owner` dict |
| Skills | `skill_groups` list |
| Education | `education` list |
| Work experience | `experience` list |
| Projects | `projects` list |

---

## Contact

- Email: [fannanafahreen@gmail.com](mailto:fannanafahreen@gmail.com)
- LinkedIn: [linkedin.com/in/fannana-fahreen](https://www.linkedin.com/in/fannana-fahreen/)
- GitHub: [github.com/fannanafahreen](https://github.com/fannanafahreen)
- URL: [my-portfolio-m8mc.onrender](https://my-portfolio-m8mc.onrender.com/)
