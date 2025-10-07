
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


@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_resume(file: UploadFile = File(...), service: ResumeAnalyzerService = Depends(get_service)):
    
    # save to a temp location
    tmp_path = save_upload_file(file)

    try:
        result = service.analyze(tmp_path)
        return result
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        # best-effort cleanup

        try:
            os.remove(tmp_path)
            
        except Exception:
            pass
