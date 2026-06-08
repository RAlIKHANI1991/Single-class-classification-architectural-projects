# src/evaluation/visualization.py

import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay, RocCurveDisplay


class Visualizer:

    @staticmethod
    def plot_confusion_matrix(model,X_test,y_test,save_path=None):
        fig, ax = plt.subplots()
        ConfusionMatrixDisplay.from_estimator(model,X_test,y_test,ax=ax)

        if save_path:
            plt.savefig(save_path,bbox_inches="tight")
        plt.close()


    @staticmethod
    def plot_roc_curve(model,X_test,y_test,save_path=None):
        fig, ax = plt.subplots()
        RocCurveDisplay.from_estimator(model,X_test,y_test,ax=ax)

        if save_path:
            plt.savefig(save_path,bbox_inches="tight")
        plt.close()