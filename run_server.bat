@echo off
call .venv\Scripts\activate
uvicorn src.api:app --reload