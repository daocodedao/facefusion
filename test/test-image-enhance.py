import time, datetime, json, os
import subprocess
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from utils.logger_settings import api_logger


processId = str(int(time.time()))
OUTPUT_DIR="out/"
os.makedirs(OUTPUT_DIR, exist_ok=True)
dstImage = f"{OUTPUT_DIR}{processId}.jpg"

frameEnchanceModel = "frame_enhancer"
srcImage = "resource/851724224941.jpg"
# commands = [
#     sys.executable,
#     "run.py",
#     "--frame-processors",
#     "frame_enhancer",
#     "--frame-enhancer-model",
#     "real_esrgan_x4",
#     "-t",
#     f"{srcImage}",
#     "-o",
#     f"{dstImage}",
#     "--headless",
# ]
# run = subprocess.run(commands, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# if run.returncode == 0:

cmd =f"sys.executable run.py
--frame-processors frame_enhancer \
--frame-enhancer-model real_esrgan_x4 \
--target {srcImage} \
--output {dstImage} \
--headless"
print(cmd)

result = subprocess.check_output(cmd, shell=True)


if result.returncode == 0:
    api_logger.info(
        f"上传合成后的图片到OSS，OUTPUT_PATH: {dstImage}, processId: {processId}"
    )
    from task import taskBase

    uploadResult = taskBase.uploadFileToTos(
        dstImage, processId, videoTypeStr=taskBase.VideoTaskType.Roop.value
    )
print(run)
