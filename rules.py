RULES = [
    {
        "name": "Unsafe Function - gets",
        "pattern": "gets(",
        "cwe": "CWE-242",
        "severity": "High",
        "description": "gets() is unsafe and can cause buffer overflow."
    },
    {
        "name": "Unsafe Function - strcpy",
        "pattern": "strcpy(",
        "cwe": "CWE-120",
        "severity": "High",
        "description": "strcpy() does not check buffer size."
    },
    {
        "name": "Unsafe Function - scanf",
        "pattern": "scanf(",
        "cwe": "CWE-20",
        "severity": "Medium",
        "description": "scanf() is unsafe without checking bounds."
    }
]
