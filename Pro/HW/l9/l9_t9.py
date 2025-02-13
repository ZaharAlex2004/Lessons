import re
from collections import defaultdict


def analysing_data(data: str) -> None:
    ip_count = defaultdict(int)

    with open(data, 'r') as log_file:
        for line in log_file:
            match = re.match(r'(\d+\.\d+\.\d+\.\d+)', line)
            if match:
                ip = match.group(1)
                ip_count[ip] += 1

    for ip, count in ip_count.items():
        print(f'IP {ip} maked {count} counts.')


lgf = 'access.log'
analysing_data(lgf)
