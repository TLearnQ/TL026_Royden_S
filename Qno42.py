import json
import yaml

def clean(path):
    try:
        with open(path, "r") as file:
            data = json.load(file)

        cleaned = {}
        for k, v in data.items():
            key = k.lower()
            if isinstance(v, dict):
                sub = {}
                for a, b in v.items():
                    sub[a.lower()] = b
                cleaned[key] = sub
            else:
                cleaned[key] = v
        with open("output1.json", "w") as f:
            json.dump(cleaned, f, indent=4)
        return cleaned
    except Exception as e:
        print("Error while processing file:", e)

print(clean(r"C:\Users\ROYDEN\OneDrive\Desktop\phytelco\PythonAssessment\test.json"))