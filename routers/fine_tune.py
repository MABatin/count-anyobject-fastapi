import http
import os
from typing import List, Optional
from fastapi import APIRouter, Depends, status, UploadFile
from collections import defaultdict
from logger import logger
from routers.context_manager import (build_request_context,
                                     context_api_id,
                                     context_log_meta)
from schema.base import GenericResponseModel

finetune_router = APIRouter(prefix="/fine-tune")


@finetune_router.post("", status_code=status.HTTP_200_OK,
                         response_model=GenericResponseModel)
async def detect_from_txt(img: UploadFile, 
                          classes: Optional[List[str]], 
                          bboxes: List[List[int]]):
    """
    Fine-tune YOLO-world model with provided bboxes and (optional)classes.
    :param img: Uploaded image
    :param classes: List of classes (optional)
    :param bboxes: List of bounding boxes
    :return: GenericResponseModel
    """
    # TODO: implement functionalities
    ...
