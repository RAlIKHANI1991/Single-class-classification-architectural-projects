# api/app.py

from fastapi import FastAPI
from api.routes.health import router as health_router
from api.routes.prediction import router as prediction_router
from src.exceptions.handlers import model_not_loaded_handler,prediction_error_handler
from src.exceptions.custom_exceptions import ModelNotLoadedError,PredictionError
from config.settings import settings

from contextlib import asynccontextmanager
from config.logging_config import setup_logger

logger = setup_logger("api")

@asynccontextmanager
async def lifespan(app):
    logger.info("API started")
    yield
    logger.info("API stopped")

app = FastAPI(
    title    = settings.APP_NAME,
    version  = settings.APP_VERSION,
    lifespan = lifespan
)

app.include_router(prediction_router)
app.include_router(health_router)

app.add_exception_handler(ModelNotLoadedError,model_not_loaded_handler)
app.add_exception_handler(PredictionError,prediction_error_handler)