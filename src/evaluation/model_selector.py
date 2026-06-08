# src/evaluation/model_selector.py

class ModelSelector:

    @staticmethod
    def select_best_model(evaluation_results,metric="roc_auc"):

        best_model = max(
            evaluation_results,key=lambda model:
            evaluation_results[model][metric])

        return best_model
    

'''
مثال:
results = {
    "lr": {"roc_auc": 0.82},
    "rf": {"roc_auc": 0.85},
    "xgb": {"roc_auc": 0.87}
}

خروجی:

"xgb"
نکته ۳ (بسیار مهم)
در پروژه‌های واقعی:
Best CV Score
همیشه برابر با
Best Business Model
نیست.

مثلاً:
Model	ROC_AUC
RF	0.85
XGB	0.86

اگر XGB:
۱۰ برابر کندتر باشد
Explainability نداشته باشد
API را سنگین کند
ممکن است RF انتخاب شود.
بنابراین در آینده ModelSelector باید چندمعیاره شود.

'''