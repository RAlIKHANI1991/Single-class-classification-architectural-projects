# src/models/threshold_optimizer.py

import numpy as np
from sklearn.metrics import f1_score


class ThresholdOptimizer:

    @staticmethod
    def find_best_threshold(model,X_valid,y_valid):

        probabilities = (model.predict_proba(X_valid)[:, 1])
        thresholds = np.arange(0.10, 0.95, 0.01 )

        best_threshold = 0.5
        best_score = 0

        for threshold in thresholds:
            predictions = (probabilities >= threshold).astype(int)
            score = f1_score(y_valid,predictions)

            if score > best_score:
                best_score = score
                best_threshold = (threshold)

        return {
            "threshold":float(best_threshold),
            "score":float(best_score)
        }
    
# این فایل یکی از مهم‌ترین بخش‌های پروژه‌های مالی است.
'''
نکته بسیار مهم
بیشتر افراد این اشتباه را می‌کنند:
prediction = (prob > 0.5)

اما در پروژه‌های واقعی:

Credit Risk
Fraud Detection
Trading Signals
Churn Prediction

تقریباً هیچ‌وقت Threshold برابر 0.5 نیست.
مثلاً:
Best Threshold = 0.37
یا:
Best Threshold = 0.62
---------------------------------------------------------
نکته ۱ (خیلی مهم)
الان threshold_optimizer.py فقط F1 را بهینه می‌کند.
این برای Titanic خوب است اما برای پروژه‌های مالی اشتباه است.
بعداً باید این ساختار را داشته باشیم:

OPTIMIZATION_METRIC = "f1"
# یا
OPTIMIZATION_METRIC = "precision"
# یا
OPTIMIZATION_METRIC = "recall"
# یا
OPTIMIZATION_METRIC = "profit"

یعنی Threshold Optimizer باید Metric-Driven باشد نه F1-Hardcoded.

فعلاً برای Titanic مشکلی نیست ولی در فازهای بعدی اصلاحش می‌کنیم.
'''

