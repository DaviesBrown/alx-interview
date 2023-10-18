#!/usr/bin/python3
"""
log parsing
"""
import sys
import re

r_log = r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}) - (\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{6}\]) (\"GET /projects/260 HTTP/1.1\") (\d{3}) (\d{1,4})'
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

file_size = 0
sdict = {}
if __name__ == "__main__":
    try:
        for i, line in enumerate(sys.stdin):
            h = re.findall(r_log, line)
            if h:
                if i % 10 == 0 and i != 0:
                    print(f'file size: {file_size}')
                    j = (dict(sorted(sdict.items())))
                    for k, v in j.items():
                        print(f'{k}: {v}')
                    
                file_size += int(h[0][4])

                if int(h[0][3]) in status_codes:
                    try:
                        sdict[h[0][3]] += 1
                    except:
                        sdict[h[0][3]] = 1
            else:
                continue
    except KeyboardInterrupt:
        print(f'file size: {file_size}')
        j = (dict(sorted(sdict.items())))
        for k, v in j.items():
            print(f'{k}: {v}')
        raise
