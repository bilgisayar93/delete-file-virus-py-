import os
import subprocess
from unittest import result
os.chdir("E:")
result= subprocess.check_output("dir /S /B *.html", shell=True).decode().split()
for i in result:
    os.remove(i)
    print("deleted : "+i)