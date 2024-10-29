#!/usr/bin/python3
"""A script that reads standard input line by line and computes metrics
"""
import sys
import collections
import re
STATUS_CODES = ["200", "301", "400", "401", "403", "404", "405", "500"]


def print_metric(metric):
    for status_code in STATUS_CODES:
        count = metric.get(status_code)
        if count is not None:
            print("{}: {}".format(status_code, metric[status_code]))


def main():
    while True:
        count = 0
        metric = collections.Counter()
        total_size = 0

        try:
            for line in sys.stdin:
                if count == 10:
                    print("File size: {}".format(total_size))
                    print_metric(metric)
                    metric = collections.Counter()
                    total_size = 0
                (status_code, file_size) = parse(line)
                total_size += file_size
                metric.update([status_code])
                count += 1
            break
        except KeyboardInterrupt:
            print("File size: {}".format(total_size))
            print_metric(metric)
            metric = collections.Counter()
            total_size = 0
            continue


def parse(line: str) -> tuple[str, int]:
    ip = r"\.".join([r"\d{1,2}[0-5]?"] * 4)
    date = r""
    ...


if __name__ == "__main__":
    main()
