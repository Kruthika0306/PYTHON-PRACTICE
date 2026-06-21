candidates = {
    "Rahul": 82,
    "Ananya": 91,
    "Vikram": 67,
    "Sneha": 88
}

for name, score in candidates.items():
    if score >= 80:
        print(name, "- Shortlisted")
    else:
        print(name, "- Rejected")

print("Screening Completed")
