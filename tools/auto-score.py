import csv

def auto_score(test_matrix_path):
    with open(test_matrix_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        total = 0
        passed = 0
        for row in reader:
            total += 1
            if row['Pass/Fail'].strip().lower() == 'pass':
                passed += 1
        if total == 0:
            return 0.0
        return round(100 * passed / total, 2)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python auto-score.py <test-matrix.csv>")
    else:
        score = auto_score(sys.argv[1])
        print(f"Pass rate: {score}%")
