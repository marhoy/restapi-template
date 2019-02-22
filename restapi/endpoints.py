from .utils import get_model_filename
from sklearn.externals import joblib
import numpy as np


def load_model(model, model_version):
    filename = get_model_filename(model, model_version)
    model = joblib.load(filename)
    return model


def dummy_model(model_version: int, x1: float, x2: float) -> float:
    model = load_model('dummy', model_version)
    x = np.array([[x1, x2]])
    return model.predict_proba(x)[0, 1]
