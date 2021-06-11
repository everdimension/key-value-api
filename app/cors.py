import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

def add_middleware(app: FastAPI):
    origins = [
        "http://localhost",
        "http://localhost:3000",
        "https://localhost:3000",
    ]

    additional_origins = os.environ.get("CORS_ALLOW_ORIGINS")
    if additional_origins:
        for origin in additional_origins.split(','):
            origins.append(origin)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

