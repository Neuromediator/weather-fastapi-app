from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.weather_api import get_current_weather, get_forecast

app = FastAPI()

# Set up template rendering
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def root():
    return "<h2>Visit <a href='/form'>/form</a> to use the weather form.</h2>"

@app.get("/form", response_class=HTMLResponse)
def serve_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.get("/weather", response_class=HTMLResponse)
def get_weather(request: Request, city: str):
    current = get_current_weather(city)
    forecast = get_forecast(city)
    return templates.TemplateResponse("weather_result.html", {
        "request": request,
        "city": city,
        "current": current,
        "forecast": forecast
    })

