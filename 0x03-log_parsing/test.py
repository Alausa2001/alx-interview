#!/usr/bin/python3
import sys
import re


def log_parsing():
    """gets infomation from logs"""
    codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    status_count = {status: 0 for status in codes} 
    file_size = []
    count = 0
    status = None
    try:
        for line in sys.stdin:
            count += 1
            search = re.search('GET .* (.*) (.*)', line)
            status = search.group(1)
            if status in status_count.keys():
                status_count[status] += 1
                file_size.append(int(search.group(2)))
            if count == 10:
                count = 0
                print("File_size: {}".format(sum(file_size)))
                for key, val in status_count.items():
                    if val != 0:
                        print("{}: {}".format(key, val))
    except KeyboardInterrupt:
        print("File_size: {}".format(sum(file_size)))
        for key, val in status_count.items():
            if val != 0:
                print("{}: {}".format(key, val))


if __name__ == "__main__":
    log_parsing()
