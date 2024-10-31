import os
import subprocess

input_file_path = '/home/daniel/Git/LLM-and-AI/testmddocs/chatgpt-raw/testoutput.md'
output_dir = '/home/daniel/Git/LLM-and-AI/testmddocs/variants'

pandoc_formats = [
    "commonmark",
    "markdown_strict",
    "markdown_phpextra",
    "markdown_mmd",
    "markdown_github",
    "markdown_auto_identifiers",
    "markdown",
    "markdown+smart",
    "markdown-implicit_figures",
    "markdown_simple_tables",
    "markdown_grid_tables",
    "markdown_pipe_tables",
    "markdown_strict+yaml_metadata_block"
]

file_name, file_ext = os.path.splitext(os.path.basename(input_file_path))
os.makedirs(output_dir, exist_ok=True)

for format in pandoc_formats:
    output_file_path = os.path.join(output_dir, f"{file_name}_{format}.md")
    subprocess.run(["pandoc", input_file_path, "-f", "markdown", "-t", format, "-o", output_file_path])
    print(f"Converted to {format} format saved as {output_file_path}")

print("All conversions complete.")
