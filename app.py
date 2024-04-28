#!/usr/bin/env python3

import os
from contextlib import asynccontextmanager
from collections import defaultdict
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import argparse
from config.settings import (HOST, 
                             PORT)
from utils.helper import download_model
from routers.detect import detection_router
from routers.fine_tune import finetune_router


@asynccontextmanager
async def lifespan(application: FastAPI):
    # TODO: implement init model for application lifecycle
    ...


description = """
CountAnyObject API powered by YOLO-worldv2. 🚀
"""

app = FastAPI(
    title="CountAnyObject API",
    description=description,
    version="0.0.1",
    lifespan=lifespan
)

# CORSMiddleware for allowing different origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend origin
    allow_methods=["*"],  # Allow all methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allow all headers for flexibility
)

#  register routers here
app.include_router(detection_router)
app.include_router(finetune_router)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--host",
        help="Host to run the API on",
    )
    parser.add_argument(
        "--port",
        help="Port to run the API on",
    )
    parser.add_argument(
        "--reload",
        action="store_true",
        default=False,
        help="Reload server on code change",
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    if not args.host:
        args.host = HOST
    if not args.port:
        args.port = PORT
    args.port = int(args.port)
    uvicorn.run("app:app", host=args.host, port=args.port, reload=args.reload)
