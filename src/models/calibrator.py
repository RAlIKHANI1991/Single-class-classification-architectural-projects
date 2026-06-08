# src/models/calibrator.py

from sklearn.calibration import CalibratedClassifierCV


class ModelCalibrator:

    @staticmethod
    def calibrate(model,X_train,y_train):

        calibrated_model = (CalibratedClassifierCV(estimator=model,method="sigmoid",cv=5))
        calibrated_model.fit(X_train,y_train)

        return calibrated_model
 
 
#این قسمت معمولاً در پروژه‌های آموزشی وجود ندارد ولی در Production اهمیت زیادی دارد.   
'''
چرا Calibration؟
فرض کن مدل می‌گوید:
Probability = 0.90
واقعاً باید حدود:
90%
موارد درست باشد.
اما معمولاً:
RandomForest
XGBoost
احتمال‌ها را بیش از حد خوش‌بینانه تخمین می‌زنند.
Calibration این مشکل را حل می‌کند.
'''