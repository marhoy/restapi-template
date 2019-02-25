import os

import pytest

import restapi


@pytest.fixture
def client():
    model_name = "test_model"
    model_version = 1
    print("Creating a temporary model")
    restapi.utils.make_test_model(model_name, model_version)
    app = restapi.create_app()
    client = app.app.test_client()
    yield client
    print("Removing temporary model")
    os.remove(restapi.utils.get_model_filename(model_name, model_version))
