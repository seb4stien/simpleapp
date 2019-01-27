from datetime import datetime
import socket
import time

while True:
    print("[{}] Running on {}".format(
          datetime.now().strftime("%H:%M:%S"),
          socket.gethostname()))
    time.sleep(10)
