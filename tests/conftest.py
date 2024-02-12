import pytest
from omero_ark.deployed import DeployedOmeroArk, deployed
from typing import Iterator
from omero_ark.api.schema import ensure_omero_user


@pytest.fixture(scope="session")
def deployed_app() -> Iterator[DeployedOmeroArk]:
    """A deployed kluster"""
    app = deployed()
    app.deployment.project.overwrite = True
    app.deployment.health_on_enter = True
    app.deployment.down_on_exit = True
    with app:

        with app.deployment.logswatcher("omero_ark") as logs:
            user = ensure_omero_user(username="root", password="omero", host="omeroserver", port=4064)




        yield app
