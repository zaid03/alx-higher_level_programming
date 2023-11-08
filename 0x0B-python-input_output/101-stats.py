#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""

import sys


def compute_metrics():
    """
    Read data from stdin, compute and print metrics.

    Metrics include:
    - Total file size
    - Number of lines by status code (sorted in ascending order)

    Input format expected: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

    The script continues reading from stdin and computes metrics every 10 lines or upon a keyboard interruption (CTRL + C).

    This script does not handle file permission or file not existing exceptions.
    """
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            data = line.split()
            if len(data) > 6:
                file_size = int(data[-1])
                status_code = data[-2]

                total_size += file_size

                if status_code in status_codes:
                    status_codes[status_code] += 1

            if line_count % 10 == 0:
                print("File size: {}".format(total_size))
                for code, count in sorted(status_codes.items()):
                    if count > 0:
                        print("{}: {}".format(code, count))
    except KeyboardInterrupt:
        pass
    finally:
        print("File size: {}".format(total_size))
        for code, count in sorted(status_codes.items()):
            if count > 0:
                print("{}: {}".format(code, count))

if __name__ == "__main__":
    compute_metrics()
