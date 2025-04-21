#!/bin/bash

# Output file
OUTPUT_FILE="project_structure_and_content.txt"

# Clear output file if it exists
> "$OUTPUT_FILE"

# Step 1: Dump directory tree
echo "[+] Writing directory tree..."
echo "== FILE TREE ==" >> "$OUTPUT_FILE"
tree -a >> "$OUTPUT_FILE" 2>/dev/null

# Step 2: Dump contents of each file
echo -e "\n\n== FILE CONTENTS ==" >> "$OUTPUT_FILE"

# Traverse all files, skipping the output file itself
while IFS= read -r -d '' file
do
    if [[ "$file" != "$OUTPUT_FILE" ]]; then
        echo -e "\n\n--- FILE: $file ---" >> "$OUTPUT_FILE"
        if file "$file" | grep -q 'text'; then
            cat "$file" >> "$OUTPUT_FILE"
        else
            echo "[BINARY FILE CONTENT OMITTED]" >> "$OUTPUT_FILE"
        fi
    fi
done < <(find . -type f -print0)

echo "Done! Output written to $OUTPUT_FILE"
