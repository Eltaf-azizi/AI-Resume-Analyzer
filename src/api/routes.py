
import os
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from fastapi import Request
from ..services.resume_analyzer import ResumeAnalyzerService
from ..api.schemas import AnalyzeResponse
from ..utils.file_utils import save_upload_file

router = APIRouter()



def get_service(request: Request):
    settings = request.app.state.settings
    return ResumeAnalyzerService(settings)


