# Student/status.py

def check_status(avg):
    """Check if the student passed based on the average"""
    if avg >= 10:
        return "Acc"  # Accepted / Passed
    else:
        return "Fail" # Rejected / Failed