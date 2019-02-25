import numpy as np


def test_root(client):
    response = client.get("/")
    assert response.status_code == 404


def test_ui(client):
    response = client.get("/ui/")
    assert response.status_code == 200


def test_dummy_predict_proba(client):
    response = client.get("/dummy_model/predict_proba?model_version=1&x1=1&x2=2")
    assert response.status_code == 200
    np.testing.assert_almost_equal(response.json, 0.9678337)
