# 🛡️ CyberShield – Open-Source SIEM & Log Monitoring System

**CyberShield** is a Python-based Security Information and Event Management (SIEM) project designed to monitor system activity, detect suspicious behavior, and identify potential security threats through real-time monitoring and event logging.

The project combines system monitoring, brute-force detection, File Integrity Monitoring (FIM), and a web-based security dashboard.

## 🚀 Features

- **System Monitoring:** Monitor CPU, RAM, disk usage, hostname, and operating system information.
- **Brute-Force Detection:** Detect repeated failed login attempts using a rule-based detection mechanism.
- **File Integrity Monitoring:** Monitor file creation, modification, and deletion.
- **Security Event Logging:** Store detected security events in an SQLite database.
- **Security Dashboard:** View system statistics, security alerts, and event severity.
- **REST API:** Access monitoring and security features through FastAPI endpoints.

## 📸 Project Screenshots

### CyberShield Security Dashboard

![CyberShield Dashboard](screenshots/dashboard.png)

![CyberShield Dashboard](screenshots/dashboard.png)

## 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| FastAPI | REST API |
| SQLite | Event and system data storage |
| Watchdog | File monitoring |
| Psutil | System monitoring |
| HTML, CSS, JavaScript | Dashboard |
| Chart.js | Security analytics |
| Git & GitHub | Version control |

## 📁 Project Structure

```text
CyberShield/
│
├── app/
│   ├── collector/
│   │   ├── file_monitor.py
│   │   └── system_collector.py
│   │
│   ├── database/
│   │   └── db.py
│   │
│   ├── detector/
│   │   └── rules.py
│   │
│   └── main.py
│
├── dashboard/
│   ├── .gitignore
│   └── index.html
│
├── logs/
├── .gitignore
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/nikhildubey14012007-tech/Cybershield.git
```

### 2. Open the project folder

```bash
cd Cybershield
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install fastapi uvicorn psutil watchdog
```

### 6. Start the backend server

```bash
uvicorn app.main:app --reload
```

## 🌐 Access the Application

| Component | URL |
|---|---|
| Backend API | http://127.0.0.1:8000 |
| API Documentation | http://127.0.0.1:8000/docs |
| Health Check | http://127.0.0.1:8000/health |
| Dashboard | http://127.0.0.1:5500/dashboard/index.html |

To launch the dashboard, open `dashboard/index.html` using the VS Code Live Server extension.

## 🔍 API Endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| `/` | GET | Root endpoint |
| `/health` | GET | Check application health |
| `/system-info` | GET | Retrieve system information |
| `/snapshots` | GET | Retrieve system snapshots |
| `/simulate-login` | GET | Simulate failed login attempts |
| `/security-events` | GET | Retrieve security events |
| `/fim/start` | POST | Start file integrity monitoring |
| `/fim/stop` | POST | Stop file integrity monitoring |
| `/live-system-info` | GET | Retrieve live system metrics |

## 🛡️ Security Detection

CyberShield currently includes:

- Rule-based brute-force detection using a threshold of five or more failed login attempts.
- File creation detection.
- File modification detection.
- File deletion detection.
- Security event classification by severity.

## 🎯 Project Objectives

1. Understand the fundamentals of SIEM architecture.
2. Develop practical cybersecurity monitoring skills.
3. Learn log collection and security event analysis.
4. Implement rule-based threat detection.
5. Build a centralized security monitoring dashboard.

## 🔮 Future Enhancements

- Network traffic monitoring.
- Intrusion Detection System (IDS).
- Advanced threat detection rules.
- IP reputation analysis.
- Authentication log monitoring.
- Machine learning-based anomaly detection.
- Improved alert management and reporting.

## ⚠️ Disclaimer

CyberShield is an educational cybersecurity project and a work in progress. Its current detection mechanisms are prototype implementations and should not be considered a replacement for a production SIEM or enterprise security solution.

## 👨‍💻 Developer

**Nikhil Dubey**

B.Tech CSE – Cyber Security & Digital Forensics

GitHub: [@nikhildubey14012007-tech](https://github.com/nikhildubey14012007-tech)

---

⭐ If you find this project interesting, consider starring the repository!