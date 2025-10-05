import csv

def analyze_failures(test_matrix_path):
    with open(test_matrix_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        failures = [row for row in reader if row['Pass/Fail'].strip().lower() != 'pass']
    for fail in failures:
        print(f"Test: {fail['Test Case']} | Notes: {fail['Notes']}")
    print(f"Total failures: {len(failures)}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python failure-analyzer.py <test-matrix.csv>")
    else:
        analyze_failures(sys.argv[1])
