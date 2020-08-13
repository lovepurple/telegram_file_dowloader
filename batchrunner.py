import sys
import subprocess
import time

PROCESS_COUNT = 5

if __name__ == "__main__":

    procList = []
    for i in range(PROCESS_COUNT):
        # subprocess.call阻塞 popen不阻塞
        proc = subprocess.Popen([sys.executable, "./downloader.py"])
        procList.append(proc)
        time.sleep(60)

    for proc in procList:
        proc.wait()
