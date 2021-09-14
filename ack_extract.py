"""
Simple script to extract acronyms from text and MS Word documents
"""

import argparse
import re
import textract
from os.path import exists

def extract_acronyms(txt_str):
    """
    Extract acronyms from supplied text
    :param txt_str: input text (str)
    :return: List of acronyms
    """

    ack_list = re.findall(r"\b[A-Z\.]{2,}s?\b", txt_str)

    return ack_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='ack_extract',
                                     usage='%(prog)s input-file output-file',
                                     description='Extract Acronyms From a Document')
    parser.add_argument('--in_file', type=str, required=True)
    parser.add_argument('--out_file', type=str, required=False)
    args = parser.parse_args()

    if exists(args.in_file):

        sample_text = textract.process(args.in_file)

        # Convert from binary string to string
        sample_text = sample_text.decode("utf8")

        acronym_list = extract_acronyms(sample_text)

        # Remove duplicates from the list
        out_list = list(dict.fromkeys(acronym_list))

        # Sort the list entries
        out_list.sort()

        # set up the output file name
        if not args.out_file:
            file_parts = args.in_file.split('.')
            out_file_name = file_parts[0] + '_acronyms.txt'
        else:
            out_file_name = args.out_file

        # Output acronym list to a text file
        with open(out_file_name, "w") as outfile:
            for acro in out_list:
                outfile.write(acro + "\n")

        print(f'Acronyms Extracted: {len(out_list)}')
        print(f'Output File: {out_file_name}')
    else:
        print(f'Error: Unable to find input file: {args.in_file}')

