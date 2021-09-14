# ack_extract - simple script to extract acronyms from a MS Word or text document

## Usage:

`pip install -r requirements.txt`

`python3 ack_extract.py --in_file <input_file_name> (optional) --out_file <output_file_name>`

The script takes a required input parameter (--in_file) and an optional output parameter (--out_file). If the outfile is not specified, a default output file name will be created based on the input file name.

Output consists of a text file with all extracted acronyms, one per line, sorted alphabetically.

This script will extract acronyms two characters or larger. This can be adjusted in the script if 
you need to set a minimum acronym size. 
