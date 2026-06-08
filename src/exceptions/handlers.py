
# src/exceptions/handlers.py

from fastapi import Request
from fastapi.responses import JSONResponse

async def model_not_loaded_handler(request: Request,exc: Exception):
    return JSONResponse(status_code=500,
                        content={
                                "error": "MODEL_NOT_LOADED",
                                "message": str(exc)
        })


async def prediction_error_handler(request: Request,exc: Exception):
    return JSONResponse(status_code=500,
                        content={
                            "error": "PREDICTION_ERROR",
                            "message": str(exc)
                    })







'''# src/exceptions/handlers.py
# این اسکریپت مشکلی نداشت صرفا امضا هنلدر را عمومی تر  کردیم تا در اپ ای پی آی پای لنس وارنینگ ندهد
from fastapi import Request
from fastapi.responses import JSONResponse
from src.exceptions.custom_exceptions import ModelNotLoadedError,PredictionError


async def model_not_loaded_handler(request: Request,exc: ModelNotLoadedError):

    return JSONResponse(
        status_code=500,
        content={
            "error": "MODEL_NOT_LOADED",
            "message": exc.message
        })


async def prediction_error_handler(request: Request,exc: PredictionError):

    return JSONResponse(
        status_code=500,
        content={
            "error": "PREDICTION_ERROR",
            "message": exc.message
        })'''
