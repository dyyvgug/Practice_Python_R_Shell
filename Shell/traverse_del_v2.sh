#!/bin/bash

# Function to display help/usage information
function display_help() {
cat << EOF
Usage: traverse_del.sh [-h | --help] <directory> <filename>

Options:
  -h, --help   Show this help message and exit.

Example:
  traverse_del.sh ./ *.txt 
EOF
}

# Process command-line options
while [[ $# -gt 0 ]]; do
case "$1" in
  -h|--help)
    display_help
    exit 0
    ;;
  *)
    # Check if we have enough arguments (directory and filename)
    if [[ $# < 2 ]]; then 
        echo "Error: Missing directory or filename argument."
        display_help
        exit 1
    fi

    # Assign arguments to variables for clarity
    directory=$1
    filename=$2
    shift 2  # Shift parameters to process the next set
    ;;
esac
done

# Validate input directory
if [ ! -d "$directory" ]; then
  echo "Error: Directory '$directory' does not exist."
  exit 1
fi

# Traverse and delete files with the specific suffix
function traverse_and_delete() {
  local workdir="$1"
  local pattern="$2"

  find "$workdir" -type f -name "*$pattern" -exec echo "Deleting {}" \; -exec rm -f {} \;
}

# Start traversal and deletion
traverse_and_delete "$directory" "$filename"

