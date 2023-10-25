import pytest

from src.candies.schemas import CandySchema
from src.candies.service import CandiesService


@pytest.fixture
def candies():
    candies = [
        CandySchema(title="candy1", owner="dodir"),
        CandySchema(title="candy2", state="eaten"),
        CandySchema(title="candy3", state="half"),
    ]
    return candies


@pytest.fixture(scope="function")
def empty_candies():
    CandiesService.delete_all()
