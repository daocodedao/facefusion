import time, datetime, json, os
import subprocess
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from utils.logger_settings import api_logger
from utils.util import Util

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
pythonPath = f"venv/bin/python"
cmd = f"{pythonPath} run.py \
--frame-processors frame_enhancer,face_enhancer \
--frame-enhancer-model real_esrgan_x4 \
--execution-device-id 0 \
--target {srcImage} \
--output {dstImage} \
--headless"
api_logger.info(cmd)

result = subprocess.check_output(cmd, shell=True)
Util.log_subprocess_output(result)

if os.path.exists(dstImage):
    api_logger.info(
        f"上传合成后的图片到OSS，OUTPUT_PATH: {dstImage}, processId: {processId}"
    )
    from task import taskBase

    uploadResult = taskBase.uploadFileToTos(
        dstImage, processId, videoTypeStr=taskBase.VideoTaskType.Roop.value
    )
# print(run)
