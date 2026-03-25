import json

# Load facts
with open("fun-facts.json", "r") as f:
    facts = json.load(f)

# Load last index
try:
    with open("fact_index.txt", "r") as f:
        index = int(f.read().strip())
except:
    index = 0

# Get next fact
fact = facts[index]

# Update index
next_index = (index + 1) % len(facts)
with open("fact_index.txt", "w") as f:
    f.write(str(next_index))

# Read README
with open("README.md", "r") as f:
    content = f.read()

start = "<!--START_SECTION:fun-fact-->"
end = "<!--END_SECTION:fun-fact-->"

new_content = content.split(start)[0] + start + "\n" + fact + "\n" + end + content.split(end)[1]

# Write updated README
with open("README.md", "w") as f:
    f.write(new_content)
