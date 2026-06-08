# api/routes/health.py

from fastapi import APIRouter

router = APIRouter(prefix="/health",tags=["Health"])

@router.get("")
def health_check():

    return {"status": "healthy"}











'''
Health Check
این Endpoint برای Kubernetes و Docker بسیار مهم است.

Health Endpoint
چرا لازم است؟
الان API فقط پیش‌بینی انجام می‌دهد.
اما سرویس‌های Production معمولاً قبل از ارسال ترافیک بررسی می‌کنند:

آیا سرویس زنده است؟
آیا سرویس پاسخ می‌دهد؟
آیا سرویس Crash نکرده؟

برای همین Endpoint سلامت ایجاد می‌شود.
------------------------------------
{
  "status": "healthy"
}
اما بعداً همین Endpoint می‌تواند بررسی کند:
Model Loaded ?
Database Connected ?
MLflow Reachable ?
Redis Reachable ?
'''