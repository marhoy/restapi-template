import os.path

from sklearn import datasets, ensemble
from sklearn.externals import joblib

MODEL_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), 'model_files'
)


def get_model_filename(model: str, model_version: int) -> str:
    filename = os.path.join(MODEL_DIR, '{}_v{}.joblib'.format(model, model_version))
    return filename


def make_test_model(model_name: str, model_version: int) -> None:
    # Generate some data
    x, y = datasets.make_classification(n_samples=1000, n_features=2,
                                        n_informative=2, n_redundant=0,
                                        random_state=0, shuffle=False)
    # Train a classifier
    clf = ensemble.RandomForestClassifier(max_depth=2, random_state=0)
    clf.fit(x, y)
    # Save the model as a binary file
    joblib.dump(clf, get_model_filename(model_name, model_version))
