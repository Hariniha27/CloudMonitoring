# Cloud Monitoring SLA Alert System ☁️🚨

---

## 📘 Project Overview

The **Cloud Monitoring SLA Alert System** is a Python-based project that monitors cloud service metrics and detects **SLA (Service Level Agreement) violations** in real-time.

It reads metrics such as **CPU usage**, **Memory usage**, **Response Time**, and **Disk I/O** from a CSV dataset, compares them against SLA thresholds, and immediately alerts administrators about any violations.

This system helps ensure cloud services remain **reliable, accountable, and transparent**, improving operational efficiency and trust in cloud infrastructure.

---

## 🎯 SDG Alignment

This project aligns with **UN Sustainable Development Goal 16: Peace, Justice, and Strong Institutions**, as it promotes **accountability and transparency** in digital service management.

| **SDG** | **Goal** | **How This Project Aligns** |
|:--------:|-----------|-----------------------------|
| **16** | *Peace, Justice, and Strong Institutions* | Provides automated SLA monitoring, ensuring cloud services remain reliable and transparent. Supports institutional trust and responsible management of digital infrastructure. |

---

## ⚙️ Setup and Installation

### 🧩 Prerequisites
- Python 3.x installed  
- Project folder contains `src/alert_system.py` and a CSV dataset with metrics  

### 🚀 Setup

**1. Create a virtual environment:**
```bash
python -m venv venv
```
**2. Activate the environment:**
```bash
Windows:
venv\Scripts\activate
```
**▶️ Run the alert system**
```bash
python src/alert_system.py
```
***📊 Sample Outputs***
```bash
✅ No SLA violations detected.

⚠️ ALERT! SLA Violations detected:
{'timestamp': '2025-10-25 12:20:00', 'service_name': 'ServiceX', 'CPU_usage': 35, 'Memory_usage': 45, 'response_time': 600.0, 'Disk_IO': 110}
```
