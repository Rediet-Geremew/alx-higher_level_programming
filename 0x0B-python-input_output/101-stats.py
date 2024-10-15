#!/usr/bin/python3
import sys

def print_statistics(total_size, status_codes):
    """Print the accumulated statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def main():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 7:
                continue  # Skip lines that do not have enough parts

            # Get status code and file size
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            # Update total size and status codes
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1

            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)

if __name__ == "__main__":
    main()
