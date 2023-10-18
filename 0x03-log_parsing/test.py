import sys
import time


status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
while True:
    try:
        print('x')
        time.sleep(2)
    except KeyboardInterrupt:
        print(4)