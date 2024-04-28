import http
import os
from typing import List, Union
from fastapi import APIRouter, Depends, status, UploadFile
from collections import defaultdict
from logger import logger
from routers.context_manager import (build_request_context,
                                     context_api_id,
                                     context_log_meta)
from schema.base import GenericResponseModel

detection_router = APIRouter(prefix="/detect-from-txt")


@detection_router.post("", status_code=status.HTTP_200_OK,
                         response_model=GenericResponseModel)
async def detect_from_txt(img: UploadFile, classes: List[str]):
    """
    Detect and count objects of classes in the uploaded image.
    :param img: Uploaded image
    :param classes: List of classes
    :return: GenericResponseModel
    """
    # TODO: implement functionalities
    ...
