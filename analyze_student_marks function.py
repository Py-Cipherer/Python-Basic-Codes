students = [
    {
        "name": "Alice",
        "grades": {"Math": 85, "Science": 92, "English": 88}
    },
    {
        "name": "Bob",
        "grades": {"Math": 79, "Science": 85, "English": 90}
    },
    {
        "name": "Charlie",
        "grades": {"Math": 95, "Science": 100, "English": 93}
    }
]

def analyze_grades(students):
    d = {}
    total_math = 0
    total_science = 0
    total_english = 0
    num_students = len(students)
    
    for student in students:
        name = student["name"]
        grades = student["grades"]
        math = grades["Math"]
        science = grades["Science"]
        english = grades["English"]
        
        total_math += math
        total_science += science
        total_english += english
        
        average_grade = sum(grades.values()) / len(grades)
        d[name] = average_grade
    
    highest_avg = max(d.values())
    lowest_avg = min(d.values())
    
    result = {
        "Highest Average": (next(k for k, v in d.items() if v == highest_avg), round(highest_avg, 2)),
        "Lowest Average": (next(k for k, v in d.items() if v == lowest_avg), round(lowest_avg, 2)),
        "Subject Averages": {
            "Math": round(total_math / num_students, 2),
            "Science": round(total_science / num_students, 2),
            "English": round(total_english / num_students, 2)
        }
    }
    
    return result

# Example Usage
result = analyze_grades(students)
print(result)
