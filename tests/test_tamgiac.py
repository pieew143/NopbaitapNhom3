# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
import pytest
from src.tamgiac import sorting, canhtamgiac
from unittest.mock import patch
import os


@pytest.fixture
def mockis_tamgiac(mocker, sorting):
    mocker.patch("src.tamgiac.sorting", return_value=sorting)

@pytest.mark.parametrize(
    "a,b,c, sorting, tamgiac",
    [
        (3,4,5, (5,3,4) , (5,3,4) ),
        (2,3,4, (4,2,3) , (4,2,3) ),
        (3,4,6, (6,3,4) , (6,3,4) ),
        (2,3,3, (3,2,3) , (3,2,3) ),
        (3,3,5, (5,3,3) , (5,3,3) ),
        (3,3,3, (3,3,3) , (3,3,3) ),
        (5,5,12, (12,5,5) , (12,5,5) )
    ],
)
@pytest.mark.usefixtures("mockis_tamgiac")
def test_tamgiac(a,b,c, tamgiac):
    assert sorting(a,b,c) == tamgiac

@pytest.mark.parametrize(
    "a,b,c, output",
    [
        (3, 4, 5,  ("tam giac la tam giac vuong")),
        (5, 4, 6,  ("tam giac la tam giac nhon")),
        (3, 4, 6, ("tam giac la tam giac tu")),
        (2, 3, 3,  ("tam giac la tam giac nhon", "tam giac la tam giac can")),
        (3, 3, 5,  ("tam giac la tam giac tu", "tam giac la tam giac can")),
        (3, 3, 3,  ("tam giac la tam giac nhon", 'tam giac la tam giac deu')),
        (5, 5, 12,  ("a,b,c khong la ba canh cua tam giac"))
    ],
)
def test_canhtamgiac(a,b,c, output):
    assert canhtamgiac(a,b,c) == output

#Press Dou Shift to search everywhere for classes, files, tool windows, actions, and
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

