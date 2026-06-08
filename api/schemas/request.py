# api/schemas/request.py

from pydantic import BaseModel


class PassengerRequest(BaseModel):
    Pclass: int
    Name: str
    Sex: str
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Embarked: str




'''
این فایل چه کاری انجام می‌دهد؟
قبلاً ورودی به شکل: دیشنری بود مثلا 
{
    "Pclass": 3,
    "Sex": "male",
    ...
}

اما FastAPI باید اعتبارسنجی کند.
اگر کاربر بنویسد:
{
    "Age": "abc"
}
باید خطا بدهد.
این مسئولیت Schema است.

'''