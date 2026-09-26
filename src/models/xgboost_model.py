import xgboost as xgb
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score,
    matthews_corrcoef
)


def train_xgboost(X, y, test_size=0.30, random_state=123):
    """
    Train an XGBoost classifier.

    Parameters
    ----------
    X : pandas.DataFrame
        Feature matrix.
    y : pandas.Series
        Target labels.
    test_size : float
        Fraction of data used for testing.
    random_state : int
        Random seed for reproducibility.

    Returns
    -------
    model : XGBClassifier
        Trained XGBoost model.
    X_train, X_test, y_train, y_test
        Training and testing datasets.
    """

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )

    model = xgb.XGBClassifier(
        scale_pos_weight=1,
        base_score=0.5,
        booster="gbtree",
        learning_rate=0.25,
        max_bin=256,
        max_depth=6,
        n_estimators=50,
        random_state=random_state,
        eval_metric="logloss"
    )

    model.fit(X_train, y_train)

    return model, X_train, X_test, y_train, y_test


def evaluate_xgboost(model, X_test, y_test):
    """
    Evaluate a trained XGBoost model.
    """

    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]

    accuracy = accuracy_score(y_test, predictions)
    roc_auc = roc_auc_score(y_test, probabilities)
    mcc = matthews_corrcoef(y_test, predictions)
    matrix = confusion_matrix(y_test, predictions)
    report = classification_report(y_test, predictions)

    results = {
        "accuracy": accuracy,
        "roc_auc": roc_auc,
        "mcc": mcc,
        "confusion_matrix": matrix,
        "classification_report": report
    }

    return results


def save_xgboost_model(model, output_path):
    """
    Save a trained XGBoost model.
    """

    model.save_model(output_path)


def load_xgboost_model(model_path):
    """
    Load a previously trained XGBoost model.
    """

    model = xgb.XGBClassifier()
    model.load_model(model_path)

    return model


def predict_xgboost(model, X):
    """
    Generate predictions and prediction probabilities.
    """

    predictions = model.predict(X)
    probabilities = model.predict_proba(X)[:, 1]

    return predictions, probabilities
