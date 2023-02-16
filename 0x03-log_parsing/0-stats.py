#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics:

    Input format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code>
    <file size>

    (if the format is not this one, the line must be skipped)
    After every 10 lines and/or a keyboard interruption (CTRL + C),
    print these statistics from the beginning:
        Total file size: File size: <total size>
        where <total size> is the sum of all previous <file size>
        (see input format above)
        Number of lines by status code:
            possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
            if a status code doesn’t appear or is not an integer,
            don’t print anything for this status code
            format: <status code>: <number>
            status codes should be printed in ascending order
"""
import sys


def log_parsing():
    """gets infomation from logs"""
    codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    status_count = {status: 0 for status in codes}
    file_size = 0
    count = 0
    status = None
    try:
        for line in sys.stdin:
            line = line.split()
            if len(line) > 4:
                status = line[-2]
                size = line[-1]
            if status in status_count.keys():
                status_count[status] += 1
            file_size += int(size)
            count += 1
            if count == 10:
                count = 0
                print("File size: {}".format(file_size))
                for key, val in status_count.items():
                    if val != 0:
                        print("{}: {}".format(key, val))
    except KeyboardInterrupt:
        pass
    finally:
        print("File size: {}".format(file_size))
        for key, val in status_count.items():
            if val != 0:
                print("{}: {}".format(key, val))


if __name__ == "__main__":
    log_parsing()
