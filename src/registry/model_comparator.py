# src/registry/model_comparator.py

class ModelComparator:

    @staticmethod
    def is_better(new_score, old_score):

        return new_score > old_score
    

'''
فعلاً ساده است.
بعداً می‌توانیم اضافه کنیم:
minimum_improvement
مثلاً:
0.5%
بهبود حداقل لازم.
نکته بسیار مهم برای پروژه‌های مالی
بیشتر افراد این اشتباه را می‌کنند:
ROC_AUC بهتر شد
مدل را Deploy کن
این خطرناک است.

مثال:
Version	ROC_AUC
v1	0.851
v2	0.853

اختلاف:
0.002
ممکن است صرفاً نویز باشد.

بعداً باید چیزی شبیه این داشته باشیم:
MIN_IMPROVEMENT = 0.01
یعنی:
حداقل 1 درصد بهبود

'''