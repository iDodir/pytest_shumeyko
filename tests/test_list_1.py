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


@pytest.mark.usefixtures("empty_candies")
class TestCandies:
    def test_count_candies(self, candies):
        for candy in candies:
            CandiesService.add(candy)

        assert CandiesService.count() == 3

    def test_list_candies(self, candies):
        for candy in candies:
            CandiesService.add(candy)

        all_candies = CandiesService.list()
        for added_candy in all_candies:
            assert CandySchema(**added_candy) in candies
