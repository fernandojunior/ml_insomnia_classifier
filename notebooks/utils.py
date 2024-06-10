from sklearn.metrics import confusion_matrix
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score


sensitivity_score = recall_score


def specificity_score(y_true, y_pred):
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    return tn / (tn+fp)


def evaluate_scores(y_true, y_pred):
    accuracy_result = accuracy_score(y_true, y_pred)
    sensitivity_result = sensitivity_score(y_true, y_pred)
    specificity_result = specificity_score(y_true, y_pred)

    print("Classification Scores: accuracy={} sensitivity={} specificity={}".format(accuracy_result, sensitivity_result, specificity_result))

    return accuracy_result, sensitivity_result, specificity_result

