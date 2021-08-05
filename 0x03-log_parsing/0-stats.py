#!/usr/bin/python3
"""Performs log parsing from stdin"""

import re
import sys
from signal import signal, SIGINT
import traceback
counter = 0
file_size = 0
statusC_counter = {200: 0, 301: 0, 400: 0,
                   401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def printCodes(dict, file_s):
    """Prints the status code and the number of times they appear"""
    print("File size: {}".format(file_s), flush=True)
    for key in sorted(dict.keys()):
        if statusC_counter[key] != 0:
            print("{}: {}".format(key, dict[key]), flush=True)


def handler(signal_received, frame):
    """Handles the ctrl-c signal."""
    print(end="", flush=True)
    printCodes(statusC_counter, file_size)
    exit(0)


for line in sys.stdin:
    counter = counter + 1
    split_string = re.split('- |"|"| " " ', str(line))
    statusC_and_file_s = split_string[-1]
    statusC = int(statusC_and_file_s.split()[0])
    f_size = int(statusC_and_file_s.split()[1])
    if statusC in statusC_counter:
        statusC_counter[statusC] = statusC_counter[statusC] + 1
        file_size = file_size + f_size
    if counter % 10 == 0:
        printCodes(statusC_counter, file_size)
    signal(SIGINT, handler)
