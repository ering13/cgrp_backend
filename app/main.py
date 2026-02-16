# -*- coding: utf-8 -*-

from fastapi import FastAPI

import backend.app.models

from backend.app.api.routes import router

app = FastAPI(
    title="CGRP App Backend",
    version="0.1.0",
)

# Register API routes
app.include_router(router)


@app.get("/")
def health_check():
    return {"status": "ok"}
