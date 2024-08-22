import time, datetime, json, os
import subprocess
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from utils.logger_settings import api_logger


processId = int(time.time())
dstImage = f"out/{processId}.jpg"
srcImage = "resource/851724224941.jpg"
commands = [
    sys.executable,
    "run.py",
    "--frame-processors",
    "frame_enhancer",
    "-t",
    f"{srcImage}",
    "-o",
    f"{dstImage}",
    "--headless",
]

run = subprocess.run(commands, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

if run.returncode == 0:
    api_logger.info(
        f"上传合成后的图片到OSS，OUTPUT_PATH: {dstImage}, processId: {processId}"
    )
    from task import taskBase

    uploadResult = taskBase.uploadFileToTos(
        dstImage, processId, videoTypeStr=taskBase.VideoTaskType.Roop.value
    )
print(run)
