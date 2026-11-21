# Student/grades.py

def calculate_avg(grades_list):
    """Calculate the average of grades"""
    if not grades_list:
        return 0
    return sum(grades_list) / len(grades_list)

def find_max(grades_list):
    """Find the maximum grade"""
    if not grades_list:
        return 0
    return max(grades_list)

def find_min(grades_list):
    """Find the minimum grade"""
    if not grades_list:
        return 0
    return min(grades_list)