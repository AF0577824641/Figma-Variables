# Use unique prefix per scaling type — either single-letter or two-letter abbreviation
# Choose abbreviations for clarity and uniqueness
prefix_map = {
    "Linear (Increment 8)": "L",
    "Geometric (x2)": "G",
    "Fibonacci": "F",
    "Modular (1.25x)": "M",
    "Typographic (1.333x)": "T",
    "Whole Numbers (by 10)": "WN",
    "Base-2 (Binary)": "B2",
    "Even Only": "E",
    "Odd Only": "O",
    "Golden Ratio (1.618x)": "GR"
}

# Superscript helper for index
def to_superscript(i):
    superscript_digits = "⁰¹²³⁴⁵⁶⁷⁸⁹"
    return ''.join(superscript_digits[int(d)] for d in str(i))

# Generate updated variable collections using prefixes and superscripts
output_files_prefix_superscript = {}

for scale_name, values in scale_defs.items():
    prefix = prefix_map[scale_name]
    variables = []
    for i, val in enumerate(values):
        superscript = to_superscript(i)
        var_name = f"{prefix}{superscript} ({val}px)"
        variables.append({
            "id": f"VariableID:{prefix}:{i}",
            "name": var_name,
            "description": "",
            "type": "FLOAT",
            "valuesByMode": {
                "26090:0": val
            },
            "resolvedValuesByMode": {
                "26090:0": {
                    "resolvedValue": val,
                    "alias": None
                }
            },
            "scopes": ["ALL_SCOPES"],
            "hiddenFromPublishing": False,
            "codeSyntax": {}
        })

    collection = {
        "id": f"VariableCollectionId:{prefix}:0500",
        "name": f"{scale_name} (Prefix Superscript Naming)",
        "modes": {
            "26090:0": scale_name
        },
        "variableIds": [v["id"] for v in variables],
        "variables": variables
    }

    filename = f"/mnt/data/Figma_{prefix}_PrefixSuperscript.json"
    with open(filename, "w") as f:
        json.dump(collection, f, indent=2)
    output_files_prefix_superscript[scale_name] = filename

output_files_prefix_superscript
