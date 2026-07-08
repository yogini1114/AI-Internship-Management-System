# 🎓 AI Internship Management System

An AI-powered Internship Management Platform built using **FastAPI**, **Streamlit**, **SQLite**, **SQLAlchemy**, **Groq LLM**, and the **GitHub REST API**. The platform helps organizations efficiently manage interns by tracking attendance, monitoring progress, analyzing GitHub repositories, generating AI-powered insights, and determining certificate eligibility.

---

## 🚀 Features

### 👨‍🎓 Intern Management
- Create, Read, Update, Delete (CRUD) Intern Records
- View Individual Intern Profiles
- Track Internship Status

### 📈 Progress Tracking
- Monitor Internship Completion
- Weekly Progress Statistics
- Overall Performance Tracking

### 📅 Attendance Analyzer
- Attendance Percentage
- Weekly & Monthly Attendance
- Consistency Score
- AI Generated Attendance Summary

### 🧑‍🏫 Mentor Dashboard
- Total Interns
- Active / Inactive Interns
- Pending Submissions
- Top Performers
- Weak Performers
- AI Recommendations

### 📊 Analytics Dashboard
- Overall Internship Statistics
- Domain-wise Distribution
- Mentor Workload
- Internship Health Score
- AI Generated Insights

### 🎯 Task Recommendation System
- Personalized Learning Recommendations
- Weak Skill Identification
- Suggested Projects
- Recommended Courses
- Revision Topics

### 🐙 GitHub Repository Analyzer
- GitHub Repository Analysis
- Repository Quality Assessment
- Documentation Score
- Code Quality Score
- Git Practices Score
- AI Suggestions using Groq LLM

### 🎓 Certificate Eligibility Analyzer
- Attendance Score
- Task Performance
- GitHub Score
- Mentor Score
- Overall Performance Score
- Eligibility Decision
- AI Generated Remarks

---

# 🛠 Tech Stack

## Frontend
- Streamlit

## Backend
- FastAPI

## Database
- SQLite
- SQLAlchemy ORM

## AI
- Groq LLM
- GitHub REST API

## Language
- Python 3

---

# 📂 Project Structure

```
AI-Internship-Management-System
│
├── backend
│   ├── api
│   ├── database
│   ├── models
│   ├── services
│   ├── ai_modules
│   └── main.py
│
├── frontend
│   ├── pages
│   ├── utils
│   └── streamlit_app.py
│
├── datasets
│
├── requirements.txt
│
├── .env.example
│
└── README.md
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/yogini1114/AI-Internship-Management-System.git
```

```bash
cd AI-Internship-Management-System
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

```
GROQ_API_KEY=YOUR_GROQ_API_KEY
GITHUB_TOKEN=YOUR_GITHUB_TOKEN
```

---

# ▶ Run Backend

```bash
uvicorn backend.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# ▶ Run Frontend

```bash
streamlit run frontend/streamlit_app.py
```

Frontend URL

```
http://localhost:8501
```

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /health | Health Check |
| POST | /api/interns | Create Intern |
| GET | /api/interns | Get All Interns |
| GET | /api/interns/{id} | Get Intern |
| PUT | /api/interns/{id} | Update Intern |
| DELETE | /api/interns/{id} | Delete Intern |
| GET | /api/progress/{id} | Progress Tracker |
| GET | /api/attendance/{id} | Attendance |
| GET | /api/mentor-dashboard | Mentor Dashboard |
| GET | /api/analytics | Analytics |
| GET | /api/task-recommendations/{id} | Task Recommendation |
| GET | /api/certificate/{id} | Certificate Eligibility |
| POST | /api/github-analysis | GitHub Repository Analysis |

---

# 📸 Screenshots

Add screenshots here.

```
screenshots/

Home.png

Intern_Profile.png

Mentor_Dashboard.png

Analytics.png

Certificate.png

GitHub_Analyzer.png

Swagger.png
```

---

# 🔮 Future Enhancements

- JWT Authentication
- Role Based Access Control
- Email Notifications
- Live GitHub Monitoring
- AI Chatbot for Mentors
- Resume Analysis
- Interview Readiness Assessment
- Deployment on AWS / Azure
- Docker Support
- CI/CD Pipeline

---

# 💡 Key Highlights

- AI Powered Internship Analytics
- Real-Time GitHub Repository Analysis
- Intelligent Certificate Eligibility Evaluation
- Mentor Performance Dashboard
- Attendance Analytics
- RESTful API Architecture
- Modular Project Structure
- Scalable Backend Design

---

# 👨‍💻 Author

Developed by **Yogini Nishad**

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.