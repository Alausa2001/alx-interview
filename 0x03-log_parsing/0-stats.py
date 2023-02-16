#!/usr/bin/python3
"""
Log parsing
"""

import sys

if __name__ == '__main__':

    filesize, count = 0, 0
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    status_count = {status: 0 for status in status_codes}

    def print_stats(stats, file_size):
        print("File size: {:d}".format(filesize))
        for key, val in sorted(stats.items()):
            if val != 0:
                print("{}: {}".format(key, val))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in status_codes:
                    status_count[status_code] += 1
            except BaseException:
                pass
            try:
                filesize += int(data[-1])
            except BaseException:
                pass
            if count == 10:
                count = 0
                print_stats(status_count, filesize)
        print_stats(status_count, filesize)
    except KeyboardInterrupt:
        print_stats(status_count, filesize)
        raise
