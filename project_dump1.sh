#!/bin/bash

# Output file
OUTPUT_FILE="project_structure_and_content1.txt"

# Create or clear the output file
> "$OUTPUT_FILE"

# Print the .py tree structure into the file
echo "Generating Python file tree structure..."
find . -type f -name "*.py" | sort | awk '{
    split($0, parts, "/");
    indent = length(parts) - 1;
    line = "";
    for (i = 1; i < length(parts); i++) {
        line = line "│   ";
    }
    line = line "├── " parts[length(parts)];
    print line;
}' >> "$OUTPUT_FILE"

echo -e "\n" >> "$OUTPUT_FILE"

# Append the contents of each .py file
echo "Appending contents of .py files..."
find . -type f -name "*.py" | sort | while read file; do
    echo "================================================================================" >> "$OUTPUT_FILE"
    echo "File: $file" >> "$OUTPUT_FILE"
    echo "================================================================================" >> "$OUTPUT_FILE"
    cat "$file" >> "$OUTPUT_FILE"
    echo -e "\n\n" >> "$OUTPUT_FILE"
done

echo "Done. Output written to $OUTPUT_FILE"

