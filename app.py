from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, HTMLResponse
import shutil
import os

from calendar_gen import generate_calendar

app = FastAPI()

DATA_DIR = "data"
ICS_PATH = os.path.join(DATA_DIR, "calendar.ics")
UPLOAD_PATH = os.path.join(DATA_DIR, "schedule.png")

os.makedirs(DATA_DIR, exist_ok=True)


@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <h2>Work calendar</h2>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file" accept="image/*">
        <button type="submit">Загрузить план</button>
    </form>
    <p><a href="/calendar.ics">Ссылка на календарь</a></p>
    """


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    with open(UPLOAD_PATH, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # пока заглушка — дальше подключим OCR
    generate_calendar(ICS_PATH)

    return {"status": "ok", "message": "Календарь обновлён"}


@app.get("/calendar.ics")
def calendar():
    return FileResponse(ICS_PATH, media_type="text/calendar")
