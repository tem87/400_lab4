import docker
import os
# test_with_pytest.py

def test_always_passes():
    assert True

def test_docker_running():
    """Check if Docker is running inside the container."""
    client = docker.from_env()
    assert client.ping(), "Docker daemon is not accessible inside the container!"

def test_volume_mount():
    """Ensure the project folder is correctly mounted in the container."""
    assert os.path.exists("/src"), "Project source directory is not mounted!"
    assert os.path.isdir("/src"), "Expected /src to be a directory!"

# def test_always_fails():
#     assert False
