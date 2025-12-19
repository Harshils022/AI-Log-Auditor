import ollama
import time 
import os

# 1. Define the 'Security Analyst' Persona
SYSTEM_PROMPT = """
You are a SOC Tier 2 Analyst. Analyze the following log entries. 
Ignore routine successful logins or 'boring' info messages.
Highlight:
- Brute force attempts (repeated failures)
- SQL Injection patterns (e.g., SELECT, UNION, --)
- Path Traversal (../../)
Provide a 2-sentence summary of the threat and a severity score (Low/Medium/High).
"""

def analyze_logs(log_data):
    # Using the SYSTEM_PROMPT we defined above
    response = ollama.chat(model='gemma:2b', messages=[
        {'role': 'system', 'content': SYSTEM_PROMPT},
        {'role': 'user', 'content': f"Analyze this log entry:\n{log_data}"}
    ])
    return response['message']['content']

def watch_logs(filename): # Changed 'access.log' to 'filename' (variable)
    print(f"[*] Monitoring {filename} for threats...")

    with open(filename, "r") as f:
        # Move to the end of the file so we only see NEW logs
        f.seek(0, os.SEEK_END)

        while True: # 'True' must be capitalized in Python
            line = f.readline()
            if not line:
                time.sleep(1)
                continue

            # If a new line appears, send it to AI
            print(f"\n[NEW LOG DETECTED]: {line.strip()}")
            report = analyze_logs(line)
            print(f"[AI ANALYSIS]:\n{report}")
            print("-" * 50)

if __name__ == "__main__":
    print("--- AI Security Audit Starting ---")
    
    # Ensure the file exists
    if not os.path.exists("access.log"):
        with open("access.log", "w") as f:
            f.write("Log file initialized.\n")

    # Start the monitoring loop
    watch_logs("access.log")