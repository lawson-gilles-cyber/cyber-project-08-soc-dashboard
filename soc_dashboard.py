# Mini SOC Dashboard - Log Visualization

# Sample logs (simulating SIEM input)
logs = [
    "LOGIN FAILED - admin - 45.33.32.1",
    "LOGIN FAILED - admin - 45.33.32.1",
    "LOGIN SUCCESS - admin - 45.33.32.1",
    "FILE ACCESS - confidential.docx",
    "LOGIN FAILED - user - 192.168.1.5"
]

# Initialize counters
failed_logins = 0
successful_logins = 0
file_access_events = 0

# Loop through logs to categorize events
for log in logs:
    # Check for failed login attempts
    if "LOGIN FAILED" in log:
        failed_logins += 1

    # Check for successful login
    elif "LOGIN SUCCESS" in log:
        successful_logins += 1

    # Check for file access events
    elif "FILE ACCESS" in log:
        file_access_events += 1

# Display dashboard output
print("=== SOC DASHBOARD ===\n")

print(f"Failed Logins: {failed_logins}")
print(f"Successful Logins: {successful_logins}")
print(f"Sensitive File Access Events: {file_access_events}\n")

# Basic threat interpretation
if failed_logins >= 3:
    print("[ALERT] Possible brute force attack detected")

if file_access_events > 0:
    print("[ALERT] Sensitive file access detected")
