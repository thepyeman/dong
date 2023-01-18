import datetime
import subprocess
import time
import urllib.request

prev_min = datetime.datetime.now().minute

while True:
    current_time = datetime.datetime.now()
    current_min = current_time.minute

    if current_min != prev_min:
        # Download the mp3 file from a URL
        mp3_url = "https://github.com/muolbarry/dong/raw/main/dong.mp3"
        mp3_file = "dong.mp3"
        urllib.request.urlretrieve(mp3_url, mp3_file)
        subprocess.run(["afplay", mp3_file])
        prev_min = current_min
    else:
        current_sec = current_time.second
        sec_left = 60 - current_sec
        print(f"Time until next dong: {sec_left} seconds")
    time.sleep(1)
