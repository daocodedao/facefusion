

import os
from enum import Enum

# import 路径修改
import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from utils.logger_settings import api_logger
# from utils.Tos import TosService
from task.Tos import TosService


class VideoTaskType(Enum):
    """Different separator style."""
    Story = "story"
    Cartoon = "cartoon"
    Roop = "roop"

def uploadFileToTos(uploadFilePath, processId, videoTypeStr=VideoTaskType.Story.value):
    if os.path.exists(uploadFilePath):
        KCDNPlayUrl="http://magicphoto.cdn.yuebanjyapp.com/"
        bucketName = "magicphoto-1315251136"
        resultUrlPre = f"{videoTypeStr}/video/{processId}/"
        # resultUrlPre = f"story/video/{processId}/"
        videoName = os.path.basename(uploadFilePath)
        reusultUrl = f"{resultUrlPre}{videoName}"
        api_logger.info(f"上传文件到OSS，本地文件:{uploadFilePath}, task.key:{reusultUrl}, task.bucketName:{bucketName}")
        TosService.upload_file(uploadFilePath, reusultUrl, bucketName)
        dstUrl = f"{KCDNPlayUrl}{reusultUrl}"
        api_logger.info(f"文件地址= {dstUrl}")
        # notiMsg = notiMsg + f"视频播放地址: {dstUrl}\n"

        return dstUrl
    else:
        return None
