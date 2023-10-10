#!/usr/bin/env python3
"""FastAPI with HTMX"""
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


# Set the app
app = FastAPI()

# Set the templates
templates = Jinja2Templates(directory="templates")

@app.get("/index", response_class=HTMLResponse)
def index(request: Request):
    """Index Function"""
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)





