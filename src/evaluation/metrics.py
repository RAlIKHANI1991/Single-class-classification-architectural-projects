# src/evaluation/metrics.py

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import roc_auc_score,average_precision_score


class MetricsCalculator:

    @staticmethod
    def calculate_metrics(y_true,y_pred,y_proba):

        return {
            "accuracy"  : float(accuracy_score(y_true,y_pred)),
            "precision" : float(precision_score(y_true,y_pred)),
            "recall"    : float(recall_score(y_true,y_pred)),
            "f1"        : float(f1_score(y_true,y_pred)),
            "roc_auc"   : float(roc_auc_score(y_true,y_proba)),
            "pr_auc"    : float(average_precision_score(y_true,y_proba))
        }
    
'''
هدف:

تمام محاسبات Metric در یک مکان متمرکز باشد.

چرا PR-AUC اضافه کردیم؟
اکثر آموزش‌ها فقط:
ROC_AUC
را محاسبه می‌کنند.
اما در:
Fraud Detection
Churn
Credit Default
Rare Events

مهم‌ترین معیار معمولاً:
PR_AUC
است.
از الان در پروژه وجود دارد.
'''