import unittest
import pytest
from prost import prov_prost

class TestProv_prost(unittest.TestCase):
    def test_add(self):
        self.assertEqual(prov_prost(5), True)
        self.assertEqual(prov_prost(100),False)
        self.assertEqual(prov_prost(4),False)
unittest.main(exit=False)

@pytest.mark.parametrize("number, expected_result",[(0,False),
                                                    (1, True),
                                                    (4,False),
                                                    (5,True),
                                                    (10,False),
                                                    (60000000000003, False)])

def test_prov(number,expected_result):
    assert prov_prost(number) == expected_result
@pytest.mark.parametrize("exp_expetion, entered",[(TypeError,'a'),
                                                  (ValueError, 1)])# Пример неудачного теста
def test_type_error(exp_expetion,entered):
    with pytest.raises(exp_expetion):
        prov_prost(exp_expetion,entered)