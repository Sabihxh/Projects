import subprocess
from datetime import datetime, timedelta
import time
audio_file = "mpthreetest.mp3"

delay_minutes = int(raw_input("After how many minutes from now do you want to activate the alarm? "))
start_time = datetime.now()
alarm_time = start_time + timedelta(seconds = delay_minutes)
print alarm_time
while datetime.now() < alarm_time:
    time.sleep(5)
    print datetime.now().strftime('%H:%M:%S')
else:
    return_code = subprocess.call(["afplay", audio_file])
