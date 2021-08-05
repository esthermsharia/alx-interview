#!/usr/bin/python3
"""Performs log parsing from stdin"""

import re
import sys
counter = 1
file_size = 0
statusC_counter = {200: 0, 301: 0, 400: 0,
                   401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def printCodes(dict, file_s):
    """Prints the status code and the number of times they appear"""
    print("File size: {}".format(file_s), flush=True)
    for key in sorted(dict.keys()):
        if statusC_counter[key] != 0:
            print("{}: {}".format(key, dict[key]), flush=True)

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            split_string = re.split('- |"|"| " " ', str(line))
            statusC_and_file_s = split_string[-1]
            statusC = int(statusC_and_file_s.split()[0])
            f_size = int(statusC_and_file_s.split()[1])
            # print("Status Code {} size {}".format(statusC, f_size))
            if statusC in statusC_counter:
                statusC_counter[statusC] = statusC_counter[statusC] + 1
                file_size = file_size + f_size
            if counter != 0 and counter % 10 == 0:
                printCodes(statusC_counter, file_size)
            counter = counter + 1
    except KeyboardInterrupt:
        printCodes(statusC_counter, file_size)
        raise
