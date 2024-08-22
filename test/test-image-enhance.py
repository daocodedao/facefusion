import time,datetime,json,os
import subprocess

# import 路径修改
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


processId = int(time.time())
srcImage="resource/851724224941.jpg"
dstImage=f"out/{processId}.jpg"


commands = [ sys.executable, 
            'run.py', 
            '--frame-processors', 
            'frame_enhancer', 
            '-t', 
            f'{srcImage}', 
            '-o', 
            f'{dstImage}', 
            '--headless' ]

run = subprocess.run(commands, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)

print(run)
