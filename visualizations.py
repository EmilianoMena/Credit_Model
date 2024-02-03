# Libraries and dependencies
import main as m
import matplotlib.pyplot as plt
from sklearn import metrics

# Confusion matrix
confusion_matrix = metrics.confusion_matrix(m.original_score, m.model_score)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = m.values7)