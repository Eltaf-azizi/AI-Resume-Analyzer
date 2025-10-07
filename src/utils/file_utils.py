
import os
import tempfile
from fastapi import UploadFile



def save_upload_file(file: UploadFile) -> str:
    suffix = os.path.splitext(file.filename)[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        content = file.file.read()
        tmp.write(content)
        tmp.flush()

        return tmp.name
