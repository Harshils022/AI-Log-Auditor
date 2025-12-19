# AI-Log-Auditor
A real-time SOC automation tool that uses a local LLM (Google Gemma:2b) to analyze system logs, identify security threats (SQLi, Brute Force, Path Traversal), and reduce alert fatigue for security analysts.

AI-Powered Automated Log Auditor
"Automating Tier-1 SOC Analysis with Generative AI"

🛡️ Project Overview
This project is a Security Automation tool designed to combat "Alert Fatigue." It monitors system logs in real-time and uses a local Large Language Model (LLM) to distinguish between routine traffic and actual security threats.

By using Google's Gemma:2b running locally via Ollama, this tool ensures that sensitive log data never leaves the local machine, maintaining strict data privacy while providing advanced threat intelligence.

🚀 Key Features
Real-time Monitoring: Functions like tail -f to watch log files as entries are written.

Local AI Inference: Uses Gemma:2b to analyze logs offline (No API keys required, no cloud costs).

Intelligent Triage: Specifically tuned to identify:

Brute Force Attacks: Repeated failed login attempts.

SQL Injection: Detecting malicious query patterns.

Path Traversal: Identifying unauthorized directory access attempts.

Rate Limiting: Built-in safeguards to manage CPU/RAM usage during high-traffic periods.

🛠️ Tech Stack
Language: Python 3.x

AI Model: Google Gemma:2b (via Ollama)

Environment: Linux/macOS/Windows

Libraries: ollama, os, time

📂 Project Structure
Plaintext

.
├── auditor.py         # The main Python automation script
├── access.log         # The log file being monitored (Target)
└── threat_report.csv  # (Optional) Exported threat summaries
🚦 How to Run
Install Ollama: Download from ollama.com.

Pull the Model:

Bash
ollama pull gemma:2b
Run the Auditor:

Bash
python auditor.py
Simulate an Attack: Open a second terminal and run:

Bash
echo '192.168.1.100 - - "GET /etc/passwd HTTP/1.1" 404' >> access.log


📈 Impact & Career Relevance
This project demonstrates skills required for SOC Analyst, Security Engineer, and AI/ML SecOps roles:

Scripting: Proficiency in Python for system automation.

LLM Implementation: Knowledge of prompt engineering and local model deployment.

Security Domain Knowledge: Understanding of common web attack vectors (OWASP Top 10).

Resource Management: Implementation of rate-limiting to ensure system stability.
