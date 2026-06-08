# workflows/deployment_workflow.py
from src.utils.io import save_model
from config.paths import MODEL_FILE

class DeploymentWorkflow:
    """
    ذخیره مدل نهایی
    """

    @staticmethod
    def run(best_model):

        save_model(best_model,MODEL_FILE)

'''
آماده‌سازی مدل برای Deployment
فعلاً ساده نگه می‌داریم.

'''