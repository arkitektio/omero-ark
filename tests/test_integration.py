import pytest
from omero_ark.api.schema import list_images
from omero_ark.deployed import DeployedOmeroArk




@pytest.mark.integration
def test_list_images(deployed_app: DeployedOmeroArk):



    with deployed_app.deployment.logswatcher("omero_ark") as logs:
        # Wait for the health check to pass
        images = list_images()
        assert len(images) == 0, "There should be no images in the database"

