import time, datetime, json, os
import subprocess
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from utils.logger_settings import api_logger
from utils.util import Util

processId = str(int(time.time()))
OUTPUT_DIR="out/"
os.makedirs(OUTPUT_DIR, exist_ok=True)


targetPath = "resource/target-240p.mp4"
srcPath = "resource/source.jpg"
outPath = f"{OUTPUT_DIR}{processId}.{os.path.splitext(targetPath)}"


pythonPath = f"venv/bin/python"
cmd = f"{pythonPath} run.py \
--frame-processors face_swapper,face_enhancer \
--frame-enhancer-model real_esrgan_x4 \
--execution-device-id 0 \
--source {srcPath} \
--target {targetPath} \
--output {outPath} \
--headless"
api_logger.info(cmd)

result = subprocess.check_output(cmd, shell=True)
Util.log_subprocess_output(result)

if os.path.exists(outPath):
    api_logger.info(
        f"上传合成后的图片到OSS，OUTPUT_PATH: {outPath}, processId: {processId}"
    )
    from task import taskBase

    uploadResult = taskBase.uploadFileToTos(
        outPath, processId, videoTypeStr=taskBase.VideoTaskType.Roop.value
    )
# print(run)
