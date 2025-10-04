import os
import yaml
import logging.config
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from src.api.routes import router as api_router



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(BASE_DIR, "config", "settings.yaml")
LOG_CONF = os.path.join(BASE_DIR, "config", "logging.conf")


if os.path.exists(LOG_CONF):
    logging.config.fileConfig(LOG_CONF)
logger = logging.getLogger(__name__)

