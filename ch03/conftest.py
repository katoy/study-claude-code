import sys

import pytest


@pytest.fixture(autouse=True)
def reset_modules():
    yield
    if "multiply" in sys.modules:
        del sys.modules["multiply"]
