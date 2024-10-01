import os

def list_files_and_folders(directory, output_file):
    indent = '    '  # Define the indentation level for sub-items
    pipe = '|'
    branch = '|___ '  # Branch symbols for directories
    last_branch = '|___ '  # Last branch symbol for the last item in a directory
    with open(output_file, 'w') as f:
        f.write(f"Project Tree Overview\n{directory.split('/')[-1]}\n")  # Project name as root
        for root, dirs, files in os.walk(directory):
            # Ignore .git and __pycache__ folders
            dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__']]
            level = root.replace(directory, '').count(os.sep)  # Determine the current level
            indent_level = pipe + indent * level  # Apply indentation based on level
            subindent = pipe + indent * (level + 1)

            f.write(f"{indent_level}{branch if dirs or files else last_branch}{os.path.basename(root)}\n")  # Print directory name
            all_items = sorted(dirs) + sorted(files)  # Combine and sort directories and files
            for index, item in enumerate(all_items):
                is_last = index == len(all_items) - 1  # Check if it's the last item
                prefix = last_branch if is_last else branch
                if item in dirs:
                    f.write(f"{subindent}{prefix}{item}\n")  # Print sub-directory
                else:
                    f.write(f"{subindent}{prefix}{item}\n")  # Print file

# Update the directory path to your project folder
project_directory = "D:/HARRISBURG/Harrisburg Master's Fifth Term Late Summer/CISC 699/DiscordBotProject_CISC699"
output_file = os.path.join(project_directory, "other/project_structure.txt")

# Call the function to list files and save output to .txt
list_files_and_folders(project_directory, output_file)

print(f"File structure saved to {output_file}")
