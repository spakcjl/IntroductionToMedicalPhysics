import re

file_path = "presentation.Rmd"

with open(file_path, "r") as f:
    lines = f.readlines()

modified_lines = []
for line in lines:
    match = re.match(r"^> Speaker Notes: (.*)$", line)
    if match:
        note_content = match.group(1).strip()
        modified_lines.append("::: notes\n")
        modified_lines.append(note_content + "\n")
        modified_lines.append(":::\n")
    else:
        modified_lines.append(line)

with open(file_path, "w") as f:
    f.writelines(modified_lines)

print("Speaker notes format corrected in presentation.Rmd")