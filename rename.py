import re
import os

def remove_question_marks_and_numbers(file_path):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove question marks and numbers from each line
    updated_lines = []
    for line in lines:
        line = line.strip()  # Remove leading and trailing whitespace
        line = re.sub(r'^\? ', '', line)  # Remove question mark and following space at the beginning of the line
        tag = re.sub(r'\b\d+(\.\d+)?\w?\b', '', line).strip()  # Remove numbers after the tag
        updated_lines.append(tag + '\n')

    # Write the modified contents back to the file
    with open(file_path, 'w') as file:
        file.writelines(updated_lines)

# Get the current directory
current_directory = os.getcwd()

# Construct the file path relative to the current directory
file_name = 'tags.txt'
file_path = os.path.join(current_directory, file_name)

# Call the function to remove question marks and numbers
remove_question_marks_and_numbers(file_path)
