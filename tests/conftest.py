import time

import pytest

from src.config import settings
from src.db import Base, engine


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    print(f"{settings.DB_NAME=}")
    assert settings.MODE == "TEST"
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        choices=("chrome", "firefox"),
    )
    parser.addoption(
        "--run-slow",
        default="true",
        choices=("true", "false"),
    )


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


def test_1(browser):
    print(browser)


# @pytest.mark.skip(reason="Slow test")
@pytest.mark.skipif('config.getoption("--run-slow") == "false"')
def test_slow():
    time.sleep(3)


def test_fast():
    pass


def test_fast_2():
    time.sleep(2)


def test_fast_1():
    time.sleep(1)
