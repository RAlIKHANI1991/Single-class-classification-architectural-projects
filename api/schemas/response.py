# api/schemas/response.py

from pydantic import BaseModel

class PredictionResponse(BaseModel):
    prediction: int
    probability: float



'''
چرا این کار را می‌کنیم؟

مزایا:

مزیت                  	توضیح
Validation	        اعتبارسنجی خودکار
Swagger	             مستندسازی خودکار
Type Safety	          کاهش خطا
Production Ready 	استاندارد صنعتی


این فایل چه کاری انجام می‌دهد؟
خروجی API را استاندارد می‌کند.

مثلاً:
{
  "prediction": 1
}
یا:
{
  "prediction": 0
}
'''