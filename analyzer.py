from rules import RULES
from report import generate_report

def analyze_file(filename):
    findings = []

    with open(filename, 'r') as file:
        lines = file.readlines()

    for line_num, line in enumerate(lines, start=1):
        for rule in RULES:
            if rule["pattern"] in line:
                findings.append({
                    "line": line_num,
                    "code": line.strip(),
                    "rule": rule
                })

    return findings

if __name__ == "__main__":
    filename = "test.c"
    findings = analyze_file(filename)
    generate_report(findings)
