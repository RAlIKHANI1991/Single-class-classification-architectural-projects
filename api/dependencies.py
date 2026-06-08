# api/dependencies.py

from services.prediction_service import PredictionService

def get_prediction_service():
    return PredictionService()







'''
چرا Dependency می‌سازیم؟
فعلاً شاید اضافی به نظر برسد.
اما بعداً:
Database
Redis
Monitoring
Cache
Settings
همگی از همین مکان تزریق می‌شوند.
Production Ready بودن از همینجا شروع می‌شود.
'''