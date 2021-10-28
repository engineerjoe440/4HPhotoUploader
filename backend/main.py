################################################################################
"""
4-H Photo Upload Service
------------------------

(c) 2021 - Stanley Solutions - Joe Stanley

This application serves to provide backend services for a React.js photo upload
system that can be used by volunteers and youth to engage with event photos.
"""
################################################################################

# Requirements
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


# Application Base
app = FastAPI()

# Mount the Static File Path
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# Main Application Response
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "fastapi_token": "Hello World"
        },
    )

# Consent Prompt Loader
@app.get("/api/consenttext")
async def get_consent_text():
    with open('static/consent.txt', 'r') as fObj:
        text = fObj.read().replace('\n', ' ')
    return text

# Main API Endpoint to Capture Image Uploads
@app.post("/api/upload")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}
