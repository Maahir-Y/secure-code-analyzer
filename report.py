def generate_report(findings):
    if not findings:
        print("No vulnerabilites.")
        return
        
    print("Security Report:\n")
    
    for f in findings:
        rule = f["rule"]
        print(f"[Line {f['line']}] {rule['name']}")
        print(f"Code: {f['code']}")
        print(f"CWE: {rule['cwe']}")
        print(f"Severity: {rule['severity']}")
        print(f"Description: {rule['description']}")
        print("-" * 40)

def suggest_threats(findings):
    print("Threat Modeling Insights:\n")

    for f in findings:
        if f["rule"]["severity"] == "High":
            print(f"Potential Attack: Buffer Overflow at line {f['line']}")
