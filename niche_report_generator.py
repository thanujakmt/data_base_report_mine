
from utility import report_handler
import time

if __name__ == '__main__':
    start_time = time.time()
    report_handler.report_generator()
    end_time = time.time()
    print(end_time - start_time)
    