import pytest
from funkcje import *

def test_add():
    assert add(2, 3) == 5
    assert not add(5, 7) != 12