#!/usr/bin/python3

import sys

def compute_metrics():
    """
    Computes metrics based on the input format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

    Prints the statistics for each 10 lines and after a keyboard interruption (CTRL + C):
    Total file size: File size: <total size>
    Number of lines by status code:
    <status code>: <number>
    status codes are printed in ascending order

    Returns:
    None
    """
    log_lines = 0
    total_size = 0
    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }
    try:
        for line in sys.stdin:
            log_lines += 1
            line = line.split()
            total_size += int(line[-1])
            status_codes[line[-2]] += 1
            if log_lines % 10 == 0:
                print("Total file size: File size: {}".format(total_size))
                for code in sorted(status_codes.keys()):
                    if status_codes[code] != 0:
                        print("{}: {}".format(code, status_codes[code]))
    except KeyboardInterrupt:
        print("Total file size: File size: {}".format(total_size))
        for code in sorted(status_codes.keys()):
            if status_codes[code] != 0:
                print("{}: {}".format(code, status_codes[code]))

if __name__ == '__main__':
    compute_metrics()

