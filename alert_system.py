# src/alert_system.py
import sys
import os

# Add src/ to sys.path so Python can find detect_violations
sys.path.append(os.path.dirname(__file__))

from detect_violations import detect_violations

def alert_system():
    violations = detect_violations()
    if violations:
        print("⚠️ ALERT! SLA Violations detected:")
        for v in violations:
            print(v)
    else:
        print("✅ No SLA violations detected.")

if __name__ == "__main__":
    alert_system()
