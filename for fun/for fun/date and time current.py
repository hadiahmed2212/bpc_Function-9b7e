from datetime import datetime
import time

while True:
    current_time = datetime.now().replace(microsecond=0)
    print(current_time.strftime("%d/%m/%Y %I:%M:%S %p"), end="\r")
    time.sleep(1)