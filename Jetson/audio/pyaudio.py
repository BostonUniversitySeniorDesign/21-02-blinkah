import subprocess
import time

a = subprocess.Popen(['cvlc', 'bos_sample.mp3'])
time.sleep(3)
b = subprocess.Popen(['cvlc', 'bos_sample.mp3'])
time.sleep(3)
a.kill()
b.kill()
