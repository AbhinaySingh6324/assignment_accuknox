import pytest
from maintask1 import main
# @pytest.mark.fast
def test_task1(*args):
    a = main("Accuknox2.txt")
    assert a==True
    # assert 2==3
    b = main("Accuknox3.txt")
    assert b==False