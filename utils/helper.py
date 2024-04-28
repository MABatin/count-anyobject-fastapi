import base64
import http
import os.path
import uuid
import requests
import cv2
import numpy as np
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import status
from logger import logger
from routers.context_manager import context_api_id, context_log_meta
from schema.base import GenericResponseModel


def build_api_response(generic_response: GenericResponseModel) -> JSONResponse:
    try:
        if not generic_response.api_id:
            generic_response.api_id = context_api_id.get() if context_api_id.get() else str(uuid.uuid4())
        if not generic_response.status_code:
            generic_response.status_code = status.HTTP_200_OK if not generic_response.error \
                else status.HTTP_422_UNPROCESSABLE_ENTITY
        response_json = jsonable_encoder(generic_response)
        res = JSONResponse(status_code=generic_response.status_code, content=response_json)
        logger.info(extra=context_log_meta.get(), msg="Generated Response with status_code:"+
                    f"{res.status_code} content: {response_json}")
        return res
    except Exception as e:
        logger.error(extra=context_log_meta.get(), msg=f"exception in build_api_response error : {e}")
        return JSONResponse(status_code=generic_response.status_code, content=generic_response.error)


def cv2_from_base64(image_base64):
    image_data = base64.b64decode(image_base64)
    image_array = np.frombuffer(image_data, np.uint8)
    img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    return img


def download_model(url: str, api_key: str, output_file: str):
    """
    Download model file using API key
    :param output_file: output file path
    :param url: download url
    :param api_key: repository api key
    :return: None
    """
    from tqdm import tqdm

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    dir_name = os.path.dirname(os.path.abspath(output_file))
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    with requests.get(url, headers=headers, stream=True) as r:
        r.raise_for_status()
        total = int(r.headers.get("Content-Length"))
        pbar = tqdm(total=total, unit="B", unit_scale=True,
                    unit_divisor=1000,
                    desc=f"Downloading to {output_file}")
        with open(output_file, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
                pbar.update(len(chunk))