import json
import os

# 1. Load facts safely
json_path = ".github/data/fun_facts.json"
with open(json_path, "r", encoding="utf-8") as f:
    facts = json.load(f)

# 2. Load last index safely
index_path = ".github/data/fact_index.txt"
try:
    with open(index_path, "r", encoding="utf-8") as f:
        index = int(f.read().strip())
except Exception:
    index = 0

# Ensure index doesn't go out of bounds
index = index % len(facts)
fact = facts[index]

# 3. Update index
next_index = (index + 1) % len(facts)
with open(index_path, "w", encoding="utf-8") as f:
    f.write(str(next_index))

# 4. Read and update README
readme_path = "README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

start = "<!--START_SECTION:fun-fact-->"
end = "<!--END_SECTION:fun-fact-->"

# Check if markers exist to prevent silent failures
if start not in content or end not in content:
    raise ValueError(f"Missing HTML comment placeholders '{start}' or '{end}' in README.md")

# Core fix: Corrected the list slicing logic
new_content = content.split(start)[0] + start + "\n" + fact + "\n" + end + content.split(end)[1]

# 5. Write updated README
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Success! Updated README with fact index {index}.")
