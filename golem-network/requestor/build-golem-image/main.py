import argparse
from pathlib import Path

DEFAULT_FILEPATH = "input.txt"

parser = argparse.ArgumentParser(description='Process a file path.')
parser.add_argument(
    "file_path",
    nargs="?",
    default=DEFAULT_FILEPATH,  # Set your default file path here
    help=f"Path to the input file (default: {DEFAULT_FILEPATH})"
)
args = parser.parse_args()

input_file_name = str(args.file_path)

print(f"The file path used is: {input_file_name}")

output_string = "Hello, "

input_file_path = Path(input_file_name)

if input_file_path.exists():
    print(f"{input_file_name} exists.")
    contents = input_file_path.read_text()
    if contents == "":
        print(f"{input_file_name} is empty.")
        output_string += "Empty World"
    else:
        output_string += contents
else:
    print(f"{input_file_name} does not exist.")
    output_string += "World"

print(output_string)