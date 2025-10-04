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


app = FastAPI(title="AI Resume Analyzer")



# load settings
with open(CONFIG_PATH, "r", encoding="utf-8") as fh:
    settings = yaml.safe_load(fh)

app.state.settings = settings

app.include_router(api_router, prefix="/api")



@app.get("/")
def read_root():
    return {"message": "AI Resume Analyzer API. Use /api/analyze to POST a resume."}

# simple CLI convenience (optional)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)
