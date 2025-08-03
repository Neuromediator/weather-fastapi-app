# 🌦️ FastAPI Weather Forecast App

A simple web application built with **FastAPI** that displays the **current weather** and a **3-day forecast** for a selected city using [WeatherAPI](https://www.weatherapi.com/).



## 🚀 Features

* 🌐 Web interface built with HTML + CSS
* 📩 Form input to submit a city name
* ⛅ Fetches current weather + 3-day forecast
* 🔁 FastAPI with async routes
* 🛠️ Ready to deploy or extend

## 🏗️ Project Structure

```
Projects1/
├── src/
│   ├── api.py               # Main FastAPI application
│   ├── weather_api.py       # WeatherAPI integration
├── templates/
│   ├── form.html            # Input form page
│   ├── weather_result.html  # Results page
├── static/
│   ├── style.css            # Basic CSS styling
├── .env                     # API key and config (not included in repo)
├── run_server.bat          # Windows launcher script
├── requirements.txt         # Python dependencies
└── README.md               # You're here!
```

## 🔧 Requirements

* Python 3.10 or 3.11
* `pip install -r requirements.txt`
* `.env` file with your WeatherAPI key:

  ```
  WEATHER_API_KEY=your_api_key_here
  ```

## ▶️ Running the Project

### Option 1: From terminal (recommended)

```bash
uvicorn src.api:app --reload
```

### Option 2: Use the `.bat` script (Windows only)

```bash
./run_server.bat
```

### Visit:

* [http://127.0.0.1:8000/](http://127.0.0.1:8000/) — Home
* [http://127.0.0.1:8000/form](http://127.0.0.1:8000/form) — City input form
* [http://127.0.0.1:8000/weather?city=Tallinn](http://127.0.0.1:8000/weather?city=Tallinn) — Sample output

## 🌍 Deployment

You can deploy this app using:

* [Render](https://render.com/)
* [Vercel + FastAPI adapter](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker)
* Docker (`uvicorn` + `gunicorn`)
* Or host it on your own VPS

## 📦 Installation for Production

```bash
python -m venv venv
venv\Scripts\activate         # or source venv/bin/activate (Linux/Mac)
pip install -r requirements.txt
uvicorn src.api:app
```

## ✅ To Do

* [ ] Add error handling (invalid city, API errors)
* [ ] Add loading animation or spinner
* [ ] Add mobile responsiveness
* [ ] Internationalization (language switch)

## 📝 License

MIT License. Feel free to use and modify.

---

Made with ❤️ using [FastAPI](https://fastapi.tiangolo.com/)
