import pytest
from src.exercise import print_until_number

def test_exercise(capsys):
    print_until_number(4)
    out, err = capsys.readouterr()
    assert out == "1\n2\n3\n4\n", "Should read '1\n2\n3\n4\n'"
