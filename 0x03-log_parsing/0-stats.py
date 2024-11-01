#!/usr/bin/python3
"""A script that reads standard input line by line and computes metrics
"""
import sys
import collections
import re

STATUS_CODES = ["200", "301", "400", "401", "403", "404", "405", "500"]


def print_metric(metric):
    """prints the metric of stats gottent from the log file
    """
    for status_code in STATUS_CODES:
        frequency = metric.get(status_code)
        if frequency is not None:
            print("{}: {}".format(status_code, metric[status_code]))


def main():
    """Main driver of the program
    """
    while True:
        num_lines = 0
        metric = collections.Counter()
        total_size = 0

        try:
            for line in sys.stdin:
                if num_lines == 10:
                    print("File size: {}".format(total_size))
                    print_metric(metric)
                    metric = collections.Counter()
                    total_size = 0
                    num_lines = 0
                (status_code, file_size) = parse(line.rstrip())
                if status_code is not None:
                    total_size += file_size
                    metric.update([status_code])
                num_lines += 1
            break
        except KeyboardInterrupt:
            print("File size: {}".format(total_size))
            print_metric(metric)


def parse(line):
    """Parses each line of the log file
    """
    ip = r"[.]".join([r"(1?\d{1,2}|2[0-4]\d|25[0-5])"] * 4)
    date = r"\d{4}-(0\d|1[0-2])-([0-2]\d|3[01])"
    time = r"([0-1]\d|2[0-3]):(0\d|[1-5]\d):(0\d|[1-5]\d)[.]\d{6}"
    datetime = rf"\[{date} {time}\]"
    request = r'"GET /projects/260 HTTP/1.1"'
    status_code = r"(?P<method>" + r"|".join(STATUS_CODES) + r")"
    filesize = r"(?P<filesize>\d+)"
    pattern = " ".join([ip, "-", datetime, request, status_code, filesize])
    match = re.match(rf"^{pattern}$", line)
    try:
        return match.group("method"), int(match.group("filesize"))
    except (AttributeError, IndexError):
        return None, None


if __name__ == "__main__":
    main()
