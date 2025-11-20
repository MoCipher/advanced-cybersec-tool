import pytest

@pytest.fixture(scope="session")
def setup_environment():
    # Setup code for the test environment
    pass

@pytest.fixture
def sample_data():
    # Provide sample data for tests
    return {
        "ip": "192.168.1.1",
        "port": 80,
        "protocol": "tcp"
    }