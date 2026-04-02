🚀 Incident Diagnostics API (SRE Project)

📌 Overview

This project is a Flask-based Incident Diagnostics API designed from an SRE (Site Reliability Engineering) perspective.

It helps automate incident triage by:
	•	Checking application service status (process-level)
	•	Validating database connectivity
	•	Fetching and analyzing logs
	•	Returning a structured diagnostic report

⸻

🧠 Architecture

Client (ServiceNow / curl / API)
        │
        ▼
Flask API (app.py)
        │
        ▼
Routes (Controller Layer)
        │
        ▼
Services (Business Logic)
        │
        ▼
System Dependencies
   ├── OS Process (pgrep)
   ├── SQLite DB
   └── Log Files


⸻

🎯 Features
	•	✅ API health check (/health/app)
	•	✅ Service health check using pgrep
	•	✅ Database connectivity validation
	•	✅ Log retrieval (tail last N lines)
	•	✅ Root Cause Analysis (RCA engine)
	•	✅ Incident analysis API
	•	✅ Unit + Integration + API tests
	•	✅ CI/CD pipeline (GitHub Actions)
	•	✅ Self-hosted runner deployment (enterprise-style)

⸻

📁 Project Structure

incident-diagnostics-api/
│
├── app.py
├── routes/
│   ├── health.py
│   └── incident.py
│
├── services/
│   ├── service_checker.py
│   ├── db_checker.py
│   ├── log_service.py
│   └── analyzer.py
│
├── utils/
│   └── config.py
│
├── logs/
├── database/
├── tests/
│   ├── test_services.py
│   ├── test_api.py
│   └── test_api_requests.py
│
├── dummy_service.py
├── requirements.txt
├── pytest.ini
└── README.md


⸻

⚙️ Setup Instructions

1️⃣ Clone Repository

git clone <your-repo-url>
cd incident-diagnostics-api


⸻

2️⃣ Create Virtual Environment

python3 -m venv venv
source venv/bin/activate


⸻

3️⃣ Install Dependencies

pip install -r requirements.txt


⸻

4️⃣ Setup Database

python setup/setup_db.py


⸻

5️⃣ Create Logs

echo "INFO: App started" >> logs/app.log
echo "ERROR: connection refused to DB" >> logs/app.log


⸻

6️⃣ Start Dummy Service (Simulated App)

python dummy_service.py


⸻

7️⃣ Start API

python app.py


⸻


8️⃣ Configure API Secret Key

```bash
export API_SECRET_KEY=your-strong-secret
```

All non-health endpoints now require `X-API-KEY` header with this value.

Example:

```bash
curl -X POST http://localhost:8000/incident/analyze \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: $API_SECRET_KEY" \
  -d '{"incident_id":"INC12345","service_name":"dummy_service.py"}'
```

⸻

🧪 API Endpoints

🔹 API Health

GET /health/app

🔹 Service Health

GET /health/dependency/service

🔹 Database Health

GET /health/dependency/db

🔥 Incident Analysis

POST /incident/analyze (requires `X-API-KEY`)


⸻

🧪 Testing

Run All Tests

```bash
pytest
```

Run only API tests:

```bash
pytest tests/test_api.py
```


⸻

🔄 CI/CD Pipeline

🧠 Architecture

Cloud Runner (CI)
   ├── Build
   ├── Test
   ├── Create Artifact
        │
        ▼
Self-hosted Runner (CD)
   ├── Download Artifact
   ├── Deploy
   ├── Install Dependencies (venv + pip)
   └── Restart App

The workflow triggers on:
- `push` to `main`
- `pull_request` targeting `main`

Deployment requires repository secret:
- `API_SECRET_KEY`

Deployment health check retries startup and prints `output.log` on failure for faster debugging.
Deployment launch unsets `RUNNER_TRACKING_ID` so the app process is not reaped when the GitHub runner job exits.


⸻

🚀 Pipeline Stages
	1.	Build
	2.	Test (pytest)
	3.	Artifact packaging (.tar.gz)
	4.	Deployment via self-hosted runner
	5.	Health check verification
⸻

🖥️ Self-Hosted Runner

This project uses a self-hosted runner to simulate enterprise deployment.

⸻

🧠 SRE Concepts Demonstrated
	•	Service monitoring (process-level)
	•	Dependency health checks
	•	Log-based diagnostics
	•	Incident automation
	•	CI/CD pipelines
	•	Artifact-based deployment

⸻

🔥 Future Improvements
	•	Dockerize application
	•	Add metrics (Prometheus)
	•	Add dashboard (Grafana)
	•	Implement rollback mechanism

⸻

👨‍💻 Author

Suraj Armugham

⸻

⭐ Final Note

This project simulates real-world SRE workflows:

Detection → Diagnosis → Automation → Deployment
